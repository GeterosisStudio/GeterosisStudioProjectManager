import unreal


# Path on disk to the asset you want to export
mesh_path = None



# helper function for easy task creation, like a template
def build_mesh_export_task(filename):


    # the task, and the additional fbx options, since it is a mesh
    task = unreal.AssetExportTask()
    fbx_options = unreal.FbxExportOption()


    # basic task properties
    task.set_editor_property('automated', True)
    task.set_editor_property('filename', filename)
    # if destination_name is '' it will use the on-disk filename

    task.set_editor_property('options', fbx_options)


    # additional options specifically for meshes


    return task



def export_assets():
    # construct the task, passing the path on disk and the location to store it.
    mesh_export_task = build_mesh_export_task(mesh_path)


    # using the very handy AssetToolsHelpers to do the work.
    # Note it takes a list, and so many exports can be batched
    unreal.AssetToolsHelpers.get_asset_tools().export_tasks([mesh_export_task])


export_assets()