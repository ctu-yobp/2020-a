import os
import sys
from PyQt5 import QtWidgets, uic,QtSql,QtCore,QtGui
from PyQt5.QtWidgets import QFileDialog
from data import Databaze
from main_1 import Ui_MainWindow

class Uvod(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def pozdrav(self):
        from okno_import_2 import MujDialog
        # print('jde to')


app=QtWidgets.QApplication([])
hlavni_okno=Uvod()
hlavni_okno.menuImport.addAction('Projekt')
hlavni_okno.menuImport.triggered.connect(hlavni_okno.pozdrav)
hlavni_okno.show()
app.exec()







    # app = QtWidgets.QApplication(sys.argv)
# window = uic.loadUi(os.path.join(os.path.dirname(__file__), "seznam_mereni.ui"))

# window.show()



# window.comboBox.addItems(['CB, X, Y, Z, kód - csv'])
# window.comboBox_2.addItems(['Sokkia - sdr'])
