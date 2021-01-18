from seznam_mereni_1 import Ui_Dialog
from PyQt5 import QtWidgets, uic,QtSql,QtCore,QtGui
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel
import sqlite3 as sql
import sys
from data import Databaze

class Seznam_mereni(QtWidgets.QDialog,Ui_Dialog):

    def __init__(self, cesta_nazvu):
        super().__init__()
        self.setupUi(self)
        self.cesta_nazvu=cesta_nazvu



        # # nacte nazev aktualniho projektu ze souboru "nazev.txt"
        # with open(cesta_nazvu) as n:
        #     nazev=n.readlines()
        #
        # nazev=nazev[0]
        # cesta_inv=cesta_nazvu[::-1] #invertuje cestu
        # pozice=cesta_inv.find('/') #najde poradi lomitka
        # cesta_konecna=cesta_nazvu[0:len(cesta_nazvu)-pozice] #udela cestu adresare bez nazvu souboru
        #
        # databaze=cesta_konecna+nazev #vytvori cestu+nazev databaze



        #otevreni databaze
        db1 = QSqlDatabase.addDatabase("QSQLITE","db1")
        # db = QSqlDatabase.addDatabase("")
        db1.setDatabaseName(cesta_nazvu)
        db1.open()

        # vytvori model databaza a nacte data
        projectModel1 = QSqlQueryModel()
        # projectModel.setQuery('select Stanovisko,Orientace, Delka,Zenitka, Smer, Kod from gps_sour',db)
        projectModel1.setQuery('select Stanovisko,Orientace,Delka,Zenitka,Smer, Kod from mereni',db1)
        self.tableView.setModel(projectModel1)
        # self.tableView.setColumnWidth(1,5)

        db1.close()
        del projectModel1
        del db1

        QSqlDatabase.removeDatabase("db1")
        self.show()
        self.exec()

if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    okno=Seznam_mereni()
    okno.show()
    sys.exit(app.exec_())
