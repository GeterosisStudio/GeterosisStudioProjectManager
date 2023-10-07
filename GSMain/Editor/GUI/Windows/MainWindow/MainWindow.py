import sys
from PySide6.QtWidgets import QApplication, QWidget
q = QApplication(sys.argv)
w = QWidget()
w.show()
sys.exit(q.exec())
