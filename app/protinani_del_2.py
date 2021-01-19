from PyQt5 import QtWidgets, uic,QtSql,QtCore
from protinani_del_1 import Ui_Dialog
import sqlite3 as sql
from vypocet import vypocty
from data import Databaze
from PyQt5.QtWidgets import QFileDialog
from cesta import path
import math

class Protinani_delky(QtWidgets.QDialog,Ui_Dialog):

    def __init__(self,cesta_projektu):
        super().__init__()
        self.setupUi(self)
        self.cesta=cesta_projektu

        self.Vypocet.clicked.connect(self.vypocet)
        self.uloz.clicked.connect(self.uloz_bod)
        self.protokol.clicked.connect(self.protokol_protinani)

        self.show()
        self.exec()

    def vypocet(self):
        # vypocte souradnice bodu urceneho protinanim
        # nacteni hodnot z okna
        self.bod1=self.bod1.toPlainText()
        self.bod2=self.bod1_2.toPlainText()
        self.del1=self.delka1.toPlainText()
        self.del2=self.delka2.toPlainText()
        self.cb=self.CB.toPlainText()

        # ziskani souradnic z databaze
        # cesta_databaze=path.ziskej_cestu()
        bod1_sour=Databaze.sql_query(self.cesta,'select X, Y from gps_sour where CB = " {} "'.format(self.bod1))
        bod2_sour=Databaze.sql_query(self.cesta,'select X, Y from gps_sour where CB = " {} "'.format(self.bod2))

        # vypocet protinani


        try:
            bod1v=[bod1_sour[0][0], bod1_sour[0][1]]
            bod2v=[bod2_sour[0][0], bod2_sour[0][1]]\

            bod=vypocty.prot_delek(bod1v,bod2v,float(self.del1),float(self.del2))

            # zaokrouhleni souradnic
            self.X=vypocty.zaokrouhleni(bod[0],3)
            self.Y=vypocty.zaokrouhleni(bod[1],3)

            # vypsani souradnic do okna
            self.Xova.setText(str(self.X))
            self.Yova.setText(str(self.Y))

        except ValueError:
            print("Nedodrzena trojuhelnikova nerovnost")

        except IndexError:
            print("Body nejsou v seznamu souradnic!!")

    def uloz_bod(self):
        # ulozeni vypocteneho bodu do seznamu souradnic
        try:
            query='insert into gps_sour (CB, Y, X) values ({}, {}, {})'.format(self.cb, self.Y, self.X)
            Databaze.pridani_bodu(self.cesta, query)
            print("Bod ulozen")
        except sql.OperationalError:
            print("Neni spocitan bod nebo neni vyplneno cislo bodu!!")

    def protokol_protinani(self):
        # ulozi protokol o vypoctu
        cesta=QFileDialog.getSaveFileUrl()
        cesta=cesta[0].toString()
        cesta=cesta[8:]

        # vypsani protokolu
        protokol = open(cesta,'a')
        protokol.write("************************* \n")
        protokol.write("Vypocet protinani z delek \n")
        protokol.write("Bod 1: {} \n".format(self.bod1))
        protokol.write("Bod 2: {} \n".format(self.bod2))
        protokol.write("Delka 1: {} m \n".format(self.del1))
        protokol.write("Delka 2: {} g \n".format(self.del2))
        protokol.write("Vysledny bod: \n")
        protokol.write("CB: {} \n".format(self.cb))
        protokol.write("Souradnice X: {} \n".format(str(self.X)))
        protokol.write("Souradnice Y: {} \n".format(str(self.Y)))
        protokol.write("************************* \n")
        protokol.close()

        print("Protokol ulozen!!")




if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    okno_delky=Protinani_delky()
    okno_delky.show()
    app.exec()
