from PyQt5 import QtWidgets
from ..mayaMixin import MayaQWidgetDockableMixin
import maya.cmds as cmds

class MyDockableWindow(MayaQWidgetDockableMixin, QtWidgets.QWidget):

    def __init__(self):
        super(MyDockableWindow, self).__init__()

        # Delete existing UI
        try:
            cmds.deleteUI('MDWWorkspaceControl')
        except RuntimeError:
            pass

        self.setWindowTitle('MDW Workspace Control')
        self.resize(500, 400)
        self.setObjectName('MDW')
        self.show(dockable=True)

MyWin = MyDockableWindow()