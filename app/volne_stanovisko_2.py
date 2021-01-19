from volne_stanovisko_1 import Ui_Dialog
from PyQt5 import QtWidgets, uic,QtSql,QtCore
from data import Databaze
import math
from vypocet import vypocty
from PyQt5.QtWidgets import QFileDialog

class Volnestanovisko(QtWidgets.QDialog,Ui_Dialog):

    def __init__(self,cesta_projektu):
        super().__init__()
        self.setupUi(self)
        self.cesta=cesta_projektu

        self.Vypocet.clicked.connect(self.vypocet)
        self.uloz.clicked.connect(self.ulozeni_stanoviska)
        self.protokol.clicked.connect(self.ulozeni_protokolu)

        self.show()
        self.exec()

    def vypocet(self):
        # vypocet volneho stanoviska
        # cisla bodu z grafickeho rozhrani
        self.ori1=self.orientace1.toPlainText()
        self.ori2=self.orientace2.toPlainText()
        self.stan=self.CB.toPlainText()

        # priprava sql prikazu
        query1='select X, Y from gps_sour where CB is " {} "'.format(str(self.ori1))
        query2='select X, Y from gps_sour where CB is " {} "'.format(str(self.ori2))
        query_stan1='select Delka, Zenitka, Smer from mereni where Stanovisko is " {} " and Orientace is " {} "'.format(str(self.stan),str(self.ori1))
        query_stan2='select Delka, Zenitka, Smer from mereni where Stanovisko is " {} " and Orientace is " {} "'.format(str(self.stan),str(self.ori2))

        #tahani dat z databaze

        ori1_sour=Databaze.sql_query(self.cesta,query1)
        ori2_sour=Databaze.sql_query(self.cesta,query2)
        ori1_mer=Databaze.sql_query(self.cesta,query_stan1)
        ori2_mer=Databaze.sql_query(self.cesta,query_stan2)

        try:
            # vypocet volneho stanoviska
            data = {503: {'x': ori1_sour[0][0], 'y': ori1_sour[0][1], 'delka': ori1_mer[0][0]*math.sin(ori1_mer[0][1]), 'smer': ori1_mer[0][2]}, 504: {'x': ori2_sour[0][0], 'y': ori2_sour[0][1], 'delka':  ori2_mer[0][0]*math.sin(ori2_mer[0][1]), 'smer': ori2_mer[0][2]}}
            stanovisko=vypocty.vyp_stanovisko(data)
            self.X=vypocty.zaokrouhleni(stanovisko['X'],3)
            self.Y=vypocty.zaokrouhleni(stanovisko['Y'],3)

            # ukazani vyslednych souradnic do graf. rozhrani
            self.Xova.setText(str(self.X))
            self.Yova.setText(str(self.Y))
        except IndexError:
            print("Data nejsou soucasti projektu!!")

    def ulozeni_stanoviska(self):
        # ulozi vysledne souradnice do projektu

        query_pridani='insert into gps_sour (CB, X ,Y ) values (" {} ",{},{})'.format(self.stan,self.X,self.Y)
        Databaze.pridani_bodu(self.cesta,query_pridani)
        print("Bod ulozen!!")

    def ulozeni_protokolu(self):
        # ulozi protokol o vypoctu
        cesta_protokol=QFileDialog.getSaveFileUrl()
        cesta_protokol=cesta_protokol[0].toString()
        cesta_protokol=cesta_protokol[8:]

        # vypsani protokolu
        protokol = open(cesta_protokol,'a')
        protokol.write("************************* \n")
        protokol.write("Vypocet volneho stanoviska \n")
        protokol.write("Orientace 1: {} \n".format(self.ori1))
        protokol.write("Orientace 2: {} \n".format(self.ori2))
        protokol.write("Stanovisko: \n")
        protokol.write("CB: {} \n".format(self.stan))
        protokol.write("Souradnice X: {} m \n".format(self.X))
        protokol.write("Souradnice Y: {} m \n".format(self.Y))
        protokol.write("************************* \n")
        protokol.close()

        print("Protokol ulozen!!")






if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    okno=Volnestanovisko()
    okno.show()
    app.exec()
