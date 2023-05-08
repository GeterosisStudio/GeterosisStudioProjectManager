import json

asset_data_types = {}

asset_data_types["char"] = {"path": "assets/chars/"}
asset_data_types["prop"] = {"path": "assets/props/"}
asset_data_types["set"] = {"path": "assets/sets/"}
asset_data_types["map"] = {"path": "assets/maps/"}

asset_data_types["animscene"] = {"path": "animation/scenes/"}
asset_data_types["movescene"] = {"path": "animation/movement/"}

asset_data_types["logicep"] = {"path": "logicmaps/scenes/"}




with open("AssetTypes.gsconfig", 'w') as file:
    json_string = json.dumps(asset_data_types, indent=4)
    file.write(json_string)
