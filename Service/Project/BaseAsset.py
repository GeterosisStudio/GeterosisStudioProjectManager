import subprocess
import json
import os
from Service.Project import BaseAssetItem

class BaseAsset:
    def __init__(self, tmplate=None, data = None):

        self.__ext = ".gsasset"
        self.__asset_name = ""
        self.__asset_label = ""
        self.__asset_path = ""
        self.__asset_file = ""
        self.__asset_data = ""
        self.__asset_item_tree = {}
        self.__project_path = ""

        if tmplate:
            self.load_asset_tmplate(tmplate)
        if data:
            self.load_asset_data(data)

    def load_asset_tmplate(self, tmplate):
        if isinstance(tmplate, str) and os.path.isfile(tmplate):
            self.__load_tmplate_file(tmplate)
            return True
        elif isinstance(tmplate, dict):
            self.__init_asset_tmplate(tmplate)
            return True
        return False


    def __load_tmplate_file(self, file_path):
        if not os.path.isfile(file_path):
            print("Кeceived string not found as file.")
            return False
        try:
            with open(file_path, "r") as tmplate:
                self.__init_asset_tmplate(json.load(tmplate))
        except Exception as e:
            print(f"ERROR: {e}")

    def __init_asset_tmplate(self, data):
        if not isinstance(data, dict):
            print("Data is not dict")
            return False
        self.__asset_item_tree = data["items"]

    def load_asset_item_tmplate(self, item_name):
        class_name = item_name
        class_obj = globals().get(class_name)
        asset = class_obj()
        print(asset.__class__.__name__)

    def open_asset_folder(self):
        subprocess.Popen(f'explorer "{self.__project_path + self.__asset_path}"')

    def _set_asset_path(self, path):
        value_path = ""
        if path[0:len(self.__project_path)] == self.__project_path:
            value_path = path[len(self.__project_path):-1]
        else:
            value_path = path

        if value_path[-1] == "\\":
            value_path[-2:-1] = "/"
        if value_path[-1] != "/":
            value_path = value_path + "/"
        self.__asset_path = value_path
        return self.__asset_path



    def get_asset_path(self):
        return self.__asset_path

    def _set_asset_name(self, name):
        self.__asset_name = name
    def get_asset_name(self):
        return self.__asset_name

    def _set_asset_label(self, label):
        if not label or isinstance(label, str):
            self.__asset_label = self.get_asset_name()
            return self.get_asset_label()
        self.__asset_label = label
        return self.get_asset_label()

    def get_asset_label(self):
        return self.__asset_label

    def load_asset_data(self, asset_path):
        is_dir = False
        is_file = False

        if not os.path.isdir(asset_path) or os.path.isfile(asset_path):
            print(f"Asset directory not corrected: {asset_path}")
            return False
        if os.path.isdir(asset_path):
            is_dir = True
        elif os.path.isfile(asset_path):
            is_file = True
        else:
            print(f"Asset directory not corrected: {asset_path}")
            return False

        if "\\" in asset_path:
            asset_path = asset_path.replace("\\", "/")
        if asset_path[-8:] != self.__ext and asset_path [-1] != "/":
            asset_path += "/"

        if is_dir:
            dir = asset_path
            assets = [elem for elem in os.listdir(asset_path) if elem[-8:] == self.__ext]
            if len(assets) > 1:
                folder_asset = asset_path.split("/")[-2] + self.__ext
                if folder_asset in assets:
                    file_name = folder_asset
                file_name = assets[0]
            if len(assets) == 1:
                file_name = assets[0]
            if not assets:
                print(f"Asset file not found in folder: {asset_path}")
                return False

        if is_file:
            file_name = asset_path.split("/")[-1]
            dir = asset_path - file_name
        try:
            with open(dir + file_name, "r") as asset_info:
                asset_data = json.load(asset_info)
                self._set_asset_data(asset_data)
                self._set_asset_file(dir + file_name)
                self._set_asset_name(asset_data['assetname'])
                self._set_asset_label(asset_data['assetlabel'])
                self.__project_path = self._set_project_path(asset_data['projectpath'])
                self._set_asset_path(dir)
                return dir + file_name
        except Exception as e:
            print(e)

    def _set_project_path(self, path):
        self.__project_path = path
        return self.__project_path

    def get_project_path(self):
        return self.__project_path
    def _set_asset_data(self, data):
        self.__asset_data = data

    def get_asset_data(self):
        return self.__asset_data

    def _set_asset_file(self, file_path):
        self.asse_file = file_path

    def get_asset_item_tree(self):
        return self.__asset_item_tree

    def get_asset_item(self, x, y):
        if str(x) in self.__asset_item_tree:
            if str(y) in self.__asset_item_tree[str(x)]:
                if "itemobject" in self.__asset_item_tree[str(x)][str(y)]:
                    return self.__asset_item_tree[str(x)][str(y)]["itemobject"]
        print(f"Item not found by index: {x}, {y} .")



if __name__ == "__main__":
    asset = BaseAsset()
    asset.load_asset_tmplate("D:/Projects/settings/Assets/GSAnimationScene.json")
    asset.load_asset_data("D:/Projects/animation/scenes/e0010/e0010s0000d0000v0000")
    # print(asset.get_project_path())
    # print(asset.get_asset_name())
    # print(asset.get_asset_data())
    print(asset.get_asset_path())
    print(asset.get_asset_item_tree())
    # print(asset.get_asset_item(0, 0))