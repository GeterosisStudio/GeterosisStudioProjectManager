from Settings import Settings
from Service.Network import Server, Client
import json


class ProjectBrowser:
    def __init__(self):
        self.projects = Settings.load_projects()
        self.client = Client.Client()
        self.server = Server.Server()



    def add_project(self, project_path):
        pass

    def create_project(self, project):
        pass

    def get_project_dict(self):
        return self.projects

    def set_open_project(self, project, value):
        self.projects[project]["opened"] = value
        return 1

    def open_project(self, project):

        self.projects[project]["opened"] = True

    def close_project(self, project):

        self.projects[project]["opened"] = False

    def reload_projects(self):
        pass



if __name__ == "__main__":
    ProjBrowser = ProjectBrowser()
