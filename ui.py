# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(265, 262)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_header = QtWidgets.QLabel(self.centralwidget)
        self.lb_header.setEnabled(True)
        self.lb_header.setGeometry(QtCore.QRect(16, 13, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_header.setFont(font)
        self.lb_header.setAutoFillBackground(True)
        self.lb_header.setFrameShape(QtWidgets.QFrame.Panel)
        self.lb_header.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lb_header.setLineWidth(3)
        self.lb_header.setScaledContents(False)
        self.lb_header.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_header.setObjectName("lb_header")
        self.lb_result = QtWidgets.QLabel(self.centralwidget)
        self.lb_result.setGeometry(QtCore.QRect(20, 70, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.lb_result.setFont(font)
        self.lb_result.setObjectName("lb_result")
        self.ch8_number = QtWidgets.QCheckBox(self.centralwidget)
        self.ch8_number.setGeometry(QtCore.QRect(19, 106, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.ch8_number.setFont(font)
        self.ch8_number.setObjectName("ch8_number")
        self.ch8_alph = QtWidgets.QCheckBox(self.centralwidget)
        self.ch8_alph.setGeometry(QtCore.QRect(20, 140, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.ch8_alph.setFont(font)
        self.ch8_alph.setObjectName("ch8_alph")
        self.btn_generator = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generator.setGeometry(QtCore.QRect(80, 190, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.btn_generator.setFont(font)
        self.btn_generator.setStyleSheet("border: 2px solid #000000;\n"
"border-radius: 10px;\n"
"background-color: #96e1ff")
        self.btn_generator.setObjectName("btn_generator")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_header.setText(_translate("MainWindow", "Генератор Паролів"))
        self.lb_result.setText(_translate("MainWindow", "Тут буде результат"))
        self.ch8_number.setText(_translate("MainWindow", "Використовувати Числа"))
        self.ch8_alph.setText(_translate("MainWindow", "Використовувати алфавіт"))
        self.btn_generator.setText(_translate("MainWindow", "Сгенерувати"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
