from PySide2 import QtWidgets, QtUiTools
from pathlib import Path

class AnimationSceneWidget(QtWidgets.QWidget):
    def __init__(self):
        super(AnimationSceneWidget, self).__init__()

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(
            'E:/Projects/core/GeterozisProjectManager/GeterosisProjectManager/GSMaya/GUI/Windows/AnimationScene/AnimScene2.ui')
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
