import sys
from PySide6.QtWidgets import QApplication
from GUI.Windows.ProjectBrowser.ProjectBrowser import ProjectBrowser

if len(sys.argv) >= 2:
    q = QApplication(sys.argv[1])
else:
    q = QApplication()
w = ProjectBrowser()
w.show()
sys.exit(q.exec())
