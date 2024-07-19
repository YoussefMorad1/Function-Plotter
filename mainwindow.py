from PySide2.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from qt_ui_elements.ui_mainwindow import Ui_MainWindow
from PySide2 import QtWidgets
from evaluator import FunctionEvaluator


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.plotWidget.setLayout(QVBoxLayout())
        self.initialize_plot()

        # Connect click signals of digits and operators to insert text
        self.digitsButtonGroup.buttonClicked.connect(self.insert_button_text)
        self.operatorsButtonGroup.buttonClicked.connect(self.insert_button_text)
        self.XButton.clicked.connect(lambda: self.insert_button_text(self.XButton))
        # Connect click signal of functions to insert function name with parentheses
        self.functionsButtonGroup.buttonClicked.connect(self.on_function_button_clicked)
        # Connect click signal of the backspace button to delete the last character
        self.backSpaceButton.clicked.connect(self.lineEdit.backspace)
        # Connect click signal of the enter button to evaluate the function
        self.enterButton.clicked.connect(self.evaluate_function)

    def insert_button_text(self, button):
        self.lineEdit.insert(button.text())
        self.lineEdit.setFocus()

    def on_function_button_clicked(self, button):
        self.lineEdit.insert(button.text() + '()')
        self.lineEdit.cursorBackward(False, 1)
        self.lineEdit.setFocus()

    def evaluate_function(self):
        try:
            fig = FunctionEvaluator.plot_function(self.lineEdit.text(), 0, 100)
            canvas = FigureCanvas(fig)
            for i in reversed(range(self.plotWidget.layout().count())):
                self.plotWidget.layout().itemAt(i).widget().deleteLater()
            self.plotWidget.layout().addWidget(canvas)
            self.statusbar.clearMessage()
        except Exception:
            self.statusbar.showMessage(f"error: unexpected characters in function")
            self.lineEdit.setFocus()

    def initialize_plot(self):
        fig = FunctionEvaluator.empty_plot()
        canvas = FigureCanvas(fig)
        self.plotWidget.layout().addWidget(canvas)