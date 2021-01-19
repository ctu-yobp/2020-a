from seznam_souradnic import Ui_Seznam
from PyQt5 import QtWidgets, uic,QtSql,QtCore,QtGui
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel
import sqlite3 as sql
import sys
from data import Databaze

class Seznam(QtWidgets.QDialog,Ui_Seznam):

    def __init__(self, cesta_nazvu):
        super().__init__()
        self.setupUi(self)
        self.cesta_nazvu=cesta_nazvu

        #otevreni databaze
        db = QSqlDatabase.addDatabase("QSQLITE","db")
        db.setDatabaseName(cesta_nazvu)
        db.open()

        # vytvori model databaza a nacte data
        projectModel = QSqlQueryModel()
        projectModel.setQuery('select cb,X,Y,Z,kod from gps_sour',db)
        # projectModel.setQuery('select Stanovisko,Orientace,Delka,Zenitka,Smer, Kod from mereni',db)
        self.columnView.setModel(projectModel)
        self.columnView.setColumnWidth(0,1)

        db.close()
        del db
        del projectModel

        QSqlDatabase.removeDatabase("db")
        self.show()
        self.exec()


if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    okno=Seznam()
    okno.show()
    sys.exit(app.exec_())



# app=QtWidgets.QApplication([])
# seznam_souradnic=Seznam()
# header=['X','Y','Z','kod']
#
# db = QSqlDatabase.addDatabase("QSQLITE")
# db.setDatabaseName('PESL1120.db')
# db.open()
# projectModel = QSqlQueryModel()
# projectModel.setQuery('select cb,X,Y,Z,kod from gps_sour',db)
#
#
#
#
# # tablemodel=MyTableModel(radky,header)
#

#
# # seznam_souradnic.columnView.setColumnWidth(3,50)
# # seznam_souradnic.columnView.setColumnWidth(3,5)
# # seznam_souradnic.columnView.setColumnWidth(3,4)
# # seznam_souradnic.columnView.setColumnWidth(3,5)
#
# seznam_souradnic.show()
# app.exec()
