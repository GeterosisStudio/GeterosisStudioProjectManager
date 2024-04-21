#Import api modules
import maya.OpenMaya as api
import maya.OpenMayaUI as apiUI
import maya.cmds as cmds



path = "D:/test/"
import os

filenames = os.listdir(path)
for i in filenames:
    cmds.file(path + i, o=1, force=True, options="v=0;", prompt=False)
    scene_name = cmds.file(q=1, sn=1, shn=1).replace(".mb", "")

    cmds.setAttr("persp.tx", 840)
    cmds.setAttr("persp.ty", 630)
    cmds.setAttr("persp.tz", 840)
    cmds.setAttr("persp.rx", -27.938)
    cmds.setAttr("persp.ry", 45)
    cmds.setAttr("persp.rz", 0)

    selected_objects = cmds.ls(type="mesh")

    target_object = selected_objects

    active_camera = cmds.getPanel(withFocus=True)

    cmds.viewFit("persp", f=1.0, fitFactor=0.9)

    view = apiUI.M3dView.active3dView()

    image = api.MImage()

    if view.getRendererName() == view.kViewport2Renderer:
        image.create(view.portWidth(), view.portHeight(), 4, api.MImage.kFloat)
        view.readColorBuffer(image)
        image.convertPixelFormat(api.MImage.kByte)
        print("viewPort2")
    else:
        view.readColorBuffer(image)
        print("old viewport !")
    image.writeToFile(path + scene_name + '.png', 'png')
