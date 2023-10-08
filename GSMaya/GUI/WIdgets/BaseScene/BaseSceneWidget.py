import Settings.Enviroment

from PySide2 import QtWidgets, QtUiTools
from GSMaya.ProjectManager.Scene.BaseScene import BaseScene
from GSMain import Log
from GSMaya.ProjectManager.MayaProject import MayaProject

class BaseSceneWidget(QtWidgets.QWidget):

    def __init__(self, SCENE_CLS_OBJECT=None):
        super(BaseSceneWidget, self).__init__()

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(__file__.replace('.py', '.ui'))
        self.scene_cls_object = SCENE_CLS_OBJECT
        self.project = MayaProject()

        if self.scene_cls_object and issubclass(self.scene_cls_object.__class__, BaseScene):
            self.init()
        elif self.scene_cls_object and not issubclass(self.scene_cls_object.__class__, BaseScene):
            Log.warning("class object {0} is not subclass of BaseScene class".format(self.scene_cls_object))
        else:
            Log.warning("Scene class is None")

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.ui)
        self.setLayout(self.layout)

    def init(self):
        if self.scene_cls_object.is_project:
            self.ui.project_name_label.setText(self.project.get_project_name())
        self.ui.scene_type_label.setText(self.scene_cls_object.get_scene_type())
        self.ui.scene_name_label.setText(self.scene_cls_object.get_scene_version_name())
        self.ui.save_button.clicked.connect(self.save)
        self.ui.override_check_box.clicked.connect(lambda state: self.ui.final_check_box.setChecked(False))
        self.ui.final_check_box.clicked.connect(lambda state: self.ui.override_check_box.setChecked(False))

    def save(self):

        if self.ui.override_check_box.isChecked():
            return self.scene_cls_object.save()

        if self.ui.final_check_box.isChecked():
            print("Final save dont tested")
            #self.scene_cls_object.final_save()
            return True

        return self.scene_cls_object.work_incremental_save()

