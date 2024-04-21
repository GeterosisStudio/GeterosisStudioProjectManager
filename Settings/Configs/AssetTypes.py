import json
from _plugins.GSMain import Log
from Settings import Enviroment

PROJECT_MANAGER_PATH = Enviroment.GSPM_PATH


def get_asset_struct(project_path) -> object:
    try:
        with open(project_path + 'Settings/AssetTypes.gsconfig') as asset_type_config_file:
            asset_type_config = json.load(asset_type_config_file)
        return asset_type_config
    except Exception as e:
        Log.warning(str(e))
