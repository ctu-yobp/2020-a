# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prot_delky.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(559, 285)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(330, 230, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.bod1 = QtWidgets.QTextEdit(Dialog)
        self.bod1.setGeometry(QtCore.QRect(140, 30, 121, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bod1.setFont(font)
        self.bod1.setObjectName("bod1")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 30, 55, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 30, 55, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.bod1_2 = QtWidgets.QTextEdit(Dialog)
        self.bod1_2.setGeometry(QtCore.QRect(350, 30, 121, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bod1_2.setFont(font)
        self.bod1_2.setObjectName("bod1_2")
        self.delka2 = QtWidgets.QTextEdit(Dialog)
        self.delka2.setGeometry(QtCore.QRect(350, 70, 121, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delka2.setFont(font)
        self.delka2.setObjectName("delka2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 70, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(280, 70, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.delka1 = QtWidgets.QTextEdit(Dialog)
        self.delka1.setGeometry(QtCore.QRect(140, 70, 121, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delka1.setFont(font)
        self.delka1.setObjectName("delka1")
        self.CB = QtWidgets.QTextEdit(Dialog)
        self.CB.setGeometry(QtCore.QRect(280, 130, 121, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CB.setFont(font)
        self.CB.setObjectName("CB")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(240, 130, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Xova = QtWidgets.QTextEdit(Dialog)
        self.Xova.setGeometry(QtCore.QRect(140, 180, 121, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Xova.setFont(font)
        self.Xova.setObjectName("Xova")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(330, 180, 20, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.Yova = QtWidgets.QTextEdit(Dialog)
        self.Yova.setGeometry(QtCore.QRect(350, 180, 121, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Yova.setFont(font)
        self.Yova.setObjectName("Yova")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(120, 180, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.Vypocet = QtWidgets.QPushButton(Dialog)
        self.Vypocet.setGeometry(QtCore.QRect(210, 230, 93, 28))
        self.Vypocet.setObjectName("Vypocet")
        self.uloz = QtWidgets.QPushButton(Dialog)
        self.uloz.setGeometry(QtCore.QRect(110, 230, 93, 28))
        self.uloz.setObjectName("uloz")
        self.protokol = QtWidgets.QPushButton(Dialog)
        self.protokol.setGeometry(QtCore.QRect(10, 230, 93, 28))
        self.protokol.setObjectName("protokol")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Bod 1:"))
        self.label_2.setText(_translate("Dialog", "Bod 2:"))
        self.label_3.setText(_translate("Dialog", "Délka 1:"))
        self.label_4.setText(_translate("Dialog", "Délka 2:"))
        self.label_5.setText(_translate("Dialog", "ČB:"))
        self.label_6.setText(_translate("Dialog", "Y:"))
        self.label_7.setText(_translate("Dialog", "X:"))
        self.Vypocet.setText(_translate("Dialog", "Výpočet"))
        self.uloz.setText(_translate("Dialog", "Ulož bod"))
        self.protokol.setText(_translate("Dialog", "Protokol"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())