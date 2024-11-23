from PyQt5 import QtCore, QtGui, QtWidgets
import json

from ui import Ui_MainWindow

class NoteWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_MainWindow()
        self.ui.setupUi(self)
        self.notes = {} #dict()

        self.ui.pushButton.clicket.conect(self.add_note)
        self.ui.listwidget.itemClicked.connect(self.show_note)
        self.ui.pushButton_3.clicked.connect(self.save_note)
        self.ui.pushButton_2.clicked.conect(self.del_note)
        self.ui.pushButton_4.clicked.conect(self.add_tag)
        self.ui.pushButton_5.clicked.conect(self.del_tag)
        self.ui.pushButton_6.clicked.conect(self.search_tag)

        self.load_notes()

    def load_notes(self):
        try:
            with open("notes_data json", "r", encodin"utf-8") as foles
                self.notes = json.load(file)
            self.ui.ListWidget.addItems(self.notes)
        except FileNotFoundError:
            self.notes = {}