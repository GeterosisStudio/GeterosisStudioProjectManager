""" This script import unreal fbx levels, reduse and export an new fbx file"""

import os
import bpy


def fbx_level_reexport(project_path):
    file_input_dir = "{}assets/Sets/Maps/Export/UnrealExport/".format(project_path)
    filenames = next(os.walk(file_input_dir), (None, None, []))[2]
    file_output_dir = "assets/Sets/Maps/Export/BlenderExport/".format(project_path)
    for i in range(len(filenames)):

        # if crash reexport
        if not -1 < i <= 100000000:
            continue
        if os.path.isfile(file_output_dir + filenames[i]):
            continue

        bpy.ops.import_scene.fbx(filepath=file_input_dir + filenames[i])
        objs = bpy.data.objects
        try:
            objs.remove(objs["LevelBounds_0"], do_unlink=True)
        except:
            pass
        try:
            objs.remove(objs["WorldSettings"], do_unlink=True)
        except:
            pass
        ob = bpy.context.scene.objects['LandscapeStreamingProxy_0']  # Get the object
        bpy.ops.object.select_all(action='DESELECT')  # Deselect all objects
        bpy.context.view_layer.objects.active = ob  # Make the cube the active object
        ob.select_set(True)
        bpy.ops.object.modifier_add(type='DECIMATE')
        bpy.context.object.modifiers["Decimate"].ratio = 0.001
        bpy.ops.export_scene.fbx(filepath=file_output_dir + filenames[i], use_selection=True)
        objs.remove(objs['LandscapeStreamingProxy_0'], do_unlink=True)
