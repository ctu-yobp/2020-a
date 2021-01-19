from PyQt5 import QtWidgets, uic,QtSql,QtCore
from delka_smernik import Ui_Smernikadelka
import sqlite3 as sql
from vypocet import vypocty
from data import Databaze
from PyQt5.QtWidgets import QFileDialog
from cesta import path

class Smernikadelka(QtWidgets.QDialog,Ui_Smernikadelka):

    def __init__(self, cesta_projektu):
        super().__init__()
        self.setupUi(self)
        self.cesta=cesta_projektu


        self.uloz_protokol_2.clicked.connect(self.vypocet) #kliknuti na vypocet
        self.uloz_protokol.clicked.connect(self.protokol) #kliknuta na ulozeni protokolu

        self.show()
        self.exec()


    def vypocet(self):
        # vezme cisla bodu
        print("*******************************************")
        print("Delka a smernik")
        self.stanovisko=self.textEdit.toPlainText() # stanovisko
        self.cil=self.textEdit_2.toPlainText() # cil

        print("Z bodu: {}".format(self.cil))
        print("Na bod: {}".format(self.stanovisko))

        query1='select Y, X from gps_sour where CB is {}{}{}{}{} '.format('"',' ',str(self.stanovisko),' ','"')
        query2='select Y, X from gps_sour where CB is {}{}{}{}{} '.format('"',' ',str(self.cil),' ','"')

        bod1=Databaze.sql_query(self.cesta,query1)
        bod2=Databaze.sql_query(self.cesta,query2)

        try:
            #vypocet smerniku a delky
            self.delka=vypocty.delka(bod1,bod2)
            self.delka=vypocty.zaokrouhleni(self.delka,3)

            self.smernik=vypocty.smernik(bod1,bod2)
            self.smernik=vypocty.zaokrouhleni(self.smernik,4)

            # posle delku a smernik do oken
            self.textEdit_4.setText(str(self.delka))
            self.textEdit_3.setText(str(self.smernik))
        except IndexError:
            print("Body nejsou v seznamu souradnic!!")

    def protokol(self):
        # ulozi protokol o vypoctu
        cesta=QFileDialog.getSaveFileUrl()
        cesta=cesta[0].toString()
        cesta=cesta[8:]

        # vypsani protokolu
        protokol = open(cesta,'a')
        protokol.write("************************* \n")
        protokol.write("Vypocet smerniku a delky \n")
        protokol.write("Stanovisko: {} \n".format(self.stanovisko))
        protokol.write("Cil: {} \n".format(self.cil))
        protokol.write("Delka: {} m \n".format(self.delka))
        protokol.write("Smernik: {} g \n".format(self.smernik))
        protokol.write("************************* \n")
        protokol.close()

        print("Protokol ulozen!!")



if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    okno=Smernikadelka()
    okno.show()
    app.exec()
