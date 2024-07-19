import sys
from PySide2 import QtWidgets
from mainwindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


#
#
# def main():
#     func = input("Enter function of x (e.g., 5*x**3 + 2*x): ")
#     min_x = input("Enter min value of x: ")
#     max_x = input("Enter max value of x: ")
#
#     plot_function(func, min_x, max_x)


