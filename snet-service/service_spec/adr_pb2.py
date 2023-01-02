# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: adr.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='adr.proto',
  package='adr',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tadr.proto\x12\x03\x61\x64r\"\x1f\n\x07IntPair\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\t\n\x01\x62\x18\x02 \x01(\x05\"\x16\n\tSingleInt\x12\t\n\x01v\x18\x01 \x01(\x05\"\x18\n\x0bInputString\x12\t\n\x01s\x18\x01 \x01(\t\"1\n\x0e\x41\x44RReturnFloat\x12\t\n\x01\x61\x18\x01 \x01(\x02\x12\t\n\x01\x64\x18\x02 \x01(\x02\x12\t\n\x01r\x18\x03 \x01(\x02\x32\x43\n\x11ServiceDefinition\x12.\n\x03\x61\x64r\x12\x10.adr.InputString\x1a\x13.adr.ADRReturnFloat\"\x00\x62\x06proto3')
)




_INTPAIR = _descriptor.Descriptor(
  name='IntPair',
  full_name='adr.IntPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='adr.IntPair.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='adr.IntPair.b', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=18,
  serialized_end=49,
)


_SINGLEINT = _descriptor.Descriptor(
  name='SingleInt',
  full_name='adr.SingleInt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='v', full_name='adr.SingleInt.v', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=51,
  serialized_end=73,
)


_INPUTSTRING = _descriptor.Descriptor(
  name='InputString',
  full_name='adr.InputString',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s', full_name='adr.InputString.s', index=0,
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
  serialized_start=75,
  serialized_end=99,
)


_ADRRETURNFLOAT = _descriptor.Descriptor(
  name='ADRReturnFloat',
  full_name='adr.ADRReturnFloat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='adr.ADRReturnFloat.a', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='d', full_name='adr.ADRReturnFloat.d', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='r', full_name='adr.ADRReturnFloat.r', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=101,
  serialized_end=150,
)

DESCRIPTOR.message_types_by_name['IntPair'] = _INTPAIR
DESCRIPTOR.message_types_by_name['SingleInt'] = _SINGLEINT
DESCRIPTOR.message_types_by_name['InputString'] = _INPUTSTRING
DESCRIPTOR.message_types_by_name['ADRReturnFloat'] = _ADRRETURNFLOAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IntPair = _reflection.GeneratedProtocolMessageType('IntPair', (_message.Message,), dict(
  DESCRIPTOR = _INTPAIR,
  __module__ = 'adr_pb2'
  # @@protoc_insertion_point(class_scope:adr.IntPair)
  ))
_sym_db.RegisterMessage(IntPair)

SingleInt = _reflection.GeneratedProtocolMessageType('SingleInt', (_message.Message,), dict(
  DESCRIPTOR = _SINGLEINT,
  __module__ = 'adr_pb2'
  # @@protoc_insertion_point(class_scope:adr.SingleInt)
  ))
_sym_db.RegisterMessage(SingleInt)

InputString = _reflection.GeneratedProtocolMessageType('InputString', (_message.Message,), dict(
  DESCRIPTOR = _INPUTSTRING,
  __module__ = 'adr_pb2'
  # @@protoc_insertion_point(class_scope:adr.InputString)
  ))
_sym_db.RegisterMessage(InputString)

ADRReturnFloat = _reflection.GeneratedProtocolMessageType('ADRReturnFloat', (_message.Message,), dict(
  DESCRIPTOR = _ADRRETURNFLOAT,
  __module__ = 'adr_pb2'
  # @@protoc_insertion_point(class_scope:adr.ADRReturnFloat)
  ))
_sym_db.RegisterMessage(ADRReturnFloat)



_SERVICEDEFINITION = _descriptor.ServiceDescriptor(
  name='ServiceDefinition',
  full_name='adr.ServiceDefinition',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=152,
  serialized_end=219,
  methods=[
  _descriptor.MethodDescriptor(
    name='adr',
    full_name='adr.ServiceDefinition.adr',
    index=0,
    containing_service=None,
    input_type=_INPUTSTRING,
    output_type=_ADRRETURNFLOAT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICEDEFINITION)

DESCRIPTOR.services_by_name['ServiceDefinition'] = _SERVICEDEFINITION

# @@protoc_insertion_point(module_scope)