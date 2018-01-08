# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from . import api_pb2 as api__pb2


class DgraphStub(object):
  """Graph response.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Query = channel.unary_unary(
        '/api.Dgraph/Query',
        request_serializer=api__pb2.Request.SerializeToString,
        response_deserializer=api__pb2.Response.FromString,
        )
    self.Mutate = channel.unary_unary(
        '/api.Dgraph/Mutate',
        request_serializer=api__pb2.Mutation.SerializeToString,
        response_deserializer=api__pb2.Assigned.FromString,
        )
    self.Alter = channel.unary_unary(
        '/api.Dgraph/Alter',
        request_serializer=api__pb2.Operation.SerializeToString,
        response_deserializer=api__pb2.Payload.FromString,
        )
    self.CommitOrAbort = channel.unary_unary(
        '/api.Dgraph/CommitOrAbort',
        request_serializer=api__pb2.TxnContext.SerializeToString,
        response_deserializer=api__pb2.TxnContext.FromString,
        )
    self.CheckVersion = channel.unary_unary(
        '/api.Dgraph/CheckVersion',
        request_serializer=api__pb2.Check.SerializeToString,
        response_deserializer=api__pb2.Version.FromString,
        )


class DgraphServicer(object):
  """Graph response.
  """

  def Query(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Mutate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Alter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CommitOrAbort(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckVersion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DgraphServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Query': grpc.unary_unary_rpc_method_handler(
          servicer.Query,
          request_deserializer=api__pb2.Request.FromString,
          response_serializer=api__pb2.Response.SerializeToString,
      ),
      'Mutate': grpc.unary_unary_rpc_method_handler(
          servicer.Mutate,
          request_deserializer=api__pb2.Mutation.FromString,
          response_serializer=api__pb2.Assigned.SerializeToString,
      ),
      'Alter': grpc.unary_unary_rpc_method_handler(
          servicer.Alter,
          request_deserializer=api__pb2.Operation.FromString,
          response_serializer=api__pb2.Payload.SerializeToString,
      ),
      'CommitOrAbort': grpc.unary_unary_rpc_method_handler(
          servicer.CommitOrAbort,
          request_deserializer=api__pb2.TxnContext.FromString,
          response_serializer=api__pb2.TxnContext.SerializeToString,
      ),
      'CheckVersion': grpc.unary_unary_rpc_method_handler(
          servicer.CheckVersion,
          request_deserializer=api__pb2.Check.FromString,
          response_serializer=api__pb2.Version.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.Dgraph', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))