# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import todo_pb2 as todo__pb2


class TodoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.requestWaitingTimes = channel.unary_unary(
                '/todoPackage.Todo/requestWaitingTimes',
                request_serializer=todo__pb2.EngineReq.SerializeToString,
                response_deserializer=todo__pb2.WaitingTimes.FromString,
                )


class TodoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def requestWaitingTimes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TodoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'requestWaitingTimes': grpc.unary_unary_rpc_method_handler(
                    servicer.requestWaitingTimes,
                    request_deserializer=todo__pb2.EngineReq.FromString,
                    response_serializer=todo__pb2.WaitingTimes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'todoPackage.Todo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Todo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def requestWaitingTimes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todoPackage.Todo/requestWaitingTimes',
            todo__pb2.EngineReq.SerializeToString,
            todo__pb2.WaitingTimes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
