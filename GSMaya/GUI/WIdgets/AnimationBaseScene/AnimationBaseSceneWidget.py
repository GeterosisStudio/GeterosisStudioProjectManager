import Settings.Enviroment

from PySide2 import QtWidgets, QtUiTools
from GSMaya.ProjectManager.Scene.BaseScene import BaseScene
from GSMain import Log


class AnimationBaseSceneWidget(QtWidgets.QWidget):

    def __init__(self, SCENE_CLS_OBJECT=None):
        super(AnimationBaseSceneWidget, self).__init__()

        relative_file_path = "GSMaya/GUI/Widgets/AnimationBaseScene/Playblast.ui"
        ui_path = Settings.GSPM_PATH + relative_file_path

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(ui_path)

        if SCENE_CLS_OBJECT and issubclass(SCENE_CLS_OBJECT.__class__, BaseScene):
            self.generate()
        elif SCENE_CLS_OBJECT and not issubclass(SCENE_CLS_OBJECT.__class__, BaseScene):
            print SCENE_CLS_OBJECT.__class__
            Log.warning("class object {0} is not subclass of BaseScene class".format(SCENE_CLS_OBJECT))
        else:
            Log.warning("Scene class is None")

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.ui)
        self.setLayout(self.layout)
    def generate(self):
        pass


    def save_btn(self):
        print ("qqq")
