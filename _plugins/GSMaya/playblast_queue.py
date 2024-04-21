import sys
import maya.cmds as cmds
import time

temp = "D:/temp.txt"

import pymel.core as pm
sys.path.append("/GeterosisProjectManager/_plugins/GSMaya")
import zurbrigg_playblast

reload(zurbrigg_playblast)

path = "D:/project/"
play_bl = "D:/project"
import os

filenames = next(os.walk(path), (None, None, []))[2]


def get_cam():
    cam = ""

    if cmds.objExists("cameras_grp"):
        cam = cmds.listRelatives("cameras_grp", children=1)[0]
    else:
        for sn in cmds.ls(type="camera"):
            if "sc" in sn:
                cam = cmds.listRelatives(sn, parent=True)[0]
            elif "ep" in sn:
                cam = cmds.listRelatives(sn, parent=True)[0]
            elif "cam" in sn:
                cam = cmds.listRelatives(sn, parent=True)[0]
    if cam == "":
        cam = "persp"
    return cam



def create_blast(scene):
    scene_name = scene.replace(".ma", "")
    pm.setFocus("modelPanel4")
    cam = get_cam()
    if cam:
        cmds.lookThru(cam)
    blast = zurbrigg_playblast.ZurbriggPlayblastUi()
    blast.force_overwrite_cb.setChecked(True)
    blast.viewer_cb.setChecked(False)
    blast.output_dir_path_le.setText(play_bl)
    blast.output_filename_le.setText(scene_name)
    blast.resolution_select_cmb.setCurrentIndex(4)
    blast.resolution_width_sb.setValue(2048)
    blast.resolution_height_sb.setValue(858)
    blast.show()
    blast.show_settings_dialog()
    blast._settings_dialog.set_ffmpeg_path("ffmpeg/bin/ffmpeg.exe")
    blast._settings_dialog.accept()
    blast.do_playblast()
    blast.close()



for i in filenames:
    if not "_anim.m" in i:
        continue
    if i.replace(".ma", ".mp4") in os.listdir(play_bl) or i[0] == "@":
        continue
    print(i)
    with open(temp, "a") as f:
        f.write(i + "\n")
    try:
        try:
            cmds.file(path + i, o=1, force=True, options="v=0;", prompt=False)
        except Exception as e:
            print("____EEEERROR____", i, e)
        create_blast(i)

    except Exception as e:
        print("____EEEERROR____", i, e)
        try:
            create_blast(i)
        except Exception as e:
            print("____BLAST ERROR____", i, e)
        time.sleep(5)