from Service.Project.Project import Project
import grpc
import Project_pb2
import Project_pb2_grpc
from concurrent import futures
import logging

class ProjectService(Project_pb2_grpc.ProjectServicer):
    def __init__(self, project_path=None):
        self.service = Project()
        if project_path:
            self.service.init_proj(project_path)

    def get_project_path(self, request, context):
        full_path = self.service.get_project_path() + self.service.get_project_file()
        print("eee" + full_path)
        return Project_pb2.single_string(single_string=full_path)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Project_pb2_grpc.add_ProjectServicer_to_server(ProjectService("D:/Projects"), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()
    # server.stop(None)


if __name__ == "__main__":
    # project = ProjectGRPC()
    # project.service.init_proj("D:/Projects/")
    # project.service.get_project_struct()
    # project.service.create_asset_object("animation/scenes/e0010/e0010s0000d0000v0000/")
    # #project.service.create_assets_in_folder("animation/scenes/e0010/")
    # asset = project.service.get_asset_from_path("D:/Projects/animation/scenes/e0010/e0010s0000d0000v0000/")
    # print(asset.get_project_path())
    # print(asset.get_asset_path())
    # item = asset.get_asset_item(0, 0)
    # print(item.get_project_path())



    logging.basicConfig()
    serve()