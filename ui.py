# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 609)
        MainWindow.setStyleSheet("background: #ff6a3d;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 311, 541))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background: #a3ebe6;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 0, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(330, 20, 311, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background: #a3ebe6;\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(330, 190, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet("background: #6a6c85;\n"
"color: white;")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(500, 190, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet("background: #6a6c85;\n"
"color: white;")
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(330, 230, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setStyleSheet("background: #6a6c85;\n"
"color: white;")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(330, 500, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_4.setFont(font)
        self.toolButton_4.setStyleSheet("background: #6a6c85;\n"
"color: white;")
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_5.setGeometry(QtCore.QRect(480, 500, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_5.setFont(font)
        self.toolButton_5.setStyleSheet("background: #6a6c85;\n"
"color: white;")
        self.toolButton_5.setObjectName("toolButton_5")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(330, 290, 301, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("background: #a3ebe6;\n"
"")
        self.listWidget_2.setObjectName("listWidget_2")
        self.toolButton_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_6.setGeometry(QtCore.QRect(330, 540, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_6.setFont(font)
        self.toolButton_6.setStyleSheet("background: #6a6c85;\n"
"color: white;")
        self.toolButton_6.setObjectName("toolButton_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 270, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 470, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background: #a3ebe6;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "список заміток"))
        self.toolButton.setText(_translate("MainWindow", "Створити замітку"))
        self.toolButton_2.setText(_translate("MainWindow", "Видалити замітку"))
        self.toolButton_3.setText(_translate("MainWindow", "Створити замітку"))
        self.toolButton_4.setText(_translate("MainWindow", "Додати до замітки"))
        self.toolButton_5.setText(_translate("MainWindow", "Відкрити від замітки"))
        self.toolButton_6.setText(_translate("MainWindow", "Шукати замітки по тегу"))
        self.label_2.setText(_translate("MainWindow", "Список тегів"))
        self.lineEdit.setText(_translate("MainWindow", "Введи тег..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())