from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

import sys
import math
from math import *
from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(80, 60, 591, 281))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 500, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 410, 341, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(510, 420, 71, 41))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(640, 420, 91, 41))
        self.spinBox_2.setObjectName("spinBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.main_layout = QVBoxLayout()
        self.setWindowTitle("Крутые функции")

        self.form = QFormLayout(self)
        self.form_1 = QFormLayout(self)

        self.graphicsView.getAxis('bottom').setScale(True)
        self.graphicsView.getAxis('left').setScale(True)

        self.spinBox_2.setRange(-1000, 1000)
        self.spinBox.setRange(-1000, 1000)
        self.points = QTextEdit(self)
        self.points.setReadOnly(True)
        self.pushButton.setText("Построить")
        self.pushButton.clicked.connect(self.function)
        self.form.addRow(self.graphicsView)
        self.label1 = QLabel( "Названия функций совпадают с названиями функций в языке (например тангенс - это tan(x)")
        self.form.addRow(self.label1)
        self.form.addRow(self.lineEdit, self.pushButton)
        self.form.addRow(self.spinBox, self.spinBox_2)
        self.form_1.addRow(QLabel("Выколотые точки в координатах"), self.points)

        self.main_layout.addLayout(self.form, stretch=10)
        self.main_layout.addLayout(self.form_1, stretch=1)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

    def function(self):
        self.points.clear()
        lst = []
        self.graphicsView.clear()
        l = int(self.spinBox.text())
        r = int(self.spinBox_2.text())
        y = []
        while l <= r:
            x = l
            try:
                y.append(l)
                lst.append(eval(self.lineEdit.text()))
            except Exception as error:
                self.graphicsView.plot(lst)
                y.pop()
                self.points.insertPlainText(f"{str(l)} : {error}\n")
            l += 0.01
        try:
            self.graphicsView.setAspectLocked()
            self.graphicsView.plot(y, lst)
        except Exception as error:
            self.points.insertPlainText(f"Ошибка построения графика {error}\n")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
