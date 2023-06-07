from PyQt5 import QtWidgets, uic, QMainWindow

class Window(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__( *args, **kwargs)
        uic.loadUi(os.path.join(os.path.abspath(__file__).replace("\\", "/").rsplit("/", 1)[0],
                                'UiPromoteTo.ui'), self)