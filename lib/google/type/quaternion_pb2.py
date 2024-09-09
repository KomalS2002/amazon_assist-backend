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
# source: google/type/quaternion.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1cgoogle/type/quaternion.proto\x12\x0bgoogle.type"8\n\nQuaternion\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\t\n\x01w\x18\x04 \x01(\x01\x42o\n\x0f\x63om.google.typeB\x0fQuaternionProtoP\x01Z@google.golang.org/genproto/googleapis/type/quaternion;quaternion\xf8\x01\x01\xa2\x02\x03GTPb\x06proto3'
)


_QUATERNION = DESCRIPTOR.message_types_by_name["Quaternion"]
Quaternion = _reflection.GeneratedProtocolMessageType(
    "Quaternion",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUATERNION,
        "__module__": "google.type.quaternion_pb2"
        # @@protoc_insertion_point(class_scope:google.type.Quaternion)
    },
)
_sym_db.RegisterMessage(Quaternion)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\017com.google.typeB\017QuaternionProtoP\001Z@google.golang.org/genproto/googleapis/type/quaternion;quaternion\370\001\001\242\002\003GTP"
    _QUATERNION._serialized_start = 45
    _QUATERNION._serialized_end = 101
# @@protoc_insertion_point(module_scope)
