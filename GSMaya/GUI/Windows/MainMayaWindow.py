from GSMaya.ProjectManager.Scene.BaseScene import BaseScene
from PySide2 import QtWidgets


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

    def buils_scene_widgets(self):
        """
        This method collects and connects widgets to the main menu of the scene
        in the order of the class hierarchy from the BaseScene.
        :return: scene widget (QtWidgets)
        """

        scene_cls_tree = list(reversed(self.scene_cls.mro()))[1:]
        for cls in scene_cls_tree:
            print cls

        return True

    def load(self):
        print("sas")
        self.buils_scene_widgets()