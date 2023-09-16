from PySide2 import QtWidgets, QtUiTools
import os
import Settings.Enviroment

class BaseSceneWidget(QtWidgets.QWidget):
    def __init__(self, scene_cls=None):
        super(BaseSceneWidget, self).__init__()

        relative_file_path = "GSMaya/GUI/Widgets/BaseScene/BaseSceneWidget.ui"
        ui_path = Settings.GSPM_PATH + relative_file_path

        print ui_path

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(ui_path)

