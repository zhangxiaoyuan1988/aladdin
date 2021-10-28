# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/remote_fused_graph_execute_info.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.tensorflow.core.framework import graph_pb2 as tensorflow_dot_core_dot_framework_dot_graph__pb2
from protos.tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from protos.tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/framework/remote_fused_graph_execute_info.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=b'\n\030org.tensorflow.frameworkB RemoteFusedGraphExecuteInfoProtoP\001Zfgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/remote_fused_graph_execute_info_go_proto\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n?tensorflow/core/framework/remote_fused_graph_execute_info.proto\x12\ntensorflow\x1a%tensorflow/core/framework/graph.proto\x1a,tensorflow/core/framework/tensor_shape.proto\x1a%tensorflow/core/framework/types.proto\"\x82\x04\n\x1bRemoteFusedGraphExecuteInfo\x12*\n\x0cremote_graph\x18\x01 \x01(\x0b\x32\x14.tensorflow.GraphDef\x12\x1d\n\x15graph_input_node_name\x18\x02 \x03(\t\x12\x1e\n\x16graph_output_node_name\x18\x03 \x03(\t\x12\x15\n\rexecutor_name\x18\x04 \x01(\t\x12&\n\x1eserialized_executor_parameters\x18\x05 \x01(\x0c\x12\x66\n default_graph_input_tensor_shape\x18\x06 \x03(\x0b\x32<.tensorflow.RemoteFusedGraphExecuteInfo.TensorShapeTypeProto\x12g\n!default_graph_output_tensor_shape\x18\x07 \x03(\x0b\x32<.tensorflow.RemoteFusedGraphExecuteInfo.TensorShapeTypeProto\x1ah\n\x14TensorShapeTypeProto\x12#\n\x05\x64type\x18\x01 \x01(\x0e\x32\x14.tensorflow.DataType\x12+\n\x05shape\x18\x02 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProtoB\xa9\x01\n\x18org.tensorflow.frameworkB RemoteFusedGraphExecuteInfoProtoP\x01Zfgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/remote_fused_graph_execute_info_go_proto\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_graph__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_types__pb2.DESCRIPTOR,])




_REMOTEFUSEDGRAPHEXECUTEINFO_TENSORSHAPETYPEPROTO = _descriptor.Descriptor(
  name='TensorShapeTypeProto',
  full_name='tensorflow.RemoteFusedGraphExecuteInfo.TensorShapeTypeProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dtype', full_name='tensorflow.RemoteFusedGraphExecuteInfo.TensorShapeTypeProto.dtype', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shape', full_name='tensorflow.RemoteFusedGraphExecuteInfo.TensorShapeTypeProto.shape', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=614,
  serialized_end=718,
)

_REMOTEFUSEDGRAPHEXECUTEINFO = _descriptor.Descriptor(
  name='RemoteFusedGraphExecuteInfo',
  full_name='tensorflow.RemoteFusedGraphExecuteInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='remote_graph', full_name='tensorflow.RemoteFusedGraphExecuteInfo.remote_graph', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='graph_input_node_name', full_name='tensorflow.RemoteFusedGraphExecuteInfo.graph_input_node_name', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='graph_output_node_name', full_name='tensorflow.RemoteFusedGraphExecuteInfo.graph_output_node_name', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='executor_name', full_name='tensorflow.RemoteFusedGraphExecuteInfo.executor_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serialized_executor_parameters', full_name='tensorflow.RemoteFusedGraphExecuteInfo.serialized_executor_parameters', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_graph_input_tensor_shape', full_name='tensorflow.RemoteFusedGraphExecuteInfo.default_graph_input_tensor_shape', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_graph_output_tensor_shape', full_name='tensorflow.RemoteFusedGraphExecuteInfo.default_graph_output_tensor_shape', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_REMOTEFUSEDGRAPHEXECUTEINFO_TENSORSHAPETYPEPROTO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=718,
)

_REMOTEFUSEDGRAPHEXECUTEINFO_TENSORSHAPETYPEPROTO.fields_by_name['dtype'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_REMOTEFUSEDGRAPHEXECUTEINFO_TENSORSHAPETYPEPROTO.fields_by_name['shape'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_REMOTEFUSEDGRAPHEXECUTEINFO_TENSORSHAPETYPEPROTO.containing_type = _REMOTEFUSEDGRAPHEXECUTEINFO
_REMOTEFUSEDGRAPHEXECUTEINFO.fields_by_name['remote_graph'].message_type = tensorflow_dot_core_dot_framework_dot_graph__pb2._GRAPHDEF
_REMOTEFUSEDGRAPHEXECUTEINFO.fields_by_name['default_graph_input_tensor_shape'].message_type = _REMOTEFUSEDGRAPHEXECUTEINFO_TENSORSHAPETYPEPROTO
_REMOTEFUSEDGRAPHEXECUTEINFO.fields_by_name['default_graph_output_tensor_shape'].message_type = _REMOTEFUSEDGRAPHEXECUTEINFO_TENSORSHAPETYPEPROTO
DESCRIPTOR.message_types_by_name['RemoteFusedGraphExecuteInfo'] = _REMOTEFUSEDGRAPHEXECUTEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemoteFusedGraphExecuteInfo = _reflection.GeneratedProtocolMessageType('RemoteFusedGraphExecuteInfo', (_message.Message,), {

  'TensorShapeTypeProto' : _reflection.GeneratedProtocolMessageType('TensorShapeTypeProto', (_message.Message,), {
    'DESCRIPTOR' : _REMOTEFUSEDGRAPHEXECUTEINFO_TENSORSHAPETYPEPROTO,
    '__module__' : 'tensorflow.core.framework.remote_fused_graph_execute_info_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.RemoteFusedGraphExecuteInfo.TensorShapeTypeProto)
    })
  ,
  'DESCRIPTOR' : _REMOTEFUSEDGRAPHEXECUTEINFO,
  '__module__' : 'tensorflow.core.framework.remote_fused_graph_execute_info_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.RemoteFusedGraphExecuteInfo)
  })
_sym_db.RegisterMessage(RemoteFusedGraphExecuteInfo)
_sym_db.RegisterMessage(RemoteFusedGraphExecuteInfo.TensorShapeTypeProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
