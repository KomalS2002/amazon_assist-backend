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
# source: google/api/launch_stage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\n\x1dgoogle/api/launch_stage.proto\x12\ngoogle.api*\x8c\x01\n\x0bLaunchStage\x12\x1c\n\x18LAUNCH_STAGE_UNSPECIFIED\x10\x00\x12\x11\n\rUNIMPLEMENTED\x10\x06\x12\r\n\tPRELAUNCH\x10\x07\x12\x10\n\x0c\x45\x41RLY_ACCESS\x10\x01\x12\t\n\x05\x41LPHA\x10\x02\x12\x08\n\x04\x42\x45TA\x10\x03\x12\x06\n\x02GA\x10\x04\x12\x0e\n\nDEPRECATED\x10\x05\x42Z\n\x0e\x63om.google.apiB\x10LaunchStageProtoP\x01Z-google.golang.org/genproto/googleapis/api;api\xa2\x02\x04GAPIb\x06proto3"
)

_LAUNCHSTAGE = DESCRIPTOR.enum_types_by_name["LaunchStage"]
LaunchStage = enum_type_wrapper.EnumTypeWrapper(_LAUNCHSTAGE)
LAUNCH_STAGE_UNSPECIFIED = 0
UNIMPLEMENTED = 6
PRELAUNCH = 7
EARLY_ACCESS = 1
ALPHA = 2
BETA = 3
GA = 4
DEPRECATED = 5


if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\016com.google.apiB\020LaunchStageProtoP\001Z-google.golang.org/genproto/googleapis/api;api\242\002\004GAPI"
    _LAUNCHSTAGE._serialized_start = 46
    _LAUNCHSTAGE._serialized_end = 186
# @@protoc_insertion_point(module_scope)
