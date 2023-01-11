# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service_spec/adr.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service_spec/adr.proto',
  package='adr',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16service_spec/adr.proto\x12\x03\x61\x64r\"!\n\x0eStringResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\"\n\x0c\x46ileResponse\x12\x12\n\nchunk_data\x18\x01 \x01(\x0c\"/\n\x08MetaData\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x11\n\textension\x18\x02 \x01(\t\"W\n\x11UploadFileRequest\x12!\n\x08metadata\x18\x01 \x01(\x0b\x32\r.adr.MetaDataH\x00\x12\x14\n\nchunk_data\x18\x02 \x01(\x0cH\x00\x42\t\n\x07request2\x81\x01\n\x11ServiceDefinition\x12\x34\n\x0c\x44ownloadFile\x12\r.adr.MetaData\x1a\x11.adr.FileResponse\"\x00\x30\x01\x12\x36\n\x03\x41\x44R\x12\x16.adr.UploadFileRequest\x1a\x13.adr.StringResponse\"\x00(\x01\x62\x06proto3')
)




_STRINGRESPONSE = _descriptor.Descriptor(
  name='StringResponse',
  full_name='adr.StringResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='adr.StringResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=31,
  serialized_end=64,
)


_FILERESPONSE = _descriptor.Descriptor(
  name='FileResponse',
  full_name='adr.FileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk_data', full_name='adr.FileResponse.chunk_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=66,
  serialized_end=100,
)


_METADATA = _descriptor.Descriptor(
  name='MetaData',
  full_name='adr.MetaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='adr.MetaData.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension', full_name='adr.MetaData.extension', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=102,
  serialized_end=149,
)


_UPLOADFILEREQUEST = _descriptor.Descriptor(
  name='UploadFileRequest',
  full_name='adr.UploadFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='adr.UploadFileRequest.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk_data', full_name='adr.UploadFileRequest.chunk_data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
    _descriptor.OneofDescriptor(
      name='request', full_name='adr.UploadFileRequest.request',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=151,
  serialized_end=238,
)

_UPLOADFILEREQUEST.fields_by_name['metadata'].message_type = _METADATA
_UPLOADFILEREQUEST.oneofs_by_name['request'].fields.append(
  _UPLOADFILEREQUEST.fields_by_name['metadata'])
_UPLOADFILEREQUEST.fields_by_name['metadata'].containing_oneof = _UPLOADFILEREQUEST.oneofs_by_name['request']
_UPLOADFILEREQUEST.oneofs_by_name['request'].fields.append(
  _UPLOADFILEREQUEST.fields_by_name['chunk_data'])
_UPLOADFILEREQUEST.fields_by_name['chunk_data'].containing_oneof = _UPLOADFILEREQUEST.oneofs_by_name['request']
DESCRIPTOR.message_types_by_name['StringResponse'] = _STRINGRESPONSE
DESCRIPTOR.message_types_by_name['FileResponse'] = _FILERESPONSE
DESCRIPTOR.message_types_by_name['MetaData'] = _METADATA
DESCRIPTOR.message_types_by_name['UploadFileRequest'] = _UPLOADFILEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StringResponse = _reflection.GeneratedProtocolMessageType('StringResponse', (_message.Message,), dict(
  DESCRIPTOR = _STRINGRESPONSE,
  __module__ = 'service_spec.adr_pb2'
  # @@protoc_insertion_point(class_scope:adr.StringResponse)
  ))
_sym_db.RegisterMessage(StringResponse)

FileResponse = _reflection.GeneratedProtocolMessageType('FileResponse', (_message.Message,), dict(
  DESCRIPTOR = _FILERESPONSE,
  __module__ = 'service_spec.adr_pb2'
  # @@protoc_insertion_point(class_scope:adr.FileResponse)
  ))
_sym_db.RegisterMessage(FileResponse)

MetaData = _reflection.GeneratedProtocolMessageType('MetaData', (_message.Message,), dict(
  DESCRIPTOR = _METADATA,
  __module__ = 'service_spec.adr_pb2'
  # @@protoc_insertion_point(class_scope:adr.MetaData)
  ))
_sym_db.RegisterMessage(MetaData)

UploadFileRequest = _reflection.GeneratedProtocolMessageType('UploadFileRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADFILEREQUEST,
  __module__ = 'service_spec.adr_pb2'
  # @@protoc_insertion_point(class_scope:adr.UploadFileRequest)
  ))
_sym_db.RegisterMessage(UploadFileRequest)



_SERVICEDEFINITION = _descriptor.ServiceDescriptor(
  name='ServiceDefinition',
  full_name='adr.ServiceDefinition',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=241,
  serialized_end=370,
  methods=[
  _descriptor.MethodDescriptor(
    name='DownloadFile',
    full_name='adr.ServiceDefinition.DownloadFile',
    index=0,
    containing_service=None,
    input_type=_METADATA,
    output_type=_FILERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ADR',
    full_name='adr.ServiceDefinition.ADR',
    index=1,
    containing_service=None,
    input_type=_UPLOADFILEREQUEST,
    output_type=_STRINGRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICEDEFINITION)

DESCRIPTOR.services_by_name['ServiceDefinition'] = _SERVICEDEFINITION

# @@protoc_insertion_point(module_scope)
