# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seznam_souradnic.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Seznam(object):
    def setupUi(self, Seznam):
        Seznam.setObjectName("Seznam")
        Seznam.resize(677, 583)
        self.layoutWidget = QtWidgets.QWidget(Seznam)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 651, 555))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.columnView = QtWidgets.QTableView(self.layoutWidget)
        self.columnView.setObjectName("columnView")
        self.horizontalLayout.addWidget(self.columnView)
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 398, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Seznam)
        QtCore.QMetaObject.connectSlotsByName(Seznam)

    def retranslateUi(self, Seznam):
        _translate = QtCore.QCoreApplication.translate
        Seznam.setWindowTitle(_translate("Seznam", "Seznam souradnic"))
        self.pushButton.setText(_translate("Seznam", "Průměr"))
        self.pushButton_3.setText(_translate("Seznam", "Smaž"))
        self.pushButton_2.setText(_translate("Seznam", "Nový"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Seznam = QtWidgets.QDialog()
    ui = Ui_Seznam()
    ui.setupUi(Seznam)
    Seznam.show()
    sys.exit(app.exec_())