import os
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from Editor.GUI.Windows.Project.ProjectWindow import ProjectWindow
from Editor.GUI.Windows.ProjectBrowser import ProjectBrowserWindow
from Core import Icons


def load():
    app = QApplication()
    if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]) and ".gsproj" in sys.argv[1]:
        window = ProjectWindow(sys.argv[1])
    elif len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
        if sys.argv[1].split("/")[-1] != "":
            name = sys.argv[1].split("/")[-1] + ".gsproj"
        else:
            name = sys.argv[1].split("/")[-2] + ".gsproj"
        if name in os.listdir(sys.argv[1]):
            window = ProjectWindow(sys.argv[1] + name)
        print(sys.argv[1])
    else:
        window = ProjectBrowserWindow.ProjectBrowserWindow(__file__.replace("\\", "/"))

    app.setWindowIcon(QIcon(Icons.get_icon_path_from_name("GSPM.ico")))

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    load()
