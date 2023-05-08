import maya.cmds as cmds
import os
import json
from GSMain import Log


class MayaAsset(object):

    def __init__(self):
        self.asset_full_path = self.get_file_dir()
        if os.path.isfile(os.path.join(self.asset_full_path, "AssetConfig.gsconfig")):
            with open(os.path.join(self.asset_full_path, "AssetConfig.gsconfig")) as asset_config_file:
                self.asset_config = json.load(asset_config_file)
        else:
            raise Log.warning("Scene incorrect: AssetConfig.gsconfig not defined.")

        self.asset_type = self.asset_config["assettype"]

        with open('../Settings/AssetTypes.gsconfig') as asset_type_config_file:
            asset_type_config = json.load(asset_type_config_file)
            if self.asset_type in asset_type_config:
                self.asset_local_path = asset_type_config[self.asset_type]["path"]
            else:
                raise Log.warning("Asset type {} not defined.".format(self.asset_type))
        self.project_path = self.asset_full_path.split(self.asset_local_path)[0]
        self.asset_name = self.asset_config["assetname"]

    def open_asset(self):
        cmds.file("", o=True)

    def work_incremental_save(self, path=None):
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
        return cmds.file(q=True, sceneName=True).split("/work")[0] + "/"

    def get_asset_type(self):
        return self.asset_type

    def get_asset_name(self):
        return self.asset_name
