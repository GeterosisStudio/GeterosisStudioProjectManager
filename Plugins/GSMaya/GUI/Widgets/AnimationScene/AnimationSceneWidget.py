from PySide2 import QtWidgets, QtUiTools
from Plugins.GSMaya.ProjectManager.Scene.BaseScene import BaseScene
from Plugins.GSMain import Log


class AnimationSceneWidget(QtWidgets.QWidget):

    def __init__(self, SCENE_CLS_OBJECT=None):
        super(AnimationSceneWidget, self).__init__()

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(__file__.replace('.py', '.ui'))

        if SCENE_CLS_OBJECT and issubclass(SCENE_CLS_OBJECT.__class__, BaseScene):
            self.generate()
        elif SCENE_CLS_OBJECT and not issubclass(SCENE_CLS_OBJECT.__class__, BaseScene):
            print(SCENE_CLS_OBJECT.__class__)
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
