import maya.cmds as cmds
import os
import json
from GSMain.Config import Config

class MayaAsset(object):

    def __init__(self, project_path, asset_type, asset_name):

        with open('../Settings/AssetTypes.gsconfig') as asset_type_config_file:
            asset_type_config = json.load(asset_type_config_file)
            if asset_type in asset_type_config:
                self.asset_local_path = asset_type_config[asset_type]["path"]
            else:
                raise ("Asset type {} not defined.".format(asset_type))
        self.project_path = project_path
        self.asset_type = asset_type
        self.asset_name = asset_name
        self.asset_full_path = os.path.join(self.project_path, self.asset_local_path, self.asset_name)
        if os.path.isfile(os.path.join(self.asset_full_path, self.asset_name + "_Config.gsconfig")):
            with open(os.path.join(self.asset_full_path, self.asset_name + "_Config.gsconfig")) as asset_config_file:
                self.asset_config = json.load(asset_config_file)
        else:
            self.create_asset_config()
            with open(os.path.join(self.asset_full_path, self.asset_name + "_Config.gsconfig")) as asset_config_file:
                self.asset_config = json.load(asset_config_file)

    def get_asset_root_name(self):
        if get_root_or_work() == "root":
            return cmds.file(q=1, sn=1, shn=1).replace(".ma", "").replace(".mb", "")
        if get_root_or_work() == "work":
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
        return cmds.file(q=True, sceneName=True).replace("/work", "")

    def export_config(self):
        pass

    def get_asset_type(self):
        pass

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