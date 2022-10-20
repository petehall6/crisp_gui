from crisp_gui import *

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class GUI(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #button connectors
        self.ui.pushButton.clicked.connect(self.buttonClicked)

    #callbacks
    def buttonClicked(self):

        sampleID = self.ui.sampIDBx.text()
        qtw.QMessageBox.information(self, "Success", sampleID)



if __name__=='__main__':
    app =qtw.QApplication([])

    MainWindow = GUI()
    MainWindow.show()

    app.exec_()
