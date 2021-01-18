from PyQt5 import QtWidgets, uic,QtSql,QtCore
from delka_smernik import Ui_Smernikadelka
import sqlite3 as sql
from vypocet import vypocty
from data import Databaze
from PyQt5.QtWidgets import QFileDialog
from cesta import path

class Smernikadelka(QtWidgets.QDialog,Ui_Smernikadelka):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


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

        print(self.cil)
        print(self.stanovisko)

        # nacte ze souboru "nazev.txt" projektu
        with open("nazev.txt") as n:
            nazev=n.readlines()

        nazev=nazev[0]
        # databaze='{}.db'.format(nazev)
        self.databaze=nazev


        #pripojeni k databazi a vybrani souradnic
        con=sql.connect(self.databaze)
        query1='select Y, X from gps_sour where CB is {}{}{}{}{} '.format('"',' ',str(self.stanovisko),' ','"')
        query2='select Y, X from gps_sour where CB is {}{}{}{}{} '.format('"',' ',str(self.cil),' ','"')

        cur=con.cursor()

        cur.execute(query1)
        bod1=cur.fetchall()

        cur.execute(query2)
        bod2=cur.fetchall()


        print(bod1)
        print(bod2)
        con.commit()
        con.close()

        #vypocet smerniku a delky
        self.delka=vypocty.delka(bod1,bod2)
        self.delka=vypocty.zaokrouhleni(self.delka,3)

        self.smernik=vypocty.smernik(bod1,bod2)
        self.smernik=vypocty.zaokrouhleni(self.smernik,4)

        # posle delku a smernik do oken
        self.textEdit_4.setText(str(self.delka))
        self.textEdit_3.setText(str(self.smernik))

    def protokol(self):

        slozka=path.ubrani_souboru(self.databaze)
        cesta_ulozeni = slozka+'protokol_smernikdelka{}_{}.txt'.format(self.stanovisko,self.cil)
        protokol = open(cesta_ulozeni,'a')
        protokol.write("************************* \n")
        protokol.write("Vypocet smerniku a delky \n")
        protokol.write("Stanovisko: {} \n".format(self.stanovisko))
        protokol.write("Cil: {} \n".format(self.cil))
        protokol.write("Delka: {} m \n".format(self.delka))
        protokol.write("Smernik: {} g \n".format(self.smernik))
        protokol.write("************************* \n")
        protokol.close()
        


if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    okno=Smernikadelka()
    okno.show()
    app.exec()
