import os
import sys
from PyQt5 import QtWidgets, uic,QtSql,QtCore,QtGui
from PyQt5.QtWidgets import QFileDialog
from cesta import pozdrav,path
from data import Databaze
from main_1 import Ui_MainWindow
from okno_import_2 import MujDialog
from seznam_souradnic_2 import Seznam
from smernikadelka import Smernikadelka
from seznam_mereni_2 import Seznam_mereni
from rajon_2 import Rajon
import matplotlib.pyplot as plt
from protinani_del_2 import Protinani_delky

class Uvod(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        pozdrav()

        self.menuImport.addAction('Projekt') #pridani tlacitka na zalozeni projektu

        self.menuImport.triggered.connect(self.pozdrav) #odkaze na zlozeni projektu
        self.rajon.triggered.connect(self.rajon1) #odkaze na tlacitko rajon
        self.smernikdelka.triggered.connect(self.smernikdelka1) #odkaze na tlacitko smernik a delka
        self.souradnice.triggered.connect(self.seznam_souradnic) #odkaze na tlacitko otevreni seznamu souradnic
        self.mereni.triggered.connect(self.seznam_mereni) #odkaze na tlacitko otevreni seznamu mereni
        self.protinani_delky.triggered.connect(self.protinani_del) #odkaze na tlacitko vypoctu protinani z delek
        self.info.triggered.connect(self.info_projekt) # odkaze na tlacitko informace o projektu
        self.o_aplikaci.triggered.connect(self.info_projekt1) # odkaze na tlacitko informace o projektu
        self.otevri.triggered.connect(self.otevri_projekt) # odkaze na tlacitko otevreni projektu
        self.zavri.triggered.connect(self.zavri_projekt) # odkaze na tlacitko zavreni projektu
        self.grafika.triggered.connect(self.zobraz_grafiku) # odkaze na tlacitko otevreni grafiky

    def seznam_souradnic(self):
        # otevreni seznamu souradnic
        # #nacte pozici databaze ze souboru "nazev.txt"
        cesta=path.ziskej_cestu()

        print("*******************************************")
        print("Otevren seznam souradnic")

        okno=Seznam(cesta[0])


    def seznam_mereni(self):
        # otevreni seznamu mereni
        # #nacte pozici databaze ze souboru "nazev.txt"
        cesta=path.ziskej_cestu()

        print("*******************************************")
        print("Otevren seznam mereni")

        okno1=Seznam_mereni(cesta[0])


    def pozdrav(self):
        # otevre okno zaloz projekt
        print("*******************************************")
        print("Zalozeni noveho projektu")

        okno1 = MujDialog()


    def rajon1(self):
        # otevre oknoo vypocet rajonu
        print("*******************************************")
        print("Vypocet rajonu")

        okno_rajon=Rajon()


    def smernikdelka1(self):
        # otevre okno vypoctu smernik a delka
        print("*******************************************")
        print("Vypocet smerniku a delky")

        okno=Smernikadelka()

    def protinani_del(self):
        # otevre okno pro vypocet protinani z delek
        print("*******************************************")
        print("Vypocet protinani z delek")

        okno_delky=Protinani_delky()

    def info_projekt(self):
        # vypise info o zalozenem projektu
        # nacte nazev databaze
        cesta=path.ziskej_cestu()

        #ziskani informaci z databaze
        info=Databaze.sql_query(cesta[0],'select * from projekt')
        pocet_stanovisek=Databaze.sql_query(cesta[0],'SELECT count(distinct Stanovisko) from mereni group by Stanovisko')

        # vypis infa do terminalu
        print("*******************************************")
        print("Pocet bodu z GPS:       {}".format(info[0][2]))
        print("Pocet bodu v zapisniku: {}".format(info[0][3]))
        print("Pocet stanovisek:       {}".format(pocet_stanovisek[0][0]))

    def info_projekt1(self):
        # vypise do terminalo informace o aplikaci
        print("*******************************************")
        print("Aplikace byla vytvorena v ramci predmetu 155YOBP - Objektove programovani na CVUT FSv")
        print("Vytvorili:")
        print("Pane Kuzmanov - pane.kuzmanov@fsv.cvut.cz")
        print("Jan Kucera    - jan.kucera.1@fsv.cvut.cz")
        print("Jakub Simek   - jakub.simek@fsv.cvut.cz")
        print("V Praze, leden 2021")

    def otevri_projekt(self):
        # otevreni noveho projektu
        print("*******************************************")
        print("Otevreni noveho projektu")

        # otevre okno pro ukazani na projekt
        self.cesta_projekt=QFileDialog.getOpenFileName()
        print(self.cesta_projekt[0])

        # zapise cestu k projektu do souboru "nazev.txt"
        path.zapis_cestu(self.cesta_projekt[0])

        # otevre okna
        okno_mereni=Seznam_mereni(self.cesta_projekt[0])
        okno_souradnice=Seznam(self.cesta_projekt[0])

    def zavri_projekt(self):
        # vymaze z "nazev.txt" cestu k projektu
        path.zapis_cestu("")

    def zobraz_grafiku(self):
        # ukaze graficky souradnice
        query="select Y, X, CB from gps_sour"
        cesta=path.ziskej_cestu()
        sour=Databaze.sql_query(cesta[0],query)

        y=[]
        x=[]
        for i in range(0,len(sour)):
            Y=-sour[i][0]
            X=-sour[i][1]
            y.append(Y)
            x.append(X)
            plt.text(Y,X,sour[i][2])

        plt.plot(y,x,'+')
        plt.show()




if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    hlavni_okno=Uvod()
    hlavni_okno.show()
    app.exec_()
