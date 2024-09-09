# -*- coding: utf-8 -*-

# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/rpc/error_details.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1egoogle/rpc/error_details.proto\x12\ngoogle.rpc\x1a\x1egoogle/protobuf/duration.proto"\x93\x01\n\tErrorInfo\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x35\n\x08metadata\x18\x03 \x03(\x0b\x32#.google.rpc.ErrorInfo.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01";\n\tRetryInfo\x12.\n\x0bretry_delay\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration"2\n\tDebugInfo\x12\x15\n\rstack_entries\x18\x01 \x03(\t\x12\x0e\n\x06\x64\x65tail\x18\x02 \x01(\t"y\n\x0cQuotaFailure\x12\x36\n\nviolations\x18\x01 \x03(\x0b\x32".google.rpc.QuotaFailure.Violation\x1a\x31\n\tViolation\x12\x0f\n\x07subject\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t"\x95\x01\n\x13PreconditionFailure\x12=\n\nviolations\x18\x01 \x03(\x0b\x32).google.rpc.PreconditionFailure.Violation\x1a?\n\tViolation\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0f\n\x07subject\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t"\x83\x01\n\nBadRequest\x12?\n\x10\x66ield_violations\x18\x01 \x03(\x0b\x32%.google.rpc.BadRequest.FieldViolation\x1a\x34\n\x0e\x46ieldViolation\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t"7\n\x0bRequestInfo\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x14\n\x0cserving_data\x18\x02 \x01(\t"`\n\x0cResourceInfo\x12\x15\n\rresource_type\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t"V\n\x04Help\x12$\n\x05links\x18\x01 \x03(\x0b\x32\x15.google.rpc.Help.Link\x1a(\n\x04Link\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t"3\n\x10LocalizedMessage\x12\x0e\n\x06locale\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\tBl\n\x0e\x63om.google.rpcB\x11\x45rrorDetailsProtoP\x01Z?google.golang.org/genproto/googleapis/rpc/errdetails;errdetails\xa2\x02\x03RPCb\x06proto3'
)


_ERRORINFO = DESCRIPTOR.message_types_by_name["ErrorInfo"]
_ERRORINFO_METADATAENTRY = _ERRORINFO.nested_types_by_name["MetadataEntry"]
_RETRYINFO = DESCRIPTOR.message_types_by_name["RetryInfo"]
_DEBUGINFO = DESCRIPTOR.message_types_by_name["DebugInfo"]
_QUOTAFAILURE = DESCRIPTOR.message_types_by_name["QuotaFailure"]
_QUOTAFAILURE_VIOLATION = _QUOTAFAILURE.nested_types_by_name["Violation"]
_PRECONDITIONFAILURE = DESCRIPTOR.message_types_by_name["PreconditionFailure"]
_PRECONDITIONFAILURE_VIOLATION = _PRECONDITIONFAILURE.nested_types_by_name["Violation"]
_BADREQUEST = DESCRIPTOR.message_types_by_name["BadRequest"]
_BADREQUEST_FIELDVIOLATION = _BADREQUEST.nested_types_by_name["FieldViolation"]
_REQUESTINFO = DESCRIPTOR.message_types_by_name["RequestInfo"]
_RESOURCEINFO = DESCRIPTOR.message_types_by_name["ResourceInfo"]
_HELP = DESCRIPTOR.message_types_by_name["Help"]
_HELP_LINK = _HELP.nested_types_by_name["Link"]
_LOCALIZEDMESSAGE = DESCRIPTOR.message_types_by_name["LocalizedMessage"]
ErrorInfo = _reflection.GeneratedProtocolMessageType(
    "ErrorInfo",
    (_message.Message,),
    {
        "MetadataEntry": _reflection.GeneratedProtocolMessageType(
            "MetadataEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _ERRORINFO_METADATAENTRY,
                "__module__": "google.rpc.error_details_pb2"
                # @@protoc_insertion_point(class_scope:google.rpc.ErrorInfo.MetadataEntry)
            },
        ),
        "DESCRIPTOR": _ERRORINFO,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.ErrorInfo)
    },
)
_sym_db.RegisterMessage(ErrorInfo)
_sym_db.RegisterMessage(ErrorInfo.MetadataEntry)

RetryInfo = _reflection.GeneratedProtocolMessageType(
    "RetryInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _RETRYINFO,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.RetryInfo)
    },
)
_sym_db.RegisterMessage(RetryInfo)

DebugInfo = _reflection.GeneratedProtocolMessageType(
    "DebugInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _DEBUGINFO,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.DebugInfo)
    },
)
_sym_db.RegisterMessage(DebugInfo)

QuotaFailure = _reflection.GeneratedProtocolMessageType(
    "QuotaFailure",
    (_message.Message,),
    {
        "Violation": _reflection.GeneratedProtocolMessageType(
            "Violation",
            (_message.Message,),
            {
                "DESCRIPTOR": _QUOTAFAILURE_VIOLATION,
                "__module__": "google.rpc.error_details_pb2"
                # @@protoc_insertion_point(class_scope:google.rpc.QuotaFailure.Violation)
            },
        ),
        "DESCRIPTOR": _QUOTAFAILURE,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.QuotaFailure)
    },
)
_sym_db.RegisterMessage(QuotaFailure)
_sym_db.RegisterMessage(QuotaFailure.Violation)

PreconditionFailure = _reflection.GeneratedProtocolMessageType(
    "PreconditionFailure",
    (_message.Message,),
    {
        "Violation": _reflection.GeneratedProtocolMessageType(
            "Violation",
            (_message.Message,),
            {
                "DESCRIPTOR": _PRECONDITIONFAILURE_VIOLATION,
                "__module__": "google.rpc.error_details_pb2"
                # @@protoc_insertion_point(class_scope:google.rpc.PreconditionFailure.Violation)
            },
        ),
        "DESCRIPTOR": _PRECONDITIONFAILURE,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.PreconditionFailure)
    },
)
_sym_db.RegisterMessage(PreconditionFailure)
_sym_db.RegisterMessage(PreconditionFailure.Violation)

BadRequest = _reflection.GeneratedProtocolMessageType(
    "BadRequest",
    (_message.Message,),
    {
        "FieldViolation": _reflection.GeneratedProtocolMessageType(
            "FieldViolation",
            (_message.Message,),
            {
                "DESCRIPTOR": _BADREQUEST_FIELDVIOLATION,
                "__module__": "google.rpc.error_details_pb2"
                # @@protoc_insertion_point(class_scope:google.rpc.BadRequest.FieldViolation)
            },
        ),
        "DESCRIPTOR": _BADREQUEST,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.BadRequest)
    },
)
_sym_db.RegisterMessage(BadRequest)
_sym_db.RegisterMessage(BadRequest.FieldViolation)

RequestInfo = _reflection.GeneratedProtocolMessageType(
    "RequestInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _REQUESTINFO,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.RequestInfo)
    },
)
_sym_db.RegisterMessage(RequestInfo)

ResourceInfo = _reflection.GeneratedProtocolMessageType(
    "ResourceInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESOURCEINFO,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.ResourceInfo)
    },
)
_sym_db.RegisterMessage(ResourceInfo)

Help = _reflection.GeneratedProtocolMessageType(
    "Help",
    (_message.Message,),
    {
        "Link": _reflection.GeneratedProtocolMessageType(
            "Link",
            (_message.Message,),
            {
                "DESCRIPTOR": _HELP_LINK,
                "__module__": "google.rpc.error_details_pb2"
                # @@protoc_insertion_point(class_scope:google.rpc.Help.Link)
            },
        ),
        "DESCRIPTOR": _HELP,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.Help)
    },
)
_sym_db.RegisterMessage(Help)
_sym_db.RegisterMessage(Help.Link)

LocalizedMessage = _reflection.GeneratedProtocolMessageType(
    "LocalizedMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOCALIZEDMESSAGE,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.LocalizedMessage)
    },
)
_sym_db.RegisterMessage(LocalizedMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\016com.google.rpcB\021ErrorDetailsProtoP\001Z?google.golang.org/genproto/googleapis/rpc/errdetails;errdetails\242\002\003RPC"
    _ERRORINFO_METADATAENTRY._options = None
    _ERRORINFO_METADATAENTRY._serialized_options = b"8\001"
    _ERRORINFO._serialized_start = 79
    _ERRORINFO._serialized_end = 226
    _ERRORINFO_METADATAENTRY._serialized_start = 179
    _ERRORINFO_METADATAENTRY._serialized_end = 226
    _RETRYINFO._serialized_start = 228
    _RETRYINFO._serialized_end = 287
    _DEBUGINFO._serialized_start = 289
    _DEBUGINFO._serialized_end = 339
    _QUOTAFAILURE._serialized_start = 341
    _QUOTAFAILURE._serialized_end = 462
    _QUOTAFAILURE_VIOLATION._serialized_start = 413
    _QUOTAFAILURE_VIOLATION._serialized_end = 462
    _PRECONDITIONFAILURE._serialized_start = 465
    _PRECONDITIONFAILURE._serialized_end = 614
    _PRECONDITIONFAILURE_VIOLATION._serialized_start = 551
    _PRECONDITIONFAILURE_VIOLATION._serialized_end = 614
    _BADREQUEST._serialized_start = 617
    _BADREQUEST._serialized_end = 748
    _BADREQUEST_FIELDVIOLATION._serialized_start = 696
    _BADREQUEST_FIELDVIOLATION._serialized_end = 748
    _REQUESTINFO._serialized_start = 750
    _REQUESTINFO._serialized_end = 805
    _RESOURCEINFO._serialized_start = 807
    _RESOURCEINFO._serialized_end = 903
    _HELP._serialized_start = 905
    _HELP._serialized_end = 991
    _HELP_LINK._serialized_start = 951
    _HELP_LINK._serialized_end = 991
    _LOCALIZEDMESSAGE._serialized_start = 993
    _LOCALIZEDMESSAGE._serialized_end = 1044
# @@protoc_insertion_point(module_scope)