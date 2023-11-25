project_name = None
UE_PROJECT_PATH = "Game/{}".format(project_name)

AssetName = "SM_PROPS_e001s01d01v001_Chris.Fbx"


AssetNameToList = AssetName.split("_")
AssetFirstName = AssetNameToList[0]
AssetSecondName = AssetNameToList[1]
AssetThirdName = AssetNameToList[2]
AssetFourthName = AssetNameToList[3]
AnmSceneFolder = AssetThirdName[0:4]
AnmSceneChar = AssetFourthName
AssetPrefix = AssetFirstName + "_" + AssetSecondName + "_"


AssetPath = {
    "SM_BUILDEXT_": "/Assets/Props/Builds/Exteriors" + "/" + AssetThirdName + "/" + AssetName,
    "SM_BUILDINT_": "/Assets/Props/Builds/Interiors" + "/" + AssetThirdName + "/" + AssetName,
    "SM_BUILDMID_": "/Assets/Props/Builds/Middles" + "/" + AssetThirdName + "/" + AssetName,
    "SM_PROPS_": "/Assets/Props/Props" + "/"  + AssetName,
    "BP_PROPS_": "/Blueprints/Props/" + "/"  + AssetName,
    "ANM_SCENECHAR_": "/Animations/Scenes" + "/" + AnmSceneFolder + "/" + AssetThirdName + "/" + AssetName,
    "A_SCENECHARWAVE_": "/Animations/Scenes" + "/" + AnmSceneFolder + "/" + AssetThirdName + "/" + AssetName,
    "SK_HEAD_": "/Assets/Chars/Head",
    "SK_TORSO_": "/Assets/Chars/Torso",
    "SK_ARMS_": "/Assets/Chars/Arms",
    "SK_PANTS_": "/Assets/Chars/Pants",
    "SK_LEGS_": "/Assets/Chars/Legs",

    "BP_HEAD_": "Blueprints/Chars/Head",
    "BP_TORSO_": "Blueprints/Chars/Torso",
    "BP_ARMS_": "Blueprints/Chars/Arms",
    "BP_PANTS_": "Blueprints/Chars/Pants",
    "BP_LEGS_": "Blueprints/Chars/Legs"
}

def return_asset():
    print(UE_PROJECT_PATH + AssetPath[AssetPrefix])
