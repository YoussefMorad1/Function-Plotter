from PySide2 import QtWidgets
from gui_main_window import MainWindow
import pytest
from pytestqt import qtbot


@pytest.fixture
def app(qtbot):
    test_app = QtWidgets.QApplication()
    main_window = MainWindow()
    qtbot.addWidget(main_window)
    return main_window


# @pytest.fixture
# def app(qtbot):
#     test_app = QtWidgets.QApplication([])
#     main_window = MainWindow()
#     qtbot.addWidget(main_window)
#     return main_window, qtbot

def test_insert_button_text(app, qtbot):
    # for each button in the digitsButtonGroup, click it
    curText = ''
    for button in app.digitsButtonGroup.buttons():
        qtbot.mouseClick(button, qtbot.LeftButton)
        curText += button.text()
    for button in app.operatorsButtonGroup.buttons():
        qtbot.mouseClick(button, qtbot.LeftButton)
        curText += button.text()

    # click the XButton
    qtbot.mouseClick(app.XButton, qtbot.LeftButton)
    curText += app.XButton.text()

    assert app.lineEdit.text() == curText


def test_erase_clear_buttons(app, qtbot):
    # for each button in the digitsButtonGroup, click it
    for button in app.digitsButtonGroup.buttons():
        qtbot.mouseClick(button, qtbot.LeftButton)

    # click the backSpaceButton and check that the last character is removed
    prevText = app.lineEdit.text()
    qtbot.mouseClick(app.backSpaceButton, qtbot.LeftButton)
    assert app.lineEdit.text() == prevText[:-1]
    assert len(app.lineEdit.text()) > 0
    # click the ACButton
    qtbot.mouseClick(app.ACButton, qtbot.LeftButton)
    assert app.lineEdit.text() == ''


def test_evaluate_function_valid(app, qtbot):
    app.lineEdit.setText('2*x')
    app.minSpinBox.setValue(0)
    app.maxSpinBox.setValue(10)
    qtbot.mouseClick(app.enterButton, qtbot.LeftButton)
    assert app.statusbar.currentMessage() == ''


def test_evaluate_function_invalid(app, qtbot):
    app.lineEdit.setText('2*x+')
    app.minSpinBox.setValue(0)
    app.maxSpinBox.setValue(10)
    qtbot.mouseClick(app.enterButton, qtbot.LeftButton)
    assert app.statusbar.currentMessage() != ''
