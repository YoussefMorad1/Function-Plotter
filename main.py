import sys
from PySide2 import QtWidgets
from gui_main_window import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
