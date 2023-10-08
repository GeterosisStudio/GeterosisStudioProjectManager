import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from GSMain.Editor.GUI.Windows.ProjectBrowser.ProjectBrowser import ProjectBrowser
from Core import Icons


if len(sys.argv) >= 2:
    q = QApplication(sys.argv[1])
else:
    q = QApplication()

q.setWindowIcon(QIcon(Icons.get_icon_path_from_name("GSPM.ico")))
w = ProjectBrowser()
w.show()
sys.exit(q.exec())
