import unreal

def auto_export_levels(project_path):
    # instances of unreal classes
    editor_util = unreal.EditorUtilityLibrary()
    system_lib = unreal.SystemLibrary()

    # get the selected assets
    selected_assets = editor_util.get_selected_assets()

    # export selected assets
    for asset in selected_assets:
        asset_name = system_lib.get_object_name(asset)
        export_task = unreal.AssetExportTask()
        export_task.set_editor_property("object", asset)
        export_task.set_editor_property("filename", "{}bufer/Maps/{}".format(project_path, asset_name))
        export_task.set_editor_property("automated", False)
        #export_task.set_editor_property("exporter", unreal.StaticMeshExporterFBX())

        unreal.Exporter.run_asset_export_task(export_task)
