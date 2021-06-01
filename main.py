import sys
from PyQt5 import QtWidgets, uic
from mydesign import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Window()
    application.show()
    sys.exit(app.exec())