# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Project_pb2 as Project__pb2


class ProjectStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_project_path = channel.unary_unary(
                '/Project/get_project_path',
                request_serializer=Project__pb2.empty.SerializeToString,
                response_deserializer=Project__pb2.super_path.FromString,
                )


class ProjectServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_project_path(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_project_path': grpc.unary_unary_rpc_method_handler(
                    servicer.get_project_path,
                    request_deserializer=Project__pb2.empty.FromString,
                    response_serializer=Project__pb2.super_path.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Project', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Project(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_project_path(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Project/get_project_path',
            Project__pb2.empty.SerializeToString,
            Project__pb2.super_path.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)