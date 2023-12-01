import unreal
from .Config import*
def assetspawn(name, translatex, translatey, translatez, rotatex, rotatey, rotatez, scalex, scaley, scalez):

    assetpath = 0

    actor = unreal.load_asset(UE_PROJECT_PATH + assetpath + actor + "." + actor)
    actor_location = unreal.Vector(translatex, translatey, translatez)
    actor_rotation = unreal.Rotator(rotatex, rotatey, rotatez)
    actor_scale = unreal.scale(scalex, scaley, scalez)
    unreal.EditorLevelLibrary.spawn_actor_from_object(actor, actor_location, actor_rotation, actor_scale)

def test():
    print("testdef")

def import_build_list(set_list):
    print(set_list)

def import_map_list(map_list):
    print(map_list)

def import_assets():
    print(UE_PROJECT_PATH)

def create_cutscene():
    print(UE_PROJECT_PATH)

def asset_type_manage():
    print(UE_PROJECT_PATH)

def test():
    pass