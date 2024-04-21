import os
import json
import subprocess


class BaseAssetItem:
    def __init__(self, tmplate=None, data=None):
        self.__project_path = ""

        self.__asset_path = ""
        self.asset_name = ""
        self.__item_path = ""
        self.__prefix = []
        self.__postfix = []
        self.__ext = ""
        self.__versions_path = ""
        self.__versions = []
        self.__variations = []
        self.__version_regular = ""
        self.__root_asset_file = ""
        self.__is_start_regular = ""
        self.__is_complete_regular = ""

        if tmplate:
            self.load_item_tmplate(tmplate)
        if data:
            self.load_item_data(data)

    def load_item_tmplate(self, tmplate):
        if isinstance(tmplate, str) and os.path.isfile(tmplate):
            with open(tmplate) as config:
                tmplate = json.load(config)
        elif not isinstance(tmplate, dict):
            return False

        self.__ext = tmplate["data"]["itemfileext"]

        if tmplate["data"]["versions"] == True:
            self.__versions_path = tmplate["data"]["versions_path"]
            self.__version_regular = tmplate["data"]["versionregular"]

    def load_item_data(self, data):
        if not isinstance(data, dict):
            print("Value not is dict.")
            return False


    def get_abs_item_path(self):
        return self.__project_path + self.__asset_path + self.__item_path

    def set_project_path(self, path):
        if not isinstance(path, str) and os.path.isdir(path):
            return False
        self.__project_path = path

    def get_project_path(self):
        return self.__project_path

    def open_item(self, last_version=None, custom_version=None):
        if last_version and self.__versions:
            subprocess.run(['open', self.get_abs_item_path() + self.__versions_path + self.__versions[-1]], check=True)
            return self.get_abs_item_path() + self.__versions_path + self.__versions[-1]
        elif custom_version and self.__versions:
            if custom_version in self.__versions:
                subprocess.run(['open', self.get_abs_item_path() + self.__versions_path + custom_version], check=True)
                return self.get_abs_item_path() + self.__versions_path + custom_version
            else:
                return False

        subprocess.run(['open', self.get_abs_item_path() + self.__root_asset_file], check=True)
        return self.get_abs_item_path() + self.__root_asset_file

if __name__ == "__main__":
    item = BaseAssetItem("D:/Projects/settings/Items/GSMontage.json",\
                         "D:/Projects/animation/scenes/e0010/e0010s0000d0000v0000/")
    print(item.get_project_path())
