import sys
import numpy as np
from matplotlib.backends.qt_compat import QtCore, QtWidgets, QtGui
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from data import Databaze

class Grafika(QtWidgets.QMainWindow):
    def __init__(self,cesta_projekt):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('foto.jpg'))
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Grafika"))
        self._main = QtWidgets.QWidget()
        self.cesta=cesta_projekt

        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        static_canvas = FigureCanvas(Figure(figsize=(20, 20)))
        layout.addWidget(static_canvas)
        self.addToolBar(NavigationToolbar(static_canvas, self))

        self._static_ax = static_canvas.figure.subplots()


        query="select Y, X, CB from gps_sour"
        sour=Databaze.sql_query(self.cesta,query)

        y=[]
        x=[]
        for i in range(0,len(sour)):
            Y=-sour[i][0]
            X=-sour[i][1]
            CB=sour[i][2]
            y.append(Y)
            x.append(X)
            self._static_ax.text(Y,X,CB)


        self._static_ax.plot(y, x, "+")
        self._static_ax.axis('equal')

        self.show()



if __name__ == "__main__":
    qapp = QtWidgets.QApplication(sys.argv)
    app = Grafika()

    app.show()
    qapp.exec_()
