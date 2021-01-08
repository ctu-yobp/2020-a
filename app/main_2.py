import os
import sys
from PyQt5 import QtWidgets, uic,QtSql,QtCore,QtGui
from PyQt5.QtWidgets import QFileDialog

from data import Databaze
from main_1 import Ui_MainWindow
from okno_import_2 import MujDialog

class Uvod(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.menuImport.addAction('Projekt')
        self.menuImport.triggered.connect(self.pozdrav)

    def pozdrav(self):
        # print('jde to')
        okno = MujDialog()

if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    hlavni_okno=Uvod()
    hlavni_okno.show()
    app.exec()
