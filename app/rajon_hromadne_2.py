from PyQt5.QtWidgets import QFileDialog
from rajon_hromadne_1 import Rajon_hromadne
from PyQt5 import QtWidgets, uic,QtSql,QtCore
from vypocet import vypocty

class Rajon_hromadne(QtWidgets.QDialog,Rajon_hromadne):

    def __init__(self,cesta_projektu):
        super().__init__()
        self.setupUi(self)
        self.cesta=cesta_projektu

        self.Vypocet.clicked.connect(self.vypocet)
        self.protokol.clicked.connect(self.protokol_rajon_hrom)

        self.show()
        self.exec()

    def vypocet(self):
        print("*******************************************")
        self.stan=self.stanovisko.toPlainText()
        self.ori=self.orientace.toPlainText()

        self.pocet_bodu=vypocty.davka(self.cesta,self.stan,self.ori)
        print("Spocteno {} bodu".format(str(self.pocet_bodu)))

    def protokol_rajon_hrom(self):
        # ulozi protokol o vypoctu
        cesta=QFileDialog.getSaveFileUrl()
        cesta=cesta[0].toString()
        cesta=cesta[8:]

        # vypsani protokolu
        protokol = open(cesta,'a')
        protokol.write("************************* \n")
        protokol.write("Vypocet rajonu hromadne \n")
        protokol.write("Stanovisko: {} \n".format(self.stan))
        protokol.write("Cil: {} \n".format(self.ori))
        protokol.write("Pocet spoctenych bodu: {} \n".format(str(self.pocet_bodu)))
        protokol.write("************************* \n")
        protokol.close()

        print("Protokol ulozen!!")






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Rajon_hromadne()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
