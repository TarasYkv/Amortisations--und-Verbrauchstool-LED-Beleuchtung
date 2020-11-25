"""Dialog-Style application."""

import sys
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

stundenProTag = 0
tageProJahr = 0

class Dialog(QDialog):
    """Dialog."""
    def __init__(self):
        """Initializer."""
        super().__init__()
        self.diaA = uic.loadUi('dialog/dialog_industrie.ui', self)
        self.setWindowTitle('Arbeitszeiten')
        self.diaA.label_8.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #0075BE, "
                                     "stop:1 white); color: #000000;}")
        self.diaA.pushButton.clicked.connect(self.berechnung)
        self.buttonBox.accepted.connect(self.wertUebertragen)
        #self.buttonBox.rejected.connect(self.test_cancel)
        self.diaA.show()

    def berechnung(self):
        global stundenProTag
        global tageProJahr
        if self.diaA.comboBox_2.currentIndex() == 0:
            stundenProTag = 8
        if self.diaA.comboBox_2.currentIndex() == 1:
            stundenProTag = 16
        if self.diaA.comboBox_2.currentIndex() == 2:
            stundenProTag = 24
        tageProJahr = int(self.diaA.comboBox.currentText()) * 52.1429
        self.diaA.label_8.setText(str(int(tageProJahr)*int(stundenProTag)))
        print(str(stundenProTag))
        print(str(tageProJahr))






    def wertUebertragen(self):
        global stundenProTag
        global tageProJahr
        self.berechnung()
        return stundenProTag, tageProJahr


