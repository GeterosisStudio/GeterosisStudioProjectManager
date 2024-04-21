from Editor.GUI.Windows.Project.ProjectWindow import ProjectWindow
import sys

import grpc
import Project_pb2
import Project_pb2_grpc


class ProjectWindowService(Project_pb2_grpc.ProjectServicer):
    def __init__(self):
        self.service = None

    def load(self):
        from PySide6.QtWidgets import QApplication
        app = QApplication()
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = Project_pb2_grpc.ProjectStub(channel)
            path_obj = stub.get_project_path(Project_pb2.single_string())
            self.service = ProjectWindow(path_obj.alpha_path)
        self.service.show()
        sys.exit(app.exec())


if __name__ == "__main__":
    s = ProjectWindowService()
    s.load()
    # from PySide6.QtWidgets import QApplication
    # app = QApplication()
    # window = ProjectWindowGRPC("D:/Projects/PRojects.gsproj")
    # window.service.show()
    # sys.exit(app.exec())
