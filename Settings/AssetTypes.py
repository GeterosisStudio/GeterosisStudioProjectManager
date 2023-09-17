import os
import json
from GSMain import Log
from Settings import Enviroment


PROJECT_MANAGER_PATH = Enviroment.GSPM_PATH
def get_all_types():
    try:
        with open(PROJECT_MANAGER_PATH + 'Settings/AssetTypes.gsconfig') as asset_type_config_file:
            asset_type_config = json.load(asset_type_config_file)
        return asset_type_config
    except Exception as e:
        Log.warning(str(e))
