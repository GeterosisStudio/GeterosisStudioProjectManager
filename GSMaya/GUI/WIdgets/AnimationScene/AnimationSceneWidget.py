from PySide2 import QtWidgets, QtUiTools
import os


class AnimationSceneWidget(QtWidgets.QWidget):
    def __init__(self):
        super(AnimationSceneWidget, self).__init__()

        relative_file_path = "/GSMaya/GUI/Widgets/AnimationSceneWidget/AnimationSceneWidget.ui"
        ui_path = os.getcwd() + relative_file_path

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(ui_path)
        self.ui.save_btn.clicked.connect(self.on_button_clicked)
        self.ui.override_checkBox.clicked.connect(lambda: self.ui.final_checkBox.setChecked(False) if self.ui.final_checkBox.isChecked() else None)
        self.ui.final_checkBox.clicked.connect(lambda: self.ui.override_checkBox.setChecked(False) if self.ui.override_checkBox.isChecked() else None)
        self.ui.import_lybrary_animation_btn.clicked.connect(self.on_button_clicked)
        self.ui.paie_btn.clicked.connect(self.on_button_clicked)
        self.ui.walkin_bend_btn.clicked.connect(self.on_button_clicked)

    def load(self):
        self.ui.show()

    def on_button_clicked(self):
        print("YES")
