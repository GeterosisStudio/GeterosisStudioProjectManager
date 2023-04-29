"""Correct chars rig"""

import maya.cmds as cmds
import os
project_path = None
filenames = next(os.walk("assets/Chars/1Defult/MH/rig/".format(project_path)), (None, None, []))[2]

for i in range(len(filenames)):
    """Correct script body"""
    cmds.file("{}assets/Chars/1Defult/MH/rig/".format(project_path) + filenames[i], o=True)
    cmds.file("{}/bufer/ctrl.ma".format(project_path), i=True)
    cmds.parent("World", "MainSystem")
    cmds.parent("General", "World")
    cmds.file(save=True)
    print("CORRECTERD {} of {} --> {}".format(i+1, len(filenames), filenames[i]))