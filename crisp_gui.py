# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crisp_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.idLbl = QtWidgets.QLabel(self.centralwidget)
        self.idLbl.setGeometry(QtCore.QRect(70, 80, 81, 16))
        self.idLbl.setObjectName("idLbl")
        self.sampIDBx = QtWidgets.QLineEdit(self.centralwidget)
        self.sampIDBx.setGeometry(QtCore.QRect(160, 80, 113, 20))
        self.sampIDBx.setObjectName("sampIDBx")
        self.seqSrtBx = QtWidgets.QLineEdit(self.centralwidget)
        self.seqSrtBx.setGeometry(QtCore.QRect(160, 110, 113, 20))
        self.seqSrtBx.setObjectName("seqSrtBx")
        self.seqSrtLbl = QtWidgets.QLabel(self.centralwidget)
        self.seqSrtLbl.setGeometry(QtCore.QRect(70, 110, 81, 16))
        self.seqSrtLbl.setObjectName("seqSrtLbl")
        self.seqEndBx = QtWidgets.QLineEdit(self.centralwidget)
        self.seqEndBx.setGeometry(QtCore.QRect(160, 150, 113, 20))
        self.seqEndBx.setObjectName("seqEndBx")
        self.seqEndLbl = QtWidgets.QLabel(self.centralwidget)
        self.seqEndLbl.setGeometry(QtCore.QRect(70, 150, 81, 16))
        self.seqEndLbl.setObjectName("seqEndLbl")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 21))
        self.menubar.setObjectName("menubar")
        self.menuSJ_CAGE_Cris_py = QtWidgets.QMenu(self.menubar)
        self.menuSJ_CAGE_Cris_py.setObjectName("menuSJ_CAGE_Cris_py")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSJ_CAGE_Cris_py.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.idLbl.setText(_translate("MainWindow", "Sample ID:"))
        self.seqSrtLbl.setText(_translate("MainWindow", "Sequence Start"))
        self.seqEndLbl.setText(_translate("MainWindow", "Sequence End"))
        self.pushButton.setText(_translate("MainWindow", "Run Test"))
        self.menuSJ_CAGE_Cris_py.setTitle(_translate("MainWindow", "SJ-CAGE Cris.py"))


    def runTest(self):
        print("Sample ID: "+self.sampIDBx.text +"/n"
        "Seq Start: "+self.seqSrtBx.text +"/n"
        "Seq End: "+self.seqEndBx.text +"/n"
        )

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
