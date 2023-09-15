import maya.cmds as cmds
import os
import json
from GSMain.Config import Config
from Settings import AssetTypes


class BaseScene(object):

    def __init__(self):

        if cmds.file(q=1, sn=1):
            if cmds.file(q=1, sn=1).split("/")[-2]=="work" and cmds.file(q=1, sn=1).split("/")[-3] in  cmds.file(q=1, sn=1, shn=1):
                self.asset_full_path = cmds.file(q=1, sn=1).split("work/" + cmds.file(q=1, sn=1, shn=1))[0]
            elif cmds.file(q=1, sn=1).split("/")[-2] in cmds.file(q=1, sn=1, shn=1):
                self.asset_full_path = cmds.file(q=1, sn=1).split("work/" + cmds.file(q=1, sn=1, shn=1))[0]
            else:
                raise ValueError("Asset structure not corrected(asset main folder name not corected).")

        else:
            raise ValueError("Maya file not saved.")
        if os.path.isfile(os.path.join(self.asset_full_path, "AssetConfig.gsconfig")):
            with open(os.path.join(self.asset_full_path, "AssetConfig.gsconfig"), "r") as asset_config_file:
                self.asset_config = json.load(asset_config_file)
        else:
            raise ValueError("Asset config not found.")

        asset_type_config = AssetTypes.get_all_types()
        self.scene_type = self.asset_config["assettype"]
        self.asset_name = self.asset_config["assetname"]
        self.asset_local_path = asset_type_config[self.scene_type]["path"] + self.asset_name

    def get_asset_root_name(self):
        if self.get_root_or_work() == "root":
            return cmds.file(q=1, sn=1, shn=1).replace(".ma", "").replace(".mb", "")
        if self.get_root_or_work() == "work":
            if "_v" in cmds.file(q=1, sn=1, shn=1):
                return cmds.file(q=1, sn=1, shn=1).split("_v")[0]
            else:
                return cmds.file(q=1, sn=1, shn=1).split(".")[0]

    def open_asset(self, file_path):
        cmds.file(file_path, o=True)

    def work_incremental_save(self, path=None):
        if not path:
            path = cmds.file(q=True, sceneName=True)
        if not len(cmds.file(q=1, sn=1).split("/")) > 2 and cmds.file(q=1, sn=1).split("/")[-2] == "work":
            short_name = cmds.file(q=True, sceneName=True, shortName=True)
            work_path = path.replace(short_name, "") + "work/"
            work_scene_path = work_path + short_name
            path = work_scene_path

        scene_path = path
        path, file = os.path.split(scene_path)
        file = file.split('.')
        file_name = file[0].split('_0')
        version = 1
        if len(file_name) > 1:
            version = int(file_name[-1]) + 1
        name = os.path.join(path, '{}.{}.{}'.format(file_name[0], str(version).rjust(4, '0'), file[-1]))
        while os.path.exists(name):
            version += 1
            name = os.path.join(path, '{}.{}.{}'.format(file_name[0], str(version).rjust(4, '0'), file[-1]))
        name = os.path.join(path, '{}.{}.{}'.format(file_name[0], str(version).rjust(4, '0'), file[-1]))
        cmds.file(rename=name)
        cmds.file(save=True)
        return name

    def work_save(self, path=None):
        if not path:
            path = cmds.file(q=True, sceneName=True)
        if not "work/" in path:
            short_name = cmds.file(q=True, sceneName=True, shortName=True)
            work_path = path.replace(short_name, "") + "work/"
            work_scene_path = work_path + short_name
            path = work_scene_path

        scene_path = path
        path, file = os.path.split(scene_path)
        file = file.split('.')
        file_name = file[0].split('_0')
        version = 1
        if len(file_name) > 1:
            version = int(file_name[-1])
        name = os.path.join(path, '{}.{}.{}'.format(file_name[0], str(version).rjust(4, '0'), file[-1]))
        while os.path.exists(name):
            version += 1
            name = os.path.join(path, '{}.{}.{}'.format(file_name[0], str(version).rjust(4, '0'), file[-1]))
        name = os.path.join(path, '{}.{}.{}'.format(file_name[0], str(version).rjust(4, '0'), file[-1]))
        cmds.file(rename=name)
        cmds.file(save=True)
        return name

    def final_save(self):
        self.work_incremental_save()
        if self.publish:
            self.publish()
        scene_path = cmds.file(q=True, sceneName=True)
        path, file = os.path.split(scene_path)
        file = file.split('.')
        file_name = file[0].split('_0')
        version = 1
        if len(file_name) > 1:
            version = int(file_name[-1]) + 1
        name = os.path.join(path, '{}.{}.{}'.format(file_name[0], str(version).rjust(4, '0'), file[-1]))
        while os.path.exists(name):
            version += 1
            name = os.path.join(path, '{}.{}.{}'.format(file_name[0], str(version).rjust(4, '0'), file[-1]))
        name = os.path.join(path, '{}.{}'.format(file_name[0], file[-1])).replace("/work", "")
        cmds.file(rename=name)
        cmds.file(save=True)

    def get_file_dir(self):
        return cmds.file(q=True, sceneName=True).split("/work")[0] + "/"

    def get_scene_type(self):
        return self.scene_type

    def get_asset_name(self):
        return self.asset_name

    def create_asset_config(self, asset_type, project_name):
        config = Config.Config()
        return config.create_asset_config(asset_name=self.get_asset_root_name(), asset_root_path=self.get_root_path(),
                                          asset_type=asset_type, project_name=project_name)

    def get_root_or_work(self):
        if len(cmds.file(q=1, sn=1).split("/")) > 2 and cmds.file(q=1, sn=1).split("/")[-2] == "work":
            return "work"
        else:
            return "root"

    def get_root_path(self):
        if len(cmds.file(q=1, sn=1).split("/")) > 2 and cmds.file(q=1, sn=1).split("/")[-2] == "work":
            return cmds.file(q=1, sn=1).replace("work/" + cmds.file(q=1, sn=1, shn=1), "")
        else:
            return cmds.file(q=1, sn=1).replace(cmds.file(q=1, sn=1, shn=1), "")

    def get_asset_root_name(self):
        if get_root_or_work() == "root":
            return cmds.file(q=1, sn=1, shn=1).replace(".ma", "").replace(".mb", "")
        if get_root_or_work() == "work":
            if "_v" in cmds.file(q=1, sn=1, shn=1):
                return cmds.file(q=1, sn=1, shn=1).split("_v")[0]
            else:
                return cmds.file(q=1, sn=1, shn=1).split(".")[0]

    def list_all_children(self, nodes):
        result = set()
        children = set(cmds.listRelatives(nodes) or [])

        return list(children)