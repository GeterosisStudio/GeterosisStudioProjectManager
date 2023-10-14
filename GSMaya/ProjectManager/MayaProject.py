import os
import json
import maya.cmds as cmds
from Settings.Configs import AssetTypes


class MayaProject():
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
        self.scene_name = self.asset_config["assetname"]
        self.asset_local_path = asset_type_config[self.scene_type]["path"] + self.scene_name
        self.__project_name = self.get_project_name()
        self.__project_path = self.get_project_path()

    def get_project_name(self):
        project_root_path = cmds.file(q=1, sn=1).split(self.asset_local_path)[0]
        if os.path.isfile(project_root_path + project_root_path.split("/")[-1] + ".gsproj"):
            return project_root_path.split("/")[-1]



    def get_project_path(self):
        project_root_path = cmds.file(q=1, sn=1).split(self.asset_local_path)[0]
        if os.path.isfile(project_root_path + project_root_path.split("/")[-1] + ".gsproj"):
            return project_root_path
