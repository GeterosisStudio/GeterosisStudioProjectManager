import sys
import importlib


gspm_main_window = None

def main(batch = None):
    global gspm_main_window
    try:
        from Scene.BaseScene import BaseScene
        base_scene = BaseScene()
    except:
        if batch:
            return False

        from GSMaya.GUI.Windows.PromoteTo.PromoteToWindow import PromoteToWindow
        gspm_main_window = PromoteToWindow()
        gspm_main_window.load()
        return None
    if batch:
        return get_scene_cls_obj(base_scene.get_scene_type())

    from GSMaya.GUI.Windows import MainMayaWindow as MainMayaWindow
    reload(MainMayaWindow)
    gspm_main_window = MainMayaWindow.MainMayaWindow(get_scene_cls_obj(base_scene.get_scene_type()))
    gspm_main_window.load()


def get_scene_cls_obj(cls_name):
    module_path = "GSMaya.ProjectManager.Scene."
    scene_type = cls_name
    module_name = module_path + scene_type
    module = importlib.import_module(module_name)
    cls = getattr(module, scene_type)
    return cls()
