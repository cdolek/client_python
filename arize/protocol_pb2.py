# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocol.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protocol.proto',
  package='protocol',
  syntax='proto3',
  serialized_options=b'Z/github.com/Arize-ai/arize/pkg/receiver/protocol',
  serialized_pb=b'\n\x0eprotocol.proto\x12\x08protocol\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xaa\x01\n\x06Record\x12\x12\n\naccount_id\x18\x01 \x01(\x03\x12\x10\n\x08model_id\x18\x02 \x01(\t\x12\x15\n\rprediction_id\x18\x03 \x01(\t\x12*\n\nprediction\x18\x04 \x01(\x0b\x32\x14.protocol.PredictionH\x00\x12 \n\x05truth\x18\x05 \x01(\x0b\x32\x0f.protocol.TruthH\x00\x42\x15\n\x13prediction_or_truth\"i\n\x05Value\x12\x16\n\x0c\x62inary_value\x18\x01 \x01(\x08H\x00\x12\x1b\n\x11\x63\x61tegorical_value\x18\x02 \x01(\tH\x00\x12\x17\n\rnumeric_value\x18\x03 \x01(\x01H\x00\x42\x12\n\x10\x63lassifier_value\"\xc7\x01\n\nPrediction\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x10prediction_value\x18\x02 \x01(\x0b\x32\x0f.protocol.Value\x12\x30\n\x06labels\x18\x03 \x03(\x0b\x32 .protocol.Prediction.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\\\n\x05Truth\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12$\n\x0btruth_value\x18\x02 \x01(\x0b\x32\x0f.protocol.Value\"\x10\n\x0eReceiverResult\"\x0f\n\rHealthRequest\"\x10\n\x0eHealthResponse2\xa5\x01\n\x08Receiver\x12\x45\n\x03Log\x12\x10.protocol.Record\x1a\x18.protocol.ReceiverResult\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/v1/log:\x01*\x12R\n\tGetHealth\x12\x17.protocol.HealthRequest\x1a\x18.protocol.HealthResponse\"\x12\x82\xd3\xe4\x93\x02\x0c\x12\n/v1/healthB1Z/github.com/Arize-ai/arize/pkg/receiver/protocolb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='protocol.Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='protocol.Record.account_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_id', full_name='protocol.Record.model_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prediction_id', full_name='protocol.Record.prediction_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prediction', full_name='protocol.Record.prediction', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='truth', full_name='protocol.Record.truth', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='prediction_or_truth', full_name='protocol.Record.prediction_or_truth',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=92,
  serialized_end=262,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='protocol.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binary_value', full_name='protocol.Value.binary_value', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='categorical_value', full_name='protocol.Value.categorical_value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numeric_value', full_name='protocol.Value.numeric_value', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
    _descriptor.OneofDescriptor(
      name='classifier_value', full_name='protocol.Value.classifier_value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=264,
  serialized_end=369,
)


_PREDICTION_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='protocol.Prediction.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protocol.Prediction.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='protocol.Prediction.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=526,
  serialized_end=571,
)

_PREDICTION = _descriptor.Descriptor(
  name='Prediction',
  full_name='protocol.Prediction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='protocol.Prediction.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prediction_value', full_name='protocol.Prediction.prediction_value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='protocol.Prediction.labels', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTION_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=571,
)


_TRUTH = _descriptor.Descriptor(
  name='Truth',
  full_name='protocol.Truth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='protocol.Truth.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='truth_value', full_name='protocol.Truth.truth_value', index=1,
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
  serialized_start=573,
  serialized_end=665,
)


_RECEIVERRESULT = _descriptor.Descriptor(
  name='ReceiverResult',
  full_name='protocol.ReceiverResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=667,
  serialized_end=683,
)


_HEALTHREQUEST = _descriptor.Descriptor(
  name='HealthRequest',
  full_name='protocol.HealthRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=685,
  serialized_end=700,
)


_HEALTHRESPONSE = _descriptor.Descriptor(
  name='HealthResponse',
  full_name='protocol.HealthResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=702,
  serialized_end=718,
)

_RECORD.fields_by_name['prediction'].message_type = _PREDICTION
_RECORD.fields_by_name['truth'].message_type = _TRUTH
_RECORD.oneofs_by_name['prediction_or_truth'].fields.append(
  _RECORD.fields_by_name['prediction'])
_RECORD.fields_by_name['prediction'].containing_oneof = _RECORD.oneofs_by_name['prediction_or_truth']
_RECORD.oneofs_by_name['prediction_or_truth'].fields.append(
  _RECORD.fields_by_name['truth'])
_RECORD.fields_by_name['truth'].containing_oneof = _RECORD.oneofs_by_name['prediction_or_truth']
_VALUE.oneofs_by_name['classifier_value'].fields.append(
  _VALUE.fields_by_name['binary_value'])
_VALUE.fields_by_name['binary_value'].containing_oneof = _VALUE.oneofs_by_name['classifier_value']
_VALUE.oneofs_by_name['classifier_value'].fields.append(
  _VALUE.fields_by_name['categorical_value'])
_VALUE.fields_by_name['categorical_value'].containing_oneof = _VALUE.oneofs_by_name['classifier_value']
_VALUE.oneofs_by_name['classifier_value'].fields.append(
  _VALUE.fields_by_name['numeric_value'])
_VALUE.fields_by_name['numeric_value'].containing_oneof = _VALUE.oneofs_by_name['classifier_value']
_PREDICTION_LABELSENTRY.containing_type = _PREDICTION
_PREDICTION.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PREDICTION.fields_by_name['prediction_value'].message_type = _VALUE
_PREDICTION.fields_by_name['labels'].message_type = _PREDICTION_LABELSENTRY
_TRUTH.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRUTH.fields_by_name['truth_value'].message_type = _VALUE
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['Prediction'] = _PREDICTION
DESCRIPTOR.message_types_by_name['Truth'] = _TRUTH
DESCRIPTOR.message_types_by_name['ReceiverResult'] = _RECEIVERRESULT
DESCRIPTOR.message_types_by_name['HealthRequest'] = _HEALTHREQUEST
DESCRIPTOR.message_types_by_name['HealthResponse'] = _HEALTHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), {
  'DESCRIPTOR' : _RECORD,
  '__module__' : 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Record)
  })
_sym_db.RegisterMessage(Record)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Value)
  })
_sym_db.RegisterMessage(Value)

Prediction = _reflection.GeneratedProtocolMessageType('Prediction', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTION_LABELSENTRY,
    '__module__' : 'protocol_pb2'
    # @@protoc_insertion_point(class_scope:protocol.Prediction.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _PREDICTION,
  '__module__' : 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Prediction)
  })
_sym_db.RegisterMessage(Prediction)
_sym_db.RegisterMessage(Prediction.LabelsEntry)

Truth = _reflection.GeneratedProtocolMessageType('Truth', (_message.Message,), {
  'DESCRIPTOR' : _TRUTH,
  '__module__' : 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Truth)
  })
_sym_db.RegisterMessage(Truth)

ReceiverResult = _reflection.GeneratedProtocolMessageType('ReceiverResult', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVERRESULT,
  '__module__' : 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ReceiverResult)
  })
_sym_db.RegisterMessage(ReceiverResult)

HealthRequest = _reflection.GeneratedProtocolMessageType('HealthRequest', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHREQUEST,
  '__module__' : 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.HealthRequest)
  })
_sym_db.RegisterMessage(HealthRequest)

HealthResponse = _reflection.GeneratedProtocolMessageType('HealthResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHRESPONSE,
  '__module__' : 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.HealthResponse)
  })
_sym_db.RegisterMessage(HealthResponse)


DESCRIPTOR._options = None
_PREDICTION_LABELSENTRY._options = None

_RECEIVER = _descriptor.ServiceDescriptor(
  name='Receiver',
  full_name='protocol.Receiver',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=721,
  serialized_end=886,
  methods=[
  _descriptor.MethodDescriptor(
    name='Log',
    full_name='protocol.Receiver.Log',
    index=0,
    containing_service=None,
    input_type=_RECORD,
    output_type=_RECEIVERRESULT,
    serialized_options=b'\202\323\344\223\002\014\"\007/v1/log:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='GetHealth',
    full_name='protocol.Receiver.GetHealth',
    index=1,
    containing_service=None,
    input_type=_HEALTHREQUEST,
    output_type=_HEALTHRESPONSE,
    serialized_options=b'\202\323\344\223\002\014\022\n/v1/health',
  ),
])
_sym_db.RegisterServiceDescriptor(_RECEIVER)

DESCRIPTOR.services_by_name['Receiver'] = _RECEIVER

# @@protoc_insertion_point(module_scope)