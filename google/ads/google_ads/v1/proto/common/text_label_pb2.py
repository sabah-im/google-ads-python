# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/common/text_label.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/common/text_label.proto',
  package='google.ads.googleads.v1.common',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v1.commonB\016TextLabelProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V1.Common\312\002\036Google\\Ads\\GoogleAds\\V1\\Common\352\002\"Google::Ads::GoogleAds::V1::Common'),
  serialized_pb=_b('\n5google/ads/googleads_v1/proto/common/text_label.proto\x12\x1egoogle.ads.googleads.v1.common\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"v\n\tTextLabel\x12\x36\n\x10\x62\x61\x63kground_color\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\xe9\x01\n\"com.google.ads.googleads.v1.commonB\x0eTextLabelProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V1.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V1\\Common\xea\x02\"Google::Ads::GoogleAds::V1::Commonb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_TEXTLABEL = _descriptor.Descriptor(
  name='TextLabel',
  full_name='google.ads.googleads.v1.common.TextLabel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='background_color', full_name='google.ads.googleads.v1.common.TextLabel.background_color', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.ads.googleads.v1.common.TextLabel.description', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=269,
)

_TEXTLABEL.fields_by_name['background_color'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_TEXTLABEL.fields_by_name['description'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['TextLabel'] = _TEXTLABEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TextLabel = _reflection.GeneratedProtocolMessageType('TextLabel', (_message.Message,), dict(
  DESCRIPTOR = _TEXTLABEL,
  __module__ = 'google.ads.googleads_v1.proto.common.text_label_pb2'
  ,
  __doc__ = """A type of label displaying text on a colored background.
  
  
  Attributes:
      background_color:
          Background color of the label in RGB format. This string must
          match the regular expression
          '^#([a-fA-F0-9]{6}\|[a-fA-F0-9]{3})$'. Note: The background
          color may not be visible for manager accounts.
      description:
          A short description of the label. The length must be no more
          than 200 characters.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.TextLabel)
  ))
_sym_db.RegisterMessage(TextLabel)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
