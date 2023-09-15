import sys
import importlib


def main(batch = None):

    try:
        from Scene.BaseScene import BaseScene
        base_scene = BaseScene()
    except:
        if batch:
            return False

        from GSMaya.GUI.Windows.PromoteTo.PromoteToWindow import PromoteToWindow
        main_window = PromoteToWindow()
        main_window.load()
        return None
    if batch:
        return get_scene_cls(base_scene.get_scene_type())

    print get_scene_cls(base_scene.get_scene_type())
    from GSMaya.GUI.Windows.MainMayaWindow import MainMayaWindow
    main_window = MainMayaWindow(get_scene_cls(base_scene.get_scene_type()))
    main_window.load()


def get_scene_cls(cls_name):
    module_path = "GSMaya.ProjectManager.Scene."
    scene_type = cls_name
    module_name = module_path + scene_type
    print module_name
    module = importlib.import_module(module_name)
    cls = getattr(module, scene_type)
    return cls
