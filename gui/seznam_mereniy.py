# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seznam_merenii.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(844, 777)
        self.tabulka_mereni = QtWidgets.QColumnView(Dialog)
        self.tabulka_mereni.setGeometry(QtCore.QRect(10, 10, 821, 761))
        self.tabulka_mereni.setObjectName("tabulka_mereni")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
