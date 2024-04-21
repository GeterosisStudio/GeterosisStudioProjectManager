from Plugins.GSMaya.ProjectManager.Scene.BaseScene import BaseScene
from PySide2 import QtWidgets, QtUiTools
import importlib
import Settings

class MainMayaWindow(QtWidgets.QWidget):
    """
    This class provides a graphical interface for using the GSPM tools within Maya and the Maya part of the GSPM.
    """

    def __init__(self, scene_cls_obj= None):
        if scene_cls_obj == None:
            raise ValueError("Scene class object is none.")
        super(MainMayaWindow, self).__init__()
        if not issubclass(scene_cls_obj.__class__, BaseScene):
            raise ValueError("{0} not subclass of BaseScene class".format(scene_cls_obj))
        self.scene_cls_object = scene_cls_obj
        self.ui = None

    def get_scene_widget_list(self):
        """
        Method collects and connects widgets to the main menu of the scene
        in the order of the class hierarchy from the BaseScene.
        :return: scene widget list (QtWidgets)
        """
        scene_cls_tree_list = list(reversed(self.scene_cls_object.__class__.mro()))[1:]
        module_path = "GSMaya.GUI.Widgets."
        scene_widget_list = []
        for cls in scene_cls_tree_list:
            cls_name = cls.__name__
            module_name = module_path + cls_name
            cls_path = module_name + "." + cls_name + "Widget"
            module = importlib.import_module(cls_path)
            widget = getattr(module, cls_name + "Widget")
            widget_object = widget(self.scene_cls_object)
            scene_widget_list.append(widget_object)

        return scene_widget_list

    def load(self):
        relative_file_path = self.ui = QtUiTools.QUiLoader().load(__file__.replace('.py', '.ui'))
        ui_path = Settings.GSPM_PATH + relative_file_path
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(ui_path)
        for widget in self.get_scene_widget_list():
            self.ui.scene_area_layout.addWidget(widget)



        self.ui.show()



