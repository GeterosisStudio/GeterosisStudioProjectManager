"""import Proxy levels and Blockout in maya and parent this roots in group "sets"."""

import os
import maya.cmds as cmds


def import_landscale(project_path):
    file_input_dir = "{}assets/Sets/Maps/Maya/Landscapes/".format(project_path)
    filenames = next(os.walk(file_input_dir), (None, None, []))[2]
    sets_grp = "sets"
    if not cmds.objExists("sets"):
        cmds.Group()
        cmds.rename("null1", sets_grp)
    for i in range(len(filenames)):
        if "_P" in filenames[i]:
            file_path = file_input_dir + filenames[i]
            cmds.file(file_path, r=True)
            root_grp_ref = cmds.file(file_path, q=True, namespace=True) + "_root"
            cmds.parent(root_grp_ref, sets_grp)


def import_blockout(project_path):
    file_input_dir = "{}assets/Sets/Maps/Maya/Blockout/".format(project_path)
    filenames = next(os.walk(file_input_dir), (None, None, []))[2]
    sets_grp = "sets"
    if not cmds.objExists("sets"):
        cmds.Group()
        cmds.rename("null1", sets_grp)
    for i in range(len(filenames)):
        if "Proxy" in filenames[i]:
            file_path = file_input_dir + filenames[i]
            cmds.file(file_path, r=True)
            root_grp_ref = cmds.file(file_path, q=True, namespace=True) + "_root"
            cmds.parent(root_grp_ref, sets_grp)
