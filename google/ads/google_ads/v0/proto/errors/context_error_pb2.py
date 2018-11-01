# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/context_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/errors/context_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_pb=_b('\n8google/ads/googleads_v0/proto/errors/context_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"\x9c\x01\n\x10\x43ontextErrorEnum\"\x87\x01\n\x0c\x43ontextError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\'\n#OPERATION_NOT_PERMITTED_FOR_CONTEXT\x10\x02\x12\x30\n,OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE\x10\x03\x42\xc7\x01\n\"com.google.ads.googleads.v0.errorsB\x11\x43ontextErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errorsb\x06proto3')
)



_CONTEXTERRORENUM_CONTEXTERROR = _descriptor.EnumDescriptor(
  name='ContextError',
  full_name='google.ads.googleads.v0.errors.ContextErrorEnum.ContextError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_NOT_PERMITTED_FOR_CONTEXT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=114,
  serialized_end=249,
)
_sym_db.RegisterEnumDescriptor(_CONTEXTERRORENUM_CONTEXTERROR)


_CONTEXTERRORENUM = _descriptor.Descriptor(
  name='ContextErrorEnum',
  full_name='google.ads.googleads.v0.errors.ContextErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONTEXTERRORENUM_CONTEXTERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=249,
)

_CONTEXTERRORENUM_CONTEXTERROR.containing_type = _CONTEXTERRORENUM
DESCRIPTOR.message_types_by_name['ContextErrorEnum'] = _CONTEXTERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContextErrorEnum = _reflection.GeneratedProtocolMessageType('ContextErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _CONTEXTERRORENUM,
  __module__ = 'google.ads.googleads_v0.proto.errors.context_error_pb2'
  ,
  __doc__ = """Container for enum describing possible context errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.ContextErrorEnum)
  ))
_sym_db.RegisterMessage(ContextErrorEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.errorsB\021ContextErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors'))
# @@protoc_insertion_point(module_scope)