# -------------------------------------------------------------------------------------------------------------------- #

import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

# ==================================================================================================================== #
# Custom Node
# ==================================================================================================================== #

# Basic Parameters for node creation
nodeName = "GSPMSceneNode"
nodeID = OpenMaya.MTypeId(0x100fff)

# -------------------------------------------------------------------------------------------------------------------- #

# Class to create Custom Node
class GSPMSceneNode(OpenMayaMPx.MPxNode):
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)

# -------------------------------------------------------------------------------------------------------------------- #

def nodeCreator():
    return OpenMayaMPx.asMPxPtr(GSPMSceneNode())

# -------------------------------------------------------------------------------------------------------------------- #

def nodeInitializer():


    # Get Output Path
    # Create function set for output string attribute
    project_name = OpenMaya.MFnStringData().create("")
    string_data_attribute = OpenMaya.MFnTypedAttribute()
    GSPMSceneNode.project_name = string_data_attribute.create("Project name", "prn", OpenMaya.MFnData.kString,
                                                                       project_name)
    # Attaching output Attributes
    GSPMSceneNode.addAttribute(GSPMSceneNode.project_name)

    # Get Output Path
    # Create function set for output string attribute
    project_path = OpenMaya.MFnStringData().create("")
    string_data_attribute = OpenMaya.MFnTypedAttribute()
    GSPMSceneNode.project_path = string_data_attribute.create("Project path", "prp", OpenMaya.MFnData.kString,
                                                                   project_path)
    # Attaching output Attributes
    GSPMSceneNode.addAttribute(GSPMSceneNode.project_path)



    # Get Input Path
    # Create function set for input string attribute
    scene_type = OpenMaya.MFnStringData().create("")
    input_directory_attribute = OpenMaya.MFnTypedAttribute()
    GSPMSceneNode.scene_type = input_directory_attribute.create("Scene type", "st", OpenMaya.MFnData.kString,
                                                                scene_type)
    # Attaching input Attributes
    GSPMSceneNode.addAttribute(GSPMSceneNode.scene_type)


# -------------------------------------------------------------------------------------------------------------------- #

# Initialize the script plugin
def initializePlugin(mobject):
    mPlugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mPlugin.registerNode(nodeName, nodeID, nodeCreator, nodeInitializer)
    except:
        sys.stderr.write("Failed to register node: {}".format(nodeName))

# -------------------------------------------------------------------------------------------------------------------- #

# Uninitialize the script plugin
def uninitializePlugin(mobject):
    mPlugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mPlugin.deregisterNode(nodeID)
    except:
        sys.stderr.write("Failed to deregister node: {}".format(nodeName))

#