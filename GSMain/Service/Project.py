import os
import json
from Settings.Configs import AssetTypes

class Project:
    def __init__(self, project_path=None):
        self.proj_ext = '.gsproj'
        self.proj_path = self.set_proj_path(project_path)
        self.proj_file = self.set_proj_file()
        self.proj_info = self.load_proj_info()
        self.proj.struct = {}
        self.opened_assets = {}
        self.init_proj_struct()

        self.project_hash = None
        self.project_name = None
        self.project_path = None

    def load_proj_info(self):
        with open(self.proj_path + self.proj_file, "r") as inf:
            info = json.load(inf)
        return info

    def set_proj_path(self, project_path):
        project_path = project_path.replace("\\", "/")

        if os.path.isdir(project_path):
            for elem in os.listdir(project_path):
                if os.path.isfile(os.path.join(project_path, elem)):
                    if os.path.splitext(os.path.join(project_path, elem))[1] == self.proj_ext:
                        if project_path[-1] != "/":
                            project_path += "/"
                        return project_path

    def set_proj_file(self):
        for elem in os.listdir(self.proj_path):
            if elem[-7:] == self.proj_ext:
                return elem
        return False

    def init_proj_struct(self):
        asset_types = AssetTypes.get_all_types()

    def upadte_proj_struct(self):
        pass

    def add_opened_asset(self):
        pass

    def set_project_hash(self, hash_str):
        self.project_hash = hash_str
        return True

    def get_project_hash(self):
        return self.project_hash

    def set_project_name(self, name):
        self.project_name = name
        return True