from PyQt5 import QtWidgets, uic,QtSql,QtCore
from protinani_del_1 import Ui_Dialog
import sqlite3 as sql
from vypocet import vypocty
from data import Databaze
from PyQt5.QtWidgets import QFileDialog
from cesta import path
import math

class Protinani_delky(QtWidgets.QDialog,Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Vypocet.clicked.connect(self.vypocet)

        self.show()
        self.exec()

    def vypocet(self):
        # vypocte souradnice bodu urceneho protinanim
        # nacteni hodnot z okna
        bod1=self.bod1.toPlainText()
        bod2=self.bod1_2.toPlainText()
        del1=self.delka1.toPlainText()
        del2=self.delka2.toPlainText()
        cb=self.CB.toPlainText()

        # ziskani souradnic z databaze
        cesta_databaze=path.ziskej_cestu()
        bod1_sour=Databaze.sql_query(cesta_databaze[0],'select X, Y from gps_sour where CB = " {} "'.format(bod1))
        bod2_sour=Databaze.sql_query(cesta_databaze[0],'select X, Y from gps_sour where CB = " {} "'.format(bod2))

        # vypocet protinani
        bod1v=[bod1_sour[0][0], bod1_sour[0][1]]
        bod2v=[bod2_sour[0][0], bod2_sour[0][1]]
        bod=vypocty.prot_delek(bod1v,bod2v,float(del1),float(del2))

        # zaokrouhleni souradnic
        X=vypocty.zaokrouhleni(bod[0],3)
        Y=vypocty.zaokrouhleni(bod[1],3)

        # vypsani souradnic do okna
        self.Xova.setText(str(X))
        self.Yova.setText(str(Y))



if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    okno_delky=Protinani_delky()
    okno_delky.show()
    app.exec()
