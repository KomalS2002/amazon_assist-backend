from fastapi import FastAPI, APIRouter, Depends, status, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import requests
import json
import shutil
import re
import os
from pathlib import Path
from dotenv import load_dotenv
from models.text_to_desc import textDescModel
from g4f.client import Client 
from g4f.Provider.GeminiPro import GeminiPro 
from g4f.Provider.GeminiProChat import GeminiProChat
from database.dbconnect import get_db,Base
from sqlalchemy.orm import Session
from models.user import Users
from authUtils.JWTBearer import JWTBearer
from PIL import Image
import io
from fastapi.encoders import jsonable_encoder
import time
from g4f.Provider.FreeChatgpt import FreeChatgpt
import boto3
import tempfile
import moviepy.editor as mp
import speech_recognition as sr
from models.history import Historys
from pydub import AudioSegment
import yt_dlp

router = APIRouter()
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Initialize the client with the GeminiPro provider
client = Client(provider=GeminiProChat,api_key=gemini_api_key)
clientimage = Client(provider=GeminiPro, api_key=gemini_api_key)

# Prompts
set_lang_english = "Reply only in English; "
# text_prompt_instructions = "; identify the products described here and generate keywords related to the product which will help in searching the product on Amazon (return the result as JSON in the format product:{keywords}) (if no products are found then return response as product:{-1}) ONLY RETURN THE JSON DO NOT WRITE ANYTHING ELSE NOT A SINGLE WORD EXTRA JUST THE JSON"
# image_identify_prompt_instructions = "; identify the products present here and generate keywords related to the product which will help in searching the product on Amazon like build, color, style, design. DO NOT DESCRIBE THE IMAGE JUST WRITE THE KEYWORDS FOR THE DIFFERENT ITEMS PRESENT IN THE IMAGE (return the result as JSON in the format product:{keywords}) (if no products are found then return response as product:{-1}) ONLY RETURN THE JSON DO NOT WRITE ANYTHING ELSE NOT A SINGLE WORD EXTRA JUST THE JSON ONLY WRITE KEYWORDS"
# image_identify_prompt_instructions2 = "; (return the result as JSON where the actual name of each item is the key and the keywords decribing its characteristics are the value) (discard any product for which proper keywords are not found) (if no products are found then return response as message:{-1}) ONLY RETURN THE JSON DO NOT WRITE ANYTHING ELSE NOT A SINGLE WORD EXTRA JUST THE JSON ONLY WRITE KEYWORDS"



HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": f"Bearer {huggingface_api_key}",
           "language":'en',
        }
HUGGINGFACE_SPEECH_TO_TEXT_API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"



def query(payload, max_retries=10, retry_delay=30):
    retries = 0
    while retries < max_retries:
        response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)
        if response.status_code == 503:
            # Model is currently loading, wait and retry
            wait_time = retry_delay * (2 ** retries)
            print(f"Model is currently loading. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
            retries += 1
        elif response.status_code == 200:
            return response.content
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
    
    print(f"Failed after {max_retries} retries.")
    return None


def s3fileUpload(file_content:UploadFile,item_name:str):
    if file_content:
        s3.upload_fileobj(file_content,BUCKET_NAME,f"{item_name}.png")
        link = "https://d1voydi2q6xpb1.cloudfront.net/"f"{item_name}.png"
        return link
    else:
        return "error in uploading"


# def save_image(image_bytes, item_name):
#     image_path = f"images/{item_name.replace(' ', '_')}.png"
#     os.makedirs(os.path.dirname(image_path), exist_ok=True)
#     with open(image_path, 'wb') as f:
#         f.write(image_bytes)
#         # image_link1 = s3fileUpload(image)
#         # print(image_link1)
#     return image_path

def convert_to_dict(json_data):
    # Convert json_data from string-value format to dict format
    dict_data = []
    for item_name, tags_str in json_data.items():
        tags = [tag.strip() for tag in tags_str.split(',')]
        dict_data.append({item_name: tags})
    return dict_data

def generate_images_from_json(json_data,db:Session):
# def generate_images_from_json(json_data):
    db_history = Historys()
    new_json = {}
    for item in json_data:
        if item: 
            # item_name = next(iter(item))  # Get the key (item name) from the dictionary
            tags = json_data[item]  # Get the value (list of tags) from the dictionary  
            prompt = f"{item}: {', '.join(tags)}"
            print(prompt)
            image_bytes = query({"inputs": prompt})
            
            if image_bytes:
                try:
                    # image_link = save_image(image_bytes, item)
                    image = io.BytesIO(image_bytes)
                    image_link = s3fileUpload(image,item)
                    print(image_link)

                    new_json[item] = {
                        "tags": ', '.join(tags),
                        "image_link": image_link
                    }
                    # saving to database
                    db_history.user_id = "86ae4637-3806-4420-b13e-c8286dbb81ab"
                    db_history.item_name = item
                    db_history.link = image_link
                    db.add(db_history)
                    db.commit()
                    db.refresh(db_history)
                    print("data saved to database")

                except IOError:
                    print(f"Error: Could not generate image for {item}")
                    new_json[item] = {
                        "tags": ', '.join(tags),
                        "image_link": "Error: Image could not be generated"
                    }
        else:
            print(f"Error: Invalid item format in json_data: {item}")
    
    return new_json


def extract_json(input_string):
    try:
        parsed_json = json.loads(input_string)
        return parsed_json
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return None

# 
#after testing comment out below line

@router.post("/text")
def textToDesc(request: textDescModel,db: Session = Depends(get_db)):
# def textToDesc(request: textDescModel):
    print(request.text)
    if request.text:
        ntpi= '; extract keywords related to each object described here and list them like this: {"Product name 1": ["feature 1","Feature 2","feature 3"],"Product name 2": ["feature 1","Feature 2","feature 3"],"Product name 3": ["feature 1","Feature 2","feature 3"],}'
        prompt = request.text + ntpi
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )

        if response.choices[0].message.content:
            response_json = response.choices[0].message.content
            print(response_json)
            print("###########################################3")
            response_json = extract_json(response_json)
            if response_json:
                newjson = generate_images_from_json(response_json,db)
                # newjson = generate_images_from_json(response_json)
                print(newjson)
                return newjson  # Using the default Status code i.e. Status 200
            else:
                msg = [{"message": "Incorrect data/missing data"}]
                return JSONResponse(content=jsonable_encoder(msg), status_code=status.HTTP_404_NOT_FOUND)
        else:
            return f"Error: {response.status_code}, {response.text}"
    else:
        msg = [{"message": "Incorrect data/missing data"}]
        return JSONResponse(content=jsonable_encoder(msg), status_code=status.HTTP_404_NOT_FOUND)
    




#after testing comment out below line
# def upload_image(file: UploadFile = File(...),db: Session = Depends(get_db),user: Users = Depends(JWTBearer())): 
@router.post("/image")
def upload_image(file: UploadFile = File(...),db: Session = Depends(get_db)):
    try:
        # Save the uploaded file locally
        upload_folder = Path("uploaded_images")
        upload_folder.mkdir(exist_ok=True)
        file_path = upload_folder / file.filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
       
        # Use the image with g4f.client
        with file_path.open("rb") as img:
            # ntpi= '; find name of products in image and list product name and features like this json list : "{"Product name 1": ["feature 1","Feature 2","feature 3"],"Product name 2": ["feature 1","Feature 2","feature 3"],"Product name 3": ["feature 1","Feature 2","feature 3"],};without ``` '
            ntpi1= '; only return name of product;without ``` '
            # prompt = set_lang_english+ntpi+image_identify_prompt_instructions2
            response = clientimage.chat.completions.create(
                model="gemini-pro-vision",
                messages=[{"role": "user", "content": ntpi1}],
                image=img
            )
        # Extract the response content
        response_content = response.choices[0].message.content
        print(response_content)
        # Delete the locally saved image
        file_path.unlink()

        ntpi2= '; for the products given ,list product names as key and features as value in given prompt like this: {"Product name 1": ["feature 1","Feature 2","feature 3"],"Product name 2": ["feature 1","Feature 2","feature 3"],"Product name 3": ["feature 1","Feature 2","feature 3"],}; without ```'
        prompt = set_lang_english+ response_content+ntpi2
        response1 = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )

        if response1.choices[0].message.content:
            response_json = response1.choices[0].message.content
            print(response_json)
            response_json = extract_json(response_json)
            if response_json:
                newjson = generate_images_from_json(response_json,db)
                # new_json = generate_images_from_json(response_json)
                return newjson  # Using the default Status code i.e. Status 200
            else:
                msg = [{"message": "Incorrect data/missing data"}]
                return JSONResponse(content=jsonable_encoder(msg), status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return f"Error: {response.status_code}, {response.text}"

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


temp_dir = tempfile.mkdtemp()
def transcribe_video(video_path):
    # Load the video file
    video = mp.VideoFileClip(video_path)

    # Extract audio from the video
    audio = video.audio

    # Save audio to a temporary file
    audio_temp_file = os.path.join(temp_dir, "temp_audio.wav")
    audio.write_audiofile(audio_temp_file)

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Recognize speech from the audio
    with sr.AudioFile(audio_temp_file) as source:
        audio_data = recognizer.record(source)
        try:
            # Use Google Web Speech API to perform speech recognition
            transcript = recognizer.recognize_google(audio_data, language="en-US")  # Adjust language if needed
            return transcript
        except sr.UnknownValueError:
            return "Speech recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"
        

 
@router.post("/video")
# def process_video(file: UploadFile = File(...),db: Session = Depends(get_db),user: Users = Depends(JWTBearer())):
def process_video(file: UploadFile = File(...),db: Session = Depends(get_db)):
    try:
        # Save the uploaded video file temporarily
        video_path = os.path.join(temp_dir, file.filename)
        with open(video_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        # Transcribe the video
        transcription = transcribe_video(video_path)
        print(transcription)
        ntpi= '; extract keywords related to each object described here and list them like this: {"Product name 1": ["feature 1","Feature 2","feature 3"],"Product name 2": ["feature 1","Feature 2","feature 3"],"Product name 3": ["feature 1","Feature 2","feature 3"],}'
        prompt = transcription + ntpi
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        if response.choices[0].message.content:
            response_json = response.choices[0].message.content
            print(response_json)
            response_json = extract_json(response_json)
            if response_json:
                newjson = generate_images_from_json(response_json,db)
                # newjson = generate_images_from_json(response_json)
                print(newjson)
                return newjson  # Using the default Status code i.e. Status 200
            else:
                msg = [{"message": "Incorrect data/missing data"}]
                return JSONResponse(content=jsonable_encoder(msg), status_code=status.HTTP_404_NOT_FOUND)
        else:
            return f"Error: {response.status_code}, {response.text}"
    except:
        msg = [{"message": "Incorrect data/missing data"}]
        return JSONResponse(content=jsonable_encoder(msg), status_code=status.HTTP_404_NOT_FOUND)
    
    
def download_audio(url: str, output_path: str) -> str:
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path + '.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return f"{output_path}.m4a"


def ytquery(filename: str):
    max_retries = 5
    retry_count = 0
    retry_delay = 100  # seconds
    while retry_count < max_retries:
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(HUGGINGFACE_SPEECH_TO_TEXT_API_URL, headers=headers, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            response_data = response.json()
            if "error" in response_data:
                if "currently loading" in response_data["error"]:
                    estimated_time = response_data.get("estimated_time", retry_delay)
                    print(f"Model is loading. Retrying in {estimated_time} seconds...")
                    time.sleep(estimated_time)
                    retry_count += 1
                else:
                    print(f"Error from API: {response_data['error']}")
                    raise HTTPException(status_code=400, detail=response_data['error'])
            else:
                response.raise_for_status()
    raise Exception("Failed to get a response after multiple retries.")


def split_audio_to_chunks(audio, chunk_length_ms: int = 30000):
    duration_ms = len(audio)
    chunks = []
    for start in range(0, duration_ms, chunk_length_ms):
        end = min(start + chunk_length_ms, duration_ms)
        chunk = audio[start:end]
        chunks.append(chunk)
    return chunks


def export_audio_chunk_to_wav(chunk, filename: str):
    # Export the chunk to WAV format
    chunk.export(filename, format="wav")
    return filename


def process_audio_chunks(filename: str, chunk_length_ms: int = 30000):
    audio = AudioSegment.from_file(filename)
    chunks = split_audio_to_chunks(audio, chunk_length_ms)
    results = []
    for i, chunk in enumerate(chunks):
        chunk_filename = f"{filename}_{i}.wav"
        wav_chunk_filename = export_audio_chunk_to_wav(chunk, chunk_filename)
        result = ytquery(wav_chunk_filename)
        results.append(result)
        os.remove(wav_chunk_filename)  # Clean up chunk file
    return results


@router.post("/youtube-video")
def youtube_video(request: dict,db: Session = Depends(get_db)):
    if 'url' not in request:
        raise HTTPException(status_code=400, detail="URL is missing in the request")

    video_url = request['url']
    output_filename = "downloaded_audio"

    try:
        final_output_filename = download_audio(video_url, output_filename)
        results = process_audio_chunks(final_output_filename)
        os.remove(final_output_filename)  # Clean up the downloaded file
        combined_result = "\n".join([result["text"] for result in results])
        ntpi= '; extract keywords related to each object described here and list them like this: {"Product name 1": ["feature 1","Feature 2","feature 3"],"Product name 2": ["feature 1","Feature 2","feature 3"],"Product name 3": ["feature 1","Feature 2","feature 3"],}'
        prompt = combined_result+ ntpi
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        )
        if response.choices[0].message.content:
            response_json = response.choices[0].message.content
            print(response_json)
            response_json = extract_json(response_json)
            if response_json:
                newjson = generate_images_from_json(response_json,db)
                print(newjson)
                return newjson  # Using the default Status code i.e. Status 200
            else:
                msg = [{"message": "Incorrect data/missing data"}]
                return JSONResponse(content=jsonable_encoder(msg), status_code=status.HTTP_404_NOT_FOUND)
        else:
            return f"Error: {response.status_code}, {response.text}"
        
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
