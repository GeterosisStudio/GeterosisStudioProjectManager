"""Exprot blockout levels maya to unreal and sets"""

import maya.cmds as cmds
import time

levels_grp = "levels_grp"
root_grp = "root"
project_path = None
blockout_dir = "{}assets/Sets/Maps/Maya/Blockout/".format(project_path)
export_dir = "{}assets/Sets/Maps/Export/MayaExport/".format(project_path)


def create_export_levels():
    default_zero_position_x = 1008000
    default_zero_position_y = 655200
    counter = 50400
    levels_arr = {}
    new_levels = []
    objs = cmds.ls("props", ap=True, dag=True, tr=True)
    del objs[0]
    if cmds.objExists(levels_grp):
        cmds.delete(levels_grp)
    for obj in range(len(objs)):
        obj_x = cmds.xform("{}.vtx[*]".format(objs[obj]), q=1, rp=True, ws=True)[0]
        obj_y = cmds.xform("{}.vtx[*]".format(objs[obj]), q=1, rp=True, ws=True)[2]

        x_count = int((obj_x + default_zero_position_x) / counter)
        y_count = int((obj_y + default_zero_position_y) / counter)
        Level = "Level_x{}_y{}".format(x_count, y_count)

        if not Level in levels_arr:
            levels_arr[Level] = []
            levels_arr[Level].append(objs[obj])
        else:
            levels_arr[Level].append(objs[obj])

    for key in levels_arr.keys():
        duplicated = cmds.duplicate(levels_arr[key])
        cmds.parent(duplicated, w=True)
        if len(duplicated) > 1:
            cmds.polyUnite(duplicated, name=key, ch=1, mergeUVSets=1)
        else:
            cmds.rename(duplicated, key)
        cmds.delete(key, ch=True)
        if not cmds.objExists(levels_grp):
            grp = cmds.group(key)
            cmds.rename(grp, levels_grp)
        else:
            cmds.parent(key, levels_grp)
        new_levels.append(key)
        print("CREATED:{}".format(key))
    return new_levels


def export_maya_levels():
    if not cmds.objExists(levels_grp):
        print("LEVELS_GRP NOT DEFINED")
        return False
    objs = cmds.ls("levels_grp", ap=True, dag=True, tr=True)
    del objs[0]
    for obj in range(len(objs)):
        if not cmds.objExists(root_grp):
            grp = cmds.group(objs[obj])
            cmds.rename(grp, root_grp)
        cmds.parent(root_grp, w=True)
        cmds.select(root_grp)
        file_dir = "{}/{}.ma".format(blockout_dir, objs[obj])
        cmds.file(file_dir, force=True, options="v=0", typ="mayaAscii", pr=True, es=True)
        print("EXPORTED: {} of {} --> {}.ma".format(obj + 1, len(objs), objs[obj]))
        cmds.delete(root_grp)
    cmds.delete(levels_grp)


def export_fbx_levels():
    if not cmds.objExists(levels_grp):
        print("LEVELS_GRP NOT DEFINED")
        return False
    objs = cmds.ls("levels_grp", ap=True, dag=True, tr=True)
    del objs[0]
    for obj in range(len(objs)):
        cmds.parent(objs[obj], w=True)
        cmds.select(objs[obj])
        file_dir = "{}/{}.fbx".format(export_dir, objs[obj])
        cmds.file(file_dir, force=True, options="v=0", typ="FBX export", pr=True, es=True)
        print("EXPORTED: {} of {} --> {}.fbx".format(obj + 1, len(objs), objs[obj]))
        cmds.delete(objs[obj])
    cmds.delete(levels_grp)


create_export_levels()
export_maya_levels()
time.sleep(0.5)
create_export_levels()
export_fbx_levels()




