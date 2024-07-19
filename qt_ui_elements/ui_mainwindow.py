# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(772, 581)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(732, 527))
        self.centralwidget.setMaximumSize(QSize(732, 527))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout = QVBoxLayout(self.widget_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.widget_5)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.widget)
        self.functionsButtonGroup = QButtonGroup(MainWindow)
        self.functionsButtonGroup.setObjectName(u"functionsButtonGroup")
        self.functionsButtonGroup.addButton(self.pushButton)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #808080;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.widget)
        self.operatorsButtonGroup = QButtonGroup(MainWindow)
        self.operatorsButtonGroup.setObjectName(u"operatorsButtonGroup")
        self.operatorsButtonGroup.addButton(self.pushButton_12)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"	background-color: #808080;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_12, 4, 3, 1, 1)

        self.pushButton_18 = QPushButton(self.widget)
        self.digitsButtonGroup = QButtonGroup(MainWindow)
        self.digitsButtonGroup.setObjectName(u"digitsButtonGroup")
        self.digitsButtonGroup.addButton(self.pushButton_18)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet(u"QPushButton {\n"
"	background-color: #A9A9A9;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_18, 6, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.widget)
        self.digitsButtonGroup.addButton(self.pushButton_9)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"	background-color: #A9A9A9;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_9, 4, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.widget)
        self.operatorsButtonGroup.addButton(self.pushButton_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	background-color: #808080;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_4, 2, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.widget)
        self.operatorsButtonGroup.addButton(self.pushButton_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	background-color: #808080;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.widget)
        self.digitsButtonGroup.addButton(self.pushButton_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	background-color: #A9A9A9;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_5, 3, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.widget)
        self.digitsButtonGroup.addButton(self.pushButton_10)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"	background-color: #A9A9A9;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_10, 4, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.widget)
        self.digitsButtonGroup.addButton(self.pushButton_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"	background-color: #A9A9A9;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_7, 3, 2, 1, 1)

        self.pushButton_14 = QPushButton(self.widget)
        self.digitsButtonGroup.addButton(self.pushButton_14)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"	background-color: #A9A9A9;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_14, 5, 1, 1, 1)

        self.XButton = QPushButton(self.widget)
        self.XButton.setObjectName(u"XButton")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.XButton.setFont(font1)
        self.XButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #808080;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.XButton, 6, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget)
        self.functionsButtonGroup.addButton(self.pushButton_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color: #808080;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.widget)
        self.digitsButtonGroup.addButton(self.pushButton_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"	background-color: #A9A9A9;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_6, 3, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.widget)
        self.digitsButtonGroup.addButton(self.pushButton_11)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"	background-color: #A9A9A9;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_11, 4, 2, 1, 1)

        self.pushButton_16 = QPushButton(self.widget)
        self.operatorsButtonGroup.addButton(self.pushButton_16)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet(u"QPushButton {\n"
"	background-color: #808080;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_16, 5, 3, 1, 1)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setItalic(True)
        self.lineEdit.setFont(font2)
        self.lineEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid gray;\n"
"	color: white;\n"
"	background-color: #050505;\n"
"	padding: 5px;\n"
"}")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 4)

        self.pushButton_15 = QPushButton(self.widget)
        self.digitsButtonGroup.addButton(self.pushButton_15)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet(u"QPushButton {\n"
"	background-color: #A9A9A9;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_15, 5, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.widget)
        self.operatorsButtonGroup.addButton(self.pushButton_8)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"	background-color: #808080;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_8, 3, 3, 1, 1)

        self.pushButton_13 = QPushButton(self.widget)
        self.digitsButtonGroup.addButton(self.pushButton_13)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"	background-color: #A9A9A9;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_13, 5, 0, 1, 1)

        self.backSpaceButton = QPushButton(self.widget)
        self.backSpaceButton.setObjectName(u"backSpaceButton")
        self.backSpaceButton.setFont(font)
        self.backSpaceButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #808080;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #707070;\n"
"	border: 1px solid gray;\n"
"	padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.backSpaceButton, 6, 2, 1, 1)

        self.enterButton = QPushButton(self.widget)
        self.enterButton.setObjectName(u"enterButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.enterButton.sizePolicy().hasHeightForWidth())
        self.enterButton.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setItalic(False)
        self.enterButton.setFont(font3)
        self.enterButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 174, 255);\n"
"	border: 1px solid gray;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 1px solid gray;\n"
"	background-color: rgba(0, 148, 216, 252);\n"
"	color: black;\n"
"}")

        self.gridLayout.addWidget(self.enterButton, 6, 3, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.widget_3 = QWidget(self.widget_5)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy3)
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.doubleSpinBox = QDoubleSpinBox(self.widget_3)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        sizePolicy3.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.doubleSpinBox)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.widget_4)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_2)


        self.verticalLayout.addWidget(self.widget_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.widget_5, 0, 0, 1, 1)

        self.plotWidget = QWidget(self.centralwidget)
        self.plotWidget.setObjectName(u"plotWidget")

        self.gridLayout_2.addWidget(self.plotWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 772, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        font4 = QFont()
        font4.setPointSize(12)
        self.statusbar.setFont(font4)
        self.statusbar.setStyleSheet(u"color: red;")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"log10", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.XButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"sqrt", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"F(X)", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.backSpaceButton.setText(QCoreApplication.translate("MainWindow", u"\u232b", None))
        self.enterButton.setText(QCoreApplication.translate("MainWindow", u"\u21b5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Min X:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Max X:", None))
    # retranslateUi

