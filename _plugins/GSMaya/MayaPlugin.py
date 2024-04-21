# -------------------------------------------------------------------------------------------------------------------- #

import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

nodeName = "GSPMSceneNode"
nodeID = OpenMaya.MTypeId(0x100fff)


class GSPMSceneNode(OpenMayaMPx.MPxNode):
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)


def nodeCreator():
    return OpenMayaMPx.asMPxPtr(GSPMSceneNode())


def nodeInitializer():
    owner = OpenMaya.MFnStringData().create("")
    string_data_attribute = OpenMaya.MFnTypedAttribute()
    GSPMSceneNode.owner = string_data_attribute.create("owner", "own", OpenMaya.MFnData.kString, owner)
    GSPMSceneNode.addAttribute(GSPMSceneNode.owner)

    project_name = OpenMaya.MFnStringData().create("")
    string_data_attribute = OpenMaya.MFnTypedAttribute()
    GSPMSceneNode.project_name = string_data_attribute.create("Project name", "prn", OpenMaya.MFnData.kString,
                                                              project_name)
    GSPMSceneNode.addAttribute(GSPMSceneNode.project_name)

    project_path = OpenMaya.MFnStringData().create("")
    string_data_attribute = OpenMaya.MFnTypedAttribute()
    GSPMSceneNode.project_path = string_data_attribute.create("Project path", "prp", OpenMaya.MFnData.kString,
                                                              project_path)
    GSPMSceneNode.addAttribute(GSPMSceneNode.project_path)

    scene_type = OpenMaya.MFnStringData().create("")
    string_data_attribute = OpenMaya.MFnTypedAttribute()
    GSPMSceneNode.scene_type = string_data_attribute.create("Scene type", "st", OpenMaya.MFnData.kString, scene_type)
    GSPMSceneNode.addAttribute(GSPMSceneNode.scene_type)


def initializePlugin(mobject):
    mPlugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mPlugin.registerNode(nodeName, nodeID, nodeCreator, nodeInitializer)
    except:
        sys.stderr.write("Failed to register node: {}".format(nodeName))


def uninitializePlugin(mobject):
    mPlugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mPlugin.deregisterNode(nodeID)
    except:
        sys.stderr.write("Failed to deregister node: {}".format(nodeName))

#
