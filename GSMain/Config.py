import os
import json
import hashlib
import getpass
import Settings.Enviroment

class Config:

    def __init__(self):
        this_path = os.path.join(os.path.abspath(__file__).replace("\\", "/").rsplit("/", 1)[0])
        with open(this_path.replace("/GSMain", "") + '/Settings/Config.json') as f:
            self.core_config = json.load(f)

        self.__custom_settings = self.core_config["settings"]["custom settings"]
        if not self.__custom_settings:
            self.user_name = getpass.getuser()
            self.__settings_path = 'C:/Users/{}/Documents/{}'.format(self.user_name, "GeterosisProjectManager/")
        else:
            self.__settings_path = __file__.replace("GSMain/Config.py", "default/")
        with open(self.__settings_path + "Settings/Config.json") as f:
            self.__user_config = json.load(f)
        with open(self.__settings_path + "Settings/Projects.json") as f:
            self.__projects_config = json.load(f)
        self.__settings_path = self.__settings_path.replace("\\", "/")



    def get_config_path(self):
        return self.__settings_path + "Settings/"

    def get_projects_config(self):
        return self.__projects_config

    def __add_project_config(self, name, value):
        if isinstance(value, dict):
            self.__projects_config[name] = value
            return True
        else:
            return False

    def __save_projects_config(self):
        with open(self.__settings_path + "Settings/Projects.json", 'w') as f:
            json.dump(self.__projects_config, f, indent=4)
            return True

    def get_user_config(self):
        return self.__user_config

    def save_user_config(self, key, value):
        with open('../Settings/Config.json') as f:
            self.__user_config[key] = value
            json.dump(self.core_config, f)

    def create_settings_path(self):
        dir_struct = {"Settings": ["Config.json", "Libraries.json", "Projects.json"], "Projects": {}, "logs": {}}
        if not os.path.exists(self.__settings_path):
            os.mkdir(self.__settings_path)
        self.__make_dir_struct(dir_struct, self.__settings_path)

    def __make_dir_struct(self, folder_structure, parent_path):

        for folder_name, contents in folder_structure.items():
            folder_path = os.path.join(parent_path, folder_name)
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            if isinstance(contents, dict):
                self.__make_dir_struct(contents, folder_path)
            elif contents:
                if isinstance(contents, list):
                    for elem in contents:
                        if isinstance(elem, dict):
                            self.__make_dir_struct(elem, folder_path)
                        else:
                            if not os.path.isfile(os.path.join(folder_path, elem)):
                                open(os.path.join(folder_path, elem), "w").close()
                else:
                    if not os.path.isfile(os.path.join(folder_path, contents)):
                        open(os.path.join(folder_path, contents), "w").close()

    def add_project(self, name, path):
        project_path = lambda p: p + "/" + name + "/" if not p.endswith("/") and not p.endswith(
            "\\") else p + name + "/"

        project = {"name": name, "path": project_path(path)}

        hash = hashlib.sha256(json.dumps(project, sort_keys=True).encode('utf-8')).hexdigest()
        if not hash in self.get_projects_config():
            self.__add_project_config(hash, project)
            self.__save_projects_config()
            return True
        else:
            return False

    def get_projects_by_name(self, name):
        returned = {}
        for proj in self.__projects_config:
            if self.__projects_config[proj]['name'] == name:
                print(self.__projects_config[proj]['name'])
                returned[proj] = self.__projects_config[proj]
        return returned

    def create_asset_config(self, **options):
        """

        :param options:
            asset_name:
            asset_root_path:
            asset_type:
            project_name:

        :return:
        """
        asset_name = options.get("asset_name")
        asset_root_path = options.get("asset_root_path")
        asset_type = options.get("asset_type")
        project_name = options.get("project_name")

        config = {"asset_name": asset_name,
                  "asset_type": asset_type,
                  "project_name": project_name
                  }

        config_full_path = asset_root_path + asset_name + ".gsconfig"
        with open(config_full_path, 'w') as f:
            json.dump(config, f, indent=4)
        return config_full_path

    def get_asset_config(self, asset_path):
        if os.path.isfile(asset_path):
            with open(asset_path) as f:
                return json.load(f)
        elif os.path.exists(asset_path):
            for config in os.listdir(asset_path):
                if ".gsconfig" in config:
                    with open(config) as f:
                        return json.load(f)
        return False

if __name__ == "__main__":
    test = Config()
    print(test.get_config_path())
