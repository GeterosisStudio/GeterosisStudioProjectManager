from PySide2 import QtWidgets, QtUiTools
from GSMaya.ProjectManager.Scene.AnimationBaseScene import AnimationSceneBase

class AnimationSceneWIdget(QtWidgets.QWidget):
    def __init__(self, gspm_maya_scene_cls):
        super(AnimationSceneWIdget, self).__init__()
        if not isinstance(gspm_maya_scene_cls, AnimationSceneBase):
            raise ValueError("{0} in not instance {1}.".format(gspm_maya_scene_cls, AnimationSceneBase))



        loader = QtUiTools.QUiLoader()
        self.ui = loader.load('Playblast.ui')

