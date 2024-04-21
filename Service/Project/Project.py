import os
import sys
import json
import copy
from Service.Project.BaseAsset import BaseAsset
from Service.Project.BaseAssetItem import BaseAssetItem
from Service.Network import Server, Client
from Settings import Settings
import importlib
import threading


class Project:
    def __init__(self, project_path=None):
        self._proj_ext = '.gsproj'
        self._proj_path_lock = threading.RLock()
        self._proj_path = ""
        self._proj_file = ""
        self._proj_info = ""
        self.__asset_dict_lock = threading.RLock()
        self._asset_dict = {}
        self.__item_dict_lock = threading.RLock()
        self._item_dict = {}
        self.__project_data_lock = threading.RLock()
        self._project_data = {}
        self.__opened_assets_lock = threading.RLock()
        self._opened_assets = {}

        self.project_hash = None
        self.project_name = None
        self.server = Server.Server()
        self.client = Client.Client()

        if project_path:
            self.init_proj(project_path)

    def init_proj(self, project_path):
        self.set_proj_path(project_path)
        self.set_proj_file()
        self._load_proj_info()
        self.add_proj_plugin_path()
        self.load_settings()

    def set_proj_path(self, project_path):
        project_path = project_path.replace("\\", "/")

        if os.path.isdir(project_path):
            for elem in os.listdir(project_path):
                if os.path.isfile(os.path.join(project_path, elem)):
                    if os.path.splitext(os.path.join(project_path, elem))[1] == self._proj_ext:
                        if project_path[-1] != "/":
                            project_path += "/"
                        self._proj_path = project_path
                        return project_path

    def set_proj_file(self):
        for elem in os.listdir(self._proj_path):
            if elem[-7:] == self._proj_ext:
                self._proj_file = elem
                return elem
        return False

    def get_project_file(self):
        return self._proj_file

    def _load_proj_info(self):
        with open(self._proj_path + self._proj_file, "r") as inf:
            info = json.load(inf)
        self._proj_info = info
        self.project_name = self._proj_info["name"]
        return info

    def add_proj_plugin_path(self):
        if not self._proj_path + "_plugins" in sys.path:
            sys.path.append(self._proj_path + "_plugins/")

    def load_settings(self):
        settings_path = self._proj_path + "settings/"

        default_asset_path = Settings.get_default_assets_path()
        default_item_path = Settings.get_default_items_path()

        project_asset_path = settings_path + "Assets/"
        project_item_path = settings_path + "Items/"

        # TODO: refact .json to .gsassettmplate
        default_assets = [i for i in os.listdir(default_asset_path) if '.json' in i]
        default_items = [i for i in os.listdir(Settings.get_default_items_path()) if '.json' in i]
        project_assets = [i for i in os.listdir(project_asset_path) if '.json' in i]
        project_items = [i for i in os.listdir(project_item_path) if '.json' in i]
        plugin_assets = []
        prigin_items = []

        # Load items.
        for i in default_items:
            self.load_item_tmplate("default", default_item_path + i)

        for i in project_items:
            self.load_item_tmplate("project", project_item_path + i)

        # Load assets.
        for i in default_assets:
            self.load_asset_tmplate("default", default_asset_path + i)

        for i in project_assets:
            self.load_asset_tmplate("project", project_asset_path + i)



        #TODO: refact .json to .gsassettype
        with open(settings_path + "FileSystem.json", "r") as file_system:
            file_system = json.load(file_system)
            self.__project_data_lock.acquire()
            self._project_data = file_system
            self.__project_data_lock.release()

        self.__project_data_lock.acquire()
        self.load_proj_data(self._project_data)
        self.__project_data_lock.release()

    def load_asset_tmplate(self, location, asset_tmplate_file):
        #print("Load: {}".format(asset_tmplate_file))
        with open(asset_tmplate_file, "r") as data:
            non_initialize_tmplate = json.load(data)
        #print(json.dumps(non_initialize_tmplate, indent=4))
        if not non_initialize_tmplate["assetclass"] in globals():
            print(non_initialize_tmplate["assetclass"] + " not defined")
            return False
        tmplate = self.init_asset_tmplate(non_initialize_tmplate)

        #Create non_initialize_tmplate object with non_initialize_tmplate and without non_initialize_tmplate path.
        asset_object = globals().get(tmplate["assetclass"])(tmplate)
        if BaseAsset == asset_object or isinstance(asset_object, BaseAsset):
            self.__asset_dict_lock.acquire()
            if location not in self._asset_dict:
                self._asset_dict[location] = {}
            self._asset_dict[location][tmplate["assettype"]] = asset_object
            #print(asset_object)
            self.__asset_dict_lock.release()
        else:
            print("Asset class "+ tmplate["assetclass"] + " not instance from BaseAsset class")

    def init_asset_tmplate(self, tmplate):
        items = tmplate["items"]
        for key in items:
            for i in key:
                # Add item
                items[key][i]["itemobject"] = self._item_dict[items[key][i]['itempath']][items[key][i]["name"]]
        return tmplate

    def load_item_tmplate(self, location, item_file):
        #print("Load: {}".format(item_file))
        with open(item_file, "r") as data:
            item_tmplate = json.load(data)
        if not item_tmplate["itemclass"] in globals():
            print(item_tmplate["itemclass"] + " not defined.")
            return False

        item_object = globals().get(item_tmplate["itemclass"])(item_tmplate)

        if BaseAssetItem == item_object or isinstance(item_object, BaseAssetItem):
            self.__item_dict_lock.acquire()
            if location not in self._asset_dict:
                self._asset_dict[location] = {}

            if not location in self._item_dict:
                self._item_dict[location] = {}
            if not item_tmplate["itemname"] in self._item_dict[location]:
                self._item_dict[location][item_tmplate["itemname"]] = {}
            self._item_dict[location][item_tmplate["itemname"]] = item_object
            self.__item_dict_lock.release()
        else:
            print("Item class "+ item_tmplate["itemname"] + " not instance from BaseAssetItem class")

    def load_proj_data(self, struct):
        """
        :param folder_data: {
        "item name": {
        "name": "local",
        "localpath": "local/path",
        "folders": {
          "path": {
            "name": "asset name",
            "localpath": "local/path/",
            "folders": null,
            "asset": {
              "assettype": "asset",
              "assettmplatepath": "project",
              "foldercount": 0
            }
        "asset": {
          "assettype": "AssetName",
          "assettmplatepath": "project",
          "foldercount": 0
        }
        """

        for item in struct:
            #print(struct[item]["localpath"])
            if struct[item]["folders"]:
                self.load_proj_data(struct[item]["folders"])
            if not struct[item]["asset"]:
                return True
            self.__asset_dict_lock.acquire()
            if not struct[item]["asset"]['assettype'] in self._asset_dict[struct[item]["asset"]["assettmplatepath"]]:
                print("___ASSET NOT FOUND___: " + struct[item]["asset"]['assettype'])
                return False
            # Add asset class and asset tmplate to prolect structure.
            struct[item]["asset"]["assetclass"] = \
                self._asset_dict[struct[item]["asset"]["assettmplatepath"]][struct[item]["asset"]["assettype"]]
            self.__asset_dict_lock.release()


            """
            DO CREATE DATA FROM ASSETS AND SUBFOLDERS
            """
            data = None
            struct[item]["asset"]["data"] = data

            if struct[item]['asset']['foldercount'] > 0:
                struct[item]['asset']['data'] = {}
                self.load_subfolders_data(struct[item])

    def load_subfolders_data(self, data):
        if not data['asset']['foldercount'] > 0:
            return None
        path = self._proj_path + data["localpath"]
        listdir = [fname for fname in os.listdir(path) if os.path.isdir("/".join([path, fname]))]
        for i in listdir:
            if not i in data:
                data['asset']["data"][i] = {}
            data['asset']["data"][i]["name"] = i
            data['asset']["data"][i]["localpath"] = data["localpath"] + i + "/"
            data['asset']["data"][i]["folders"] = {}
            data['asset']["data"][i]["assetsobjects"] = {}
            if data['asset']['foldercount'] > 1:
                data['asset']["data"][i]["folders"] = self.load_subfolders(data['asset']["data"][i]["folders"],
                                                                           data["localpath"] + i + "/",
                                                                           data['asset']['foldercount'] - 1, 1)

    def load_subfolders(self, data = {}, local_path ="", depth = 0, level = 0):
        """
        Recursive load pathes for assets
        :param data:
        :param local_path:
        :param depth:
        :return:
        """
        count = depth - 1
        path = self._proj_path + local_path
        listdir = [fname for fname in os.listdir(path) if os.path.isdir("/".join([path, fname]))]
        for i in listdir:
            #print(level * "\t" + i)
            if i not in data:
                data[i] = {}
            data[i]["name"] = i
            data[i]["localpath"] = local_path + i + "/"
            data[i]["folders"] = {}
            if count <= 0:
                data[i]["assetsobjects"] = {}
            if count > 0:
                data[i]["folders"] = self.load_subfolders(data[i]["folders"], local_path + i + "/", count, level + 1)
        return data

    def create_assets_in_folder(self, local_folder):
        for i in os.listdir(self._proj_path + local_folder):
            self.create_asset_object(local_folder + i)

    def create_asset_object(self, local_path):
        asset_tmplate = self.get_asset_tmplate_obj_from_path(local_path)
        asset_obj = copy.deepcopy(asset_tmplate)
        asset_obj.load_asset_data(self._proj_path + local_path)
        data = self.search_in_project_data("assetdata", local_path, self._project_data)
        asset_name = asset_obj.get_asset_name()
        if not asset_name in data:
            data[asset_name] = {"classobject": asset_obj, "localpath": local_path}
            #print(f"Createt {asset_name} object from path {local_path}")
            return asset_obj
        else:
            #print(f"Exist {asset_name} object from path {local_path}")
            return data[asset_name]["classobject"]

    def clear_global_path(self, global_path):
        global_path_len = len(self._proj_path)
        if global_path[0:global_path_len] == global_path:
            return global_path[global_path_len:]


    def get_asset_tmplate_obj_from_path(self, local_path):
        self.__project_data_lock.acquire()

        asset_template = self.search_in_project_data(type="tmplate", local_path = local_path, parent = self._project_data)
        self.__project_data_lock.release()
        return asset_template

    def search_in_project_data(self, type="", local_path="", parent={}, is_asset=False):
        if not type:
            type = "assetdata"
        if not parent:
            parent = self._project_data

        if not local_path and not isinstance(local_path, str):
            print(f"Path not corrected: {local_path}.")
            return False

        for item in parent:
            local_p = parent[item]["localpath"]
            str_len = len(parent[item]["localpath"])
            if not is_asset and not parent[item]['localpath'] == local_path[0:str_len]:
                continue
            if not is_asset and not 'asset' in parent[item]:
                return self.search_in_project_data(type, local_path, parent[item]["folders"])
            if not is_asset and 'asset' in parent[item] and not parent[item]['asset']:
                return self.search_in_project_data(type, local_path, parent[item]["folders"])
            elif type == "tmplate":
                if 'asset' in parent[item] and parent[item]['asset']:
                    qwe = parent[item]['asset']["assetclass"]
                    return parent[item]['asset']["assetclass"]
                else:
                    return self.search_in_project_data(type, local_path, parent[item]["folders"])

            elif type == "assetdata":
                if not is_asset:
                    if not parent[item]['asset']:
                        return self.search_in_project_data(type, local_path, parent[item]["folders"])
                    elif parent[item]['asset']:
                        return self.search_in_project_data(type, local_path, parent[item]['asset']["data"], is_asset=True)
                else:
                    if parent[item]['folders']:
                        return self.search_in_project_data(type, local_path, parent[item]['folders'], is_asset=True)
                    elif 'assetsobjects' in parent[item]:
                        return parent[item]['assetsobjects']

            raise print("NOT FOUND")

    def get_asset_from_path(self, local_path):
        project_path = self.get_project_path()
        project_path_len = len(project_path)
        if local_path[0:project_path_len] == project_path:
            local_path = local_path[project_path_len:]

        data = self.search_in_project_data(local_path = local_path)
        if not os.path.isdir(project_path + local_path):
            print(f"Path not corrected: {project_path + local_path}")
            print(f"Asset not found: {project_path + local_path}")
            return False
        for asset in data:
            if data[asset]['localpath'] == local_path:
                return data[asset]['classobject']
        print(f"Asset not found: {project_path + local_path}")
        return False

    def get_project_struct(self):
        return self._project_data

    def get_project_path(self):
        self._proj_path_lock.acquire()
        project_path = self._proj_path
        self._proj_path_lock.release()
        return project_path



if __name__ == "__main__":
    project = Project()
    project.init_proj("D:/Projects/")
    project.get_project_struct()
    project.create_asset_object("animation/scenes/e0010/e0010s0000d0000v0000/")
    project.create_assets_in_folder("animation/scenes/e0010/")
    asset = project.get_asset_from_path("D:/Projects/animation/scenes/e0010/e0010s0000d0000v0000/")
    print(asset.get_project_path())
    print(asset.get_asset_path())
    item = asset.get_asset_item(0, 0)
    print(item.get_project_path())

