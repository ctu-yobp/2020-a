import os
import sys
from PyQt5 import QtWidgets, uic,QtSql,QtCore
from PyQt5.QtWidgets import QFileDialog
from data import Databaze
from okno_import_1 import Ui_Dialog
from config import DB_CONFIG, DATA_CONFIG

class MujDialog(QtWidgets.QDialog,Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.v='~~~'
        self.comboBox.addItem('XYZ     ')
        self.comboBox_2.addItem('Sokkia SDR')

        self.toolButton.clicked.connect(self.souradnice)
        self.toolButton_2.clicked.connect(self.mereni)

        self.show()
        self.exec()

    def accept(self):
        nazev=self.textEdit.toPlainText()
        print(nazev)
        #======================================================================#
        databaze = Databaze()
        databaze.vytvoreni(nazev)
        databaze.vytvor_tabulku(DB_CONFIG["tabulka_souradnic"], DB_CONFIG["schema_tabulky_souradnic"])
        databaze.vytvor_tabulku(DB_CONFIG["tabulka_mereni"], DB_CONFIG["schema_tabulky_mereni"])
        databaze.importuj_sour(str(self.cesta_souradnice[0]))
        databaze.importuj_mereni(str(self.cesta_mereni[0]))
        self.close()

    def souradnice(self):
        self.cesta_souradnice=QFileDialog.getOpenFileName()
        print(self.cesta_souradnice[0])

        okno.label_cesta.setText('{} {} {}'.format(self.v,str(self.cesta_souradnice[0]),self.v))

    def mereni(self):
        self.cesta_mereni=QFileDialog.getOpenFileName()
        print(self.cesta_mereni[0])
        okno.label_mereni.setText('{} {} {}'.format(self.v,str(self.cesta_mereni[0]),self.v))

if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    okno=MujDialog()
    okno.toolButton.clicked.connect(okno.souradnice)
    okno.toolButton_2.clicked.connect(okno.mereni)

    okno.show()
    app.exec()
