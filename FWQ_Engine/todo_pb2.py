# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntodo.proto\x12\x0btodoPackage\"\x0b\n\tEngineReq\")\n\x0cWaitingTimes\x12\x19\n\x11times_string_dict\x18\x01 \x01(\t2R\n\x04Todo\x12J\n\x13requestWaitingTimes\x12\x16.todoPackage.EngineReq\x1a\x19.todoPackage.WaitingTimes\"\x00\x62\x06proto3')



_ENGINEREQ = DESCRIPTOR.message_types_by_name['EngineReq']
_WAITINGTIMES = DESCRIPTOR.message_types_by_name['WaitingTimes']
EngineReq = _reflection.GeneratedProtocolMessageType('EngineReq', (_message.Message,), {
  'DESCRIPTOR' : _ENGINEREQ,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todoPackage.EngineReq)
  })
_sym_db.RegisterMessage(EngineReq)

WaitingTimes = _reflection.GeneratedProtocolMessageType('WaitingTimes', (_message.Message,), {
  'DESCRIPTOR' : _WAITINGTIMES,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todoPackage.WaitingTimes)
  })
_sym_db.RegisterMessage(WaitingTimes)

_TODO = DESCRIPTOR.services_by_name['Todo']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ENGINEREQ._serialized_start=27
  _ENGINEREQ._serialized_end=38
  _WAITINGTIMES._serialized_start=40
  _WAITINGTIMES._serialized_end=81
  _TODO._serialized_start=83
  _TODO._serialized_end=165
# @@protoc_insertion_point(module_scope)
