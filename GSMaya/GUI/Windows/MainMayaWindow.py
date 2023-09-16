from GSMaya.ProjectManager.Scene.BaseScene import BaseScene
from PySide2 import QtWidgets, QtUiTools
import os
import importlib
import Settings


class MainMayaWindow(QtWidgets.QWidget):
    """
    This class provides a graphical interface for using the GSPM tools within Maya and the Maya part of the GSPM.
    """

    def __init__(self, scene_cls= None):
        if scene_cls == None:
            raise ValueError("Scene class is none.")
        super(MainMayaWindow, self).__init__()
        if not issubclass(scene_cls, BaseScene):
            raise ValueError("{0} not instance of BaseScene class".format(scene_cls))
        self.scene_cls = scene_cls
        self.ui = None

    def get_scene_widget_list(self):
        """
        Method collects and connects widgets to the main menu of the scene
        in the order of the class hierarchy from the BaseScene.
        :return: scene widget list (QtWidgets)
        """

        scene_cls_tree_widgets= list(reversed(self.scene_cls.mro()))[1:]
        module_path = "GSMaya.GUI.Widgets."
        scene_cls_tree_widget_list = []

        for cls in scene_cls_tree_widgets:
            cls_name = cls.__name__
            module_name = module_path + cls_name
            module = importlib.import_module(module_name + "." + cls_name + "Widget")
            widget = getattr(module, cls_name + "Widget")
            widget_object = widget(self.scene_cls)
            scene_cls_tree_widget_list.append(widget_object)

        return scene_cls_tree_widget_list

    def load(self):
        relative_file_path = "GSMaya/GUI/Windows/MainMayaWindow.ui"
        ui_path = Settings.GSPM_PATH + relative_file_path

        loader = QtUiTools.QUiLoader()
        print (ui_path)
        self.ui = loader.load(ui_path)

        cls_tree = self.get_scene_widget_list()


        self.ui.show()



