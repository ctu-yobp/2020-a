# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'okno.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("GeoApp")
        MainWindow.resize(979, 706)
        MainWindow.setWindowIcon(QtGui.QIcon('foto.jpg'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 979, 26))
        self.menubar.setObjectName("menubar")
        self.menuSoubor = QtWidgets.QMenu(self.menubar)
        self.menuSoubor.setObjectName("menuSoubor")
        self.menuImport = QtWidgets.QMenu(self.menuSoubor)
        self.menuImport.setObjectName("menuImport")
        self.menuV_po_ty = QtWidgets.QMenu(self.menubar)
        self.menuV_po_ty.setObjectName("menuV_po_ty")

        self.menuData = QtWidgets.QMenu(self.menubar)#
        self.menuData.setObjectName("Data")#

        self.menuO = QtWidgets.QMenu(self.menubar)
        self.menuO.setObjectName("o_aplikaci")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.importSDR = QtWidgets.QAction(MainWindow)
        self.importSDR.setObjectName("importSDR")
        self.importTXT = QtWidgets.QAction(MainWindow)
        self.importTXT.setObjectName("importTXT")
        self.rajon = QtWidgets.QAction(MainWindow)
        self.rajon.setObjectName("rajon")
        self.protinani_delky = QtWidgets.QAction(MainWindow)
        self.protinani_delky.setObjectName("protinani_delky")

        self.souradnice = QtWidgets.QAction(MainWindow)#
        self.souradnice.setObjectName("soubor")#

        self.mereni=QtWidgets.QAction(MainWindow)
        self.mereni.setObjectName("mereni")

        self.info=QtWidgets.QAction(MainWindow)
        self.info.setObjectName("info")

        self.o_aplikaci = QtWidgets.QAction(MainWindow)
        self.o_aplikaci.setObjectName("infoA")

        self.smernikdelka = QtWidgets.QAction(MainWindow)
        self.smernikdelka.setObjectName("smernikdelka")

        self.otevri = QtWidgets.QAction(MainWindow)
        self.otevri.setObjectName("otevri")

        self.zavri = QtWidgets.QAction(MainWindow)
        self.zavri.setObjectName("zavri")

        self.grafika = QtWidgets.QAction(MainWindow)
        self.grafika.setObjectName("grafika")

        self.exportSour = QtWidgets.QAction(MainWindow)
        self.exportSour.setObjectName("exportSour")

        self.volneStanovisko = QtWidgets.QAction(MainWindow)
        self.volneStanovisko.setObjectName("volneStanovisko")

        self.rajon_hromadne=QtWidgets.QAction(MainWindow)
        self.rajon_hromadne.setObjectName("rajon_hromadne")


        self.menuSoubor.addAction(self.menuImport.menuAction())
        self.menuData.addAction(self.souradnice)#
        self.menuData.addAction(self.mereni)
        self.menuData.addAction(self.grafika)
        self.menuData.addAction(self.info)
        self.menuSoubor.addAction(self.otevri)
        self.menuSoubor.addAction(self.exportSour)
        self.menuSoubor.addAction(self.zavri)


        self.menuO.addAction(self.o_aplikaci)

        self.menuV_po_ty.addAction(self.rajon)
        self.menuV_po_ty.addAction(self.rajon_hromadne)
        self.menuV_po_ty.addAction(self.smernikdelka)
        self.menuV_po_ty.addAction(self.protinani_delky)
        self.menuV_po_ty.addAction(self.volneStanovisko)
        self.menubar.addAction(self.menuSoubor.menuAction())
        self.menubar.addAction(self.menuV_po_ty.menuAction())
        self.menubar.addAction(self.menuData.menuAction())#
        self.menubar.addAction(self.menuO.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #cesta k souboru souradnic


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("GeoApp", "GeoApp"))
        self.menuSoubor.setTitle(_translate("GeoApp", "Soubor"))
        self.menuImport.setTitle(_translate("GeoApp", "Nový"))
        self.menuV_po_ty.setTitle(_translate("GeoApp", "Výpočty"))

        self.menuData.setTitle(_translate("GeoApp", "Data"))#
        self.menuO.setTitle(_translate("GeoApp","O aplikaci"))

        self.importSDR.setText(_translate("GeoApp", "Měření \'.sdr\'"))
        self.importTXT.setText(_translate("GeoApp", "Souřadnice \'.txt\'"))
        self.rajon.setText(_translate("GeoApp", "Rajón"))
        self.smernikdelka.setText(_translate("GeoApp", "Délka a směrník"))
        self.souradnice.setText(_translate("GeoApp","Seznam souřadnic"))#
        self.mereni.setText(_translate("GeoApp","Seznam měření"))
        self.protinani_delky.setText(_translate("GeoApp", "Protínání z délek"))
        self.o_aplikaci.setText(_translate("GeoApp","Informace o aplikaci"))
        self.otevri.setText(_translate("GeoApp","Otevři projekt"))
        self.info.setText(_translate("GeoApp",'Info o projektu'))
        self.zavri.setText(_translate("GeoApp", "Zavři projekt"))
        self.grafika.setText(_translate("GeoApp", "Grafika"))
        self.exportSour.setText(_translate("GeoApp", "Export seznamu souradnic"))
        self.volneStanovisko.setText(_translate("GeoApp", "Volné stanovisko"))
        self.rajon_hromadne.setText(_translate("GeoApp", "Rajón hromadně"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
