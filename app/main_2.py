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
from protinani_del_2 import Protinani_delky
from grafika import Grafika
from volne_stanovisko_2 import Volnestanovisko
from rajon_hromadne_2 import Rajon_hromadne


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
        self.exportSour.triggered.connect(self.exportSouradnic) # odkaze na tlacitko exportu souradnic
        self.volneStanovisko.triggered.connect(self.volneStan)
        self.rajon_hromadne.triggered.connect(self.rajon_hrom)

    def seznam_souradnic(self):
        # otevreni seznamu souradnic

        print("*******************************************")


        try:
            okno=Seznam(self.cesta_projektu[0])
            print("Otevren seznam souradnic")
        except AttributeError:
            print("Neni aktivni projekt!")


    def seznam_mereni(self):
        # otevreni seznamu mereni

        print("*******************************************")


        try:
            okno1=Seznam_mereni(self.cesta_projektu[0])
            print("Otevren seznam mereni")
        except AttributeError:
            print("Neni aktivni projekt!!")


    def pozdrav(self):
        # otevre okno zaloz projekt
        print("*******************************************")
        print("Zalozeni noveho projektu")

        okno1 = MujDialog()
        self.cesta_projektu=okno1.global_cesta


    def rajon1(self):
        # otevre oknoo vypocet rajonu
        print("*******************************************")
        print("Vypocet rajonu")

        try:
            okno_rajon=Rajon(self.cesta_projektu[0])
        except AttributeError:
            print("Neni aktivni projekt!!")


    def smernikdelka1(self):
        # otevre okno vypoctu smernik a delka
        print("*******************************************")
        print("Vypocet smerniku a delky")

        try:
            okno=Smernikadelka(self.cesta_projektu[0])
        except AttributeError:
            print("Neni aktivni projekt!!")

    def protinani_del(self):
        # otevre okno pro vypocet protinani z delek
        print("*******************************************")
        print("Vypocet protinani z delek")

        try:
            okno_delky=Protinani_delky(self.cesta_projektu[0])
        except AttributeError:
            print("Neni aktivni projekt!!")

    def info_projekt(self):
        # vypise info o zalozenem projektu

        #ziskani informaci z databaze
        try:
            info=Databaze.sql_query(self.cesta_projektu[0],'select * from projekt')
            pocet_stanovisek=Databaze.sql_query(self.cesta_projektu[0],'SELECT count(distinct Stanovisko) from mereni group by Stanovisko')

            # vypis infa do terminalu
            print("*******************************************")
            print("Aktivni projekt: {}".format(self.cesta_projektu[0]))
            print("Pocet bodu z GPS:       {}".format(info[0][2]))
            print("Pocet bodu v zapisniku: {}".format(info[0][3]))
            print("Pocet stanovisek:       {}".format(pocet_stanovisek[0][0]))

        except AttributeError:
            print("Neni aktivni projekt!!")

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
        self.cesta_projektu=QFileDialog.getOpenFileName(None,None,None,'DB(*.db)')

        # otevre okna
        # okno_mereni=Seznam_mereni(self.cesta_projektu[0])
        # okno_souradnice=Seznam(self.cesta_projektu[0])

    def zavri_projekt(self):
        # zavre aktualni projekt
        try:
            del self.cesta_projektu
        except:
            print("Neni co zavrit!!")

    def zobraz_grafiku(self):
        # ukaze graficky souradnice
        print("*******************************************")
        try:
            okno_grafika=Grafika(self.cesta_projektu[0])
            print("Grafika otevrena!!")
        except AttributeError:
            print("Neni aktivni projekt!!")

    def exportSouradnic(self):
        # export senamu souradnic
        cesta_export=QFileDialog.getSaveFileUrl()
        cesta_export=cesta_export[0].toString()
        cesta_export=cesta_export[8:]

        Databaze.export2txt(self.cesta_projektu[0],cesta_export)
        print("Seznam souradnic ulozen!!")

    def volneStan(self):
        # otevreni okna pro vypocet volneho stanoviska
        okno_stanovisko=Volnestanovisko(self.cesta_projektu[0])

    def rajon_hrom(self):

        try:
            okno_rajon_hrom=Rajon_hromadne(self.cesta_projektu[0])
            print('Body spocteny a ulozeny')
        except AttributeError:
            print("Neni aktivni projekt!!")



if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    hlavni_okno=Uvod()
    hlavni_okno.show()
    app.exec_()
