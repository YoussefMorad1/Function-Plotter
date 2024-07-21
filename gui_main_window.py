from PySide2.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from qt_ui_elements.ui_mainwindow import Ui_MainWindow
from PySide2 import QtWidgets
from function_plotter import FunctionPlotter
import matplotlib.pyplot as plt


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main window of the application. It inherits from Ui_MainWindow generated by Qt Designer."""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.plotWidget.setLayout(QVBoxLayout())
        self.initialize_plot(self.minSpinBox.value(), self.maxSpinBox.value())
        self.setFixedSize(1055, 586)

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
        # Connect click signal of the clear button to clear the line edit
        self.ACButton.clicked.connect(self.lineEdit.clear)

    def insert_button_text(self, button):
        """Inserts the text of the clicked button to the line edit."""
        self.lineEdit.insert(button.text())
        self.lineEdit.setFocus()

    def on_function_button_clicked(self, button):
        """Inserts the function name with parentheses to the line edit."""
        self.lineEdit.insert(button.text() + '()')
        self.lineEdit.cursorBackward(False, 1)
        self.lineEdit.setFocus()

    def evaluate_function(self):
        """Evaluates the function and plots it in the plot widget."""
        try:
            fig = FunctionPlotter.plot_function(self.lineEdit.text(), self.minSpinBox.value(), self.maxSpinBox.value())
            plt.close(fig)  # Close the figure to avoid memory leak
            canvas = FigureCanvas(fig)
            for i in reversed(range(self.plotWidget.layout().count())):
                self.plotWidget.layout().itemAt(i).widget().deleteLater()
            self.plotWidget.layout().addWidget(canvas)
            self.statusbar.clearMessage()
        except Exception as e:
            self.statusbar.showMessage(str(e))
            self.lineEdit.setFocus()

    def initialize_plot(self, minX, maxX):
        """Initializes the plot widget with an empty plot."""
        fig = FunctionPlotter.empty_plot(minX, maxX)
        plt.close(fig) # Close the figure to avoid memory leak
        canvas = FigureCanvas(fig)
        self.plotWidget.layout().addWidget(canvas)
