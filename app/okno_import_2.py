import os
import sys
from PyQt5 import QtWidgets, uic,QtSql,QtCore
from PyQt5.QtWidgets import QFileDialog
from data import Databaze
from okno_import_1 import Ui_Dialog
from config import DB_CONFIG, DATA_CONFIG
from seznam_souradnic_2 import Seznam
from seznam_mereni_2 import Seznam_mereni



class MujDialog(QtWidgets.QDialog,Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.v='~~~'
        # moznosti importu do rolovacich menu
        self.comboBox.addItem('XYZ     ')
        self.comboBox_2.addItem('Sokkia SDR')

        #pri kliknuti na |***| otevre okno na ukazani cesty k souborum
        self.toolButton.clicked.connect(self.souradnice)
        self.toolButton_2.clicked.connect(self.mereni)

        self.show()
        self.exec()

    def accept(self):
        # kdyz se klikne na OK
        print("*******************************************")
        print("Projekt zalozen")
        nazev=self.textEdit.toPlainText() # vezme nazev souboru
        print(nazev)

        cesta=self.cesta_souradnice[0]
        cesta_inv=cesta[::-1]
        pozice=cesta_inv.find('/')
        cesta_konecna=cesta[0:len(cesta)-pozice]
        #======================================================================#
        #zalozeni databaze
        databaze = Databaze()
        databaze.vytvoreni(nazev,cesta_konecna)
        databaze.vytvor_tabulku(DB_CONFIG["tabulka_souradnic"], DB_CONFIG["schema_tabulky_souradnic"])
        databaze.vytvor_tabulku(DB_CONFIG["tabulka_mereni"], DB_CONFIG["schema_tabulky_mereni"])
        databaze.vytvor_tabulku(DB_CONFIG["tabulka_projekt"], DB_CONFIG["schema_projekt"])
        databaze.importuj_sour(str(self.cesta_souradnice[0]))
        databaze.importuj_mereni(str(self.cesta_mereni[0]))
        databaze.zapis_info(self.cesta_souradnice[0])


        # cesta_nazvu=cesta_konecna+'nazev.txt'
        # soubor=open(cesta_nazvu,"w")
        # soubor.write(nazev+'.db')
        # soubor.close()

        zapis=open("nazev.txt","w")
        f=str(cesta_konecna+nazev+'.db')
        zapis.write(f)
        print('Projekt ulozen do: '+cesta_konecna+nazev+'.db')
        zapis.close()

        self.close()

        okno_souradnice=Seznam(f)
        okno_mereni=Seznam_mereni(f)



    def souradnice(self):
        # otevreni okna na nalezeni seznamu souradnic
        print("*******************************************")
        print("Ukaz cestu souboru souradnic")
        self.cesta_souradnice=QFileDialog.getOpenFileName()
        # print('Projekt ulozen: {}'.format(self.cesta_souradnice[0]))

        # vytiskne cestu
        self.label_cesta.setText('{} {} {}'.format(self.v,str(self.cesta_souradnice[0]),self.v))

    def mereni(self):
        # otevreni okna na nalezeni zapisniku mereni
        print("*******************************************")
        print("Ukaz cestu souboru mereni")
        self.cesta_mereni=QFileDialog.getOpenFileName()
        # print(self.cesta_mereni[0])

        # vytiskne cestu
        self.label_mereni.setText('{} {} {}'.format(self.v,str(self.cesta_mereni[0]),self.v))


if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    okno1=MujDialog()
    # okno.toolButton.clicked.connect(okno.souradnice)
    # okno.toolButton_2.clicked.connect(okno.mereni)

    okno1.show()
    app.exec()
