from Settings import Settings
import json

class ProjectBrowser:
    def __init__(self):
        self.projects = Settings.load_projects()

    def get_project_dict(self):
        return self.projects

    def set_open_project(self, project, value):
        self.projects[project]["opened"] = value
        return 1



if __name__ == "__main__":
    from Client import Client

    config = Settings.get_config()
    ProjBrowser = ProjectBrowser()
    client = Client()
    client.set_client_host(config["Project browser"]["host"])
    client.set_client_port(config["Project browser"]["port"])
    while True:
        if client.check_port(1):
            break
        print("Сервер не доступен...")
    client.start_client()


