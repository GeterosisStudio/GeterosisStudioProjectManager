import os.path
from GSMain import Log
import maya.cmds as cmds
from GSMain import Config
reload(Config)




def promote_to_base():
    if not cmds.file(q=1, sn=1):
        Log.warning("File non saved.")
        return False
    return create_config("base", None)

def promote_to_animation_scene():
    if not cmds.file(q=1, sn=1):
        Log.warning("File non saved.")
        return False
    target_path = get_root_path() + "target/"
    if not os.path.exists(get_root_path() + "target/"):
        os.mkdir(target_path)
    return create_config("animation_scene", None)