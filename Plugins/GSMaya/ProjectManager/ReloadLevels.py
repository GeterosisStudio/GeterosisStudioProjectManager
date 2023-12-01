"""reload proxy and originals levels in maya after reduse in blender"""

import os
import maya.cmds as cmds
import time

# cmds.file(f = True, new = True)
project_path = None
file_input_blender_dir = "{}assets/Sets/Maps/Export/BlenderExport/".format(project_path)
file_input_unreal_dir = "{}assets/Sets/Maps/Export/UnrealExport/".format(project_path)
filenames_in_blender = next(os.walk(file_input_blender_dir), (None, None, []))[2]
filenames_in_unreal = next(os.walk(file_input_unreal_dir), (None, None, []))[2]
file_output_dir = "{}assets/Sets/Maps/Maya/Landscapes/".format(project_path)
default_zero_position_x = -1008000
default_zero_position_y = -655200


def reimport_level_proxy():
    for i in range(len(filenames_in_blender)):
        if not -1 < i <= 100000000:
            continue
        x_count = int(filenames_in_blender[i].replace("Level_x", "").partition('_y')[0])
        y_count = int(filenames_in_blender[i].split("_y")[1].replace(".FBX", ""))

        file_name = filenames_in_blender[i].replace(".FBX", "")
        new_level_file = file_output_dir + file_name + "_P" + ".mb"
        cmds.file(file_input_blender_dir + filenames_in_blender[i], i=True)
        cmds.group("LandscapeStreamingProxy_0")
        cmds.rename("group1", "root")

        # set position
        x_attr = default_zero_position_x + (x_count * 50400)
        z_attr = default_zero_position_y + (y_count * 50400)
        cmds.setAttr("LandscapeStreamingProxy_0.translateX", x_attr)
        cmds.setAttr("LandscapeStreamingProxy_0.translateZ", z_attr)

        # correct_normal
        cmds.polyMergeVertex("LandscapeStreamingProxy_0", d=0.3795, am=1, ch=1)
        cmds.polySetToFaceNormal("LandscapeStreamingProxy_0")
        cmds.DeleteHistory("LandscapeStreamingProxy_0")

        try:
            cmds.delete("WorldSettings", "LevelBounds_0")
        except:
            pass
        try:
            cmds.delete("WorldSettings", "LevelBounds_0")
        except:
            pass

        print("LEVEL CREATED:", file_name + "_P" + ".mb", "-->", new_level_file)
        print(i+1, "of", len(filenames_in_blender))
        time.sleep(0.2)
        cmds.file(rename=new_level_file)
        cmds.file(s=True)
        cmds.file(f=True, new=True)


def reimport_level_originals():
    for i in range(len(filenames_in_unreal)):
        if not -1 < i <= 100000000:
            continue
        x_count = int(filenames_in_unreal[i].replace("Level_x", "").partition('_y')[0])
        y_count = int(filenames_in_unreal[i].split("_y")[1].replace(".FBX", ""))

        file_name = filenames_in_unreal[i].replace(".FBX", "")
        new_level_file = file_output_dir + file_name + ".mb"
        cmds.file(file_input_unreal_dir + filenames_in_unreal[i], i=True)
        cmds.group("LandscapeStreamingProxy_0")
        cmds.rename("group1", "root")
        # set position
        x_attr = default_zero_position_x + (x_count * 50400)
        z_attr = default_zero_position_y + (y_count * 50400)
        cmds.setAttr("LandscapeStreamingProxy_0.translateX", x_attr)
        cmds.setAttr("LandscapeStreamingProxy_0.translateZ", z_attr)

        try:
            cmds.delete("WorldSettings", "LevelBounds_0")
        except:
            pass
        try:
            cmds.delete("WorldSettings", "LevelBounds_0")
        except:
            pass
        print("LEVEL CREATED:", file_name + ".mb", "-->", new_level_file)
        print(i+1, "of", len(filenames_in_unreal))
        time.sleep(0.2)
        cmds.file(rename=new_level_file)
        cmds.file(s=True)
        cmds.file(f=True, new=True)


reimport_level_proxy()
reimport_level_originals()
