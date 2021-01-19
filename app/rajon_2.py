from PyQt5 import QtWidgets, uic,QtSql,QtCore
from rajon_1 import Ui_Dialog
import sqlite3 as sql
from vypocet import vypocty
from data import Databaze
from PyQt5.QtWidgets import QFileDialog
from cesta import path
import math

class Rajon(QtWidgets.QDialog,Ui_Dialog):

    def __init__(self,cesta_projektu):
        super().__init__()
        self.setupUi(self)
        self.cesta=cesta_projektu

        self.vypocet.clicked.connect(self.vypocet_rajonu)
        self.uloz_bod.clicked.connect(self.ulozeni_rajonu)
        self.protokol.clicked.connect(self.protokol_rajon)

        self.show()
        self.exec()

    def vypocet_rajonu(self):
        # vypocet rajonu
        print("*******************************************")
        print("Vypocet rajonu")

        # vezme hodnoty z textEdit
        self.stan = self.stanovisko.toPlainText()
        self.ori = self.orientace.toPlainText()
        self.bod = self.merenybod.toPlainText()

        #tahani dat z databaze
        query_stanovisko = 'select * from gps_sour where CB is " {} "'.format(self.stan)
        query_orientace = 'select * from gps_sour where CB is " {} "'.format(self.ori)
        query_bod = 'select * from mereni where Orientace is " {} " and Stanovisko is " {} "'.format(self.bod,self.stan)
        query_mereni_orientace = 'select * from mereni where Orientace is " {} " and Stanovisko is " {} "'.format(self.ori,self.stan)
        self.stanovisko_data = Databaze.sql_query(self.cesta,query_stanovisko)
        self.orientace_data = Databaze.sql_query(self.cesta,query_orientace)
        self.bod_data = Databaze.sql_query(self.cesta,query_bod)
        self.mereni_orientace = Databaze.sql_query(self.cesta,query_mereni_orientace)

        try:
            # priprava slovniku pro vypocet rajonu
            b_ori={5001:{'x': self.orientace_data[0][3], 'y': self.orientace_data[0][2], 'smer': self.mereni_orientace[0][5]}}
            b_sta={'X': self.stanovisko_data[0][3], 'Y': self.stanovisko_data[0][2]}
            b_mer={5003:{'delka': self.bod_data[0][3]*math.sin(self.bod_data[0][4]*math.pi/200), 'smer': self.bod_data[0][5]}}

            # vypocet rajonu
            rajon=vypocty.rajon(b_ori,b_sta,b_mer)

            # vypsani souradnic rajonu
            self.souradniceX=vypocty.zaokrouhleni(rajon[5003]['x'],3)
            self.souradniceY=vypocty.zaokrouhleni(rajon[5003]['y'],3)
            self.X.setText(str(self.souradniceX))
            self.Y.setText(str(self.souradniceY))

        except IndexError:
            print("Data nejsou soucasti projektu!!")

    def ulozeni_rajonu(self):
        # ulozi souradnice spocitaneho rajonu
        try:
            query='insert into gps_sour (CB, Y, X, kod) values (" {} ", {}, {}," {} ")'.format(self.bod, self.souradniceY, self.souradniceX, self.bod_data[0][6])
            Databaze.pridani_bodu(self.cesta, query)
            print("Bod ulozen!!")
        except IndexError:
            print("Bod neni spocitan!!")

    def protokol_rajon(self):
        # ulozi protokol o vypoctu
        cesta=QFileDialog.getSaveFileUrl()
        cesta=cesta[0].toString()
        cesta=cesta[8:]

        try:
            # vypsani protokolu
            protokol = open(cesta,'a')
            protokol.write("************************* \n")
            protokol.write("Vypocet rajonu \n")
            protokol.write("Stanovisko: {} \n".format(self.stan))
            protokol.write("Orientace: {} \n".format(self.ori))
            protokol.write("Vysledny bod: \n")
            protokol.write("CB: {} \n".format(self.bod))
            protokol.write("Souradnice X: {} \n".format(str(self.souradniceX)))
            protokol.write("Souradnice Y: {} \n".format(str(self.souradniceY)))
            protokol.write("************************* \n")
            protokol.close()

            print("Protokol ulozen!!")

        except AttributeError:
            print("Uloha neni spocitana!!")




if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    okno=Rajon()
    okno.show()
    app.exec()
