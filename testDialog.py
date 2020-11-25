"""Dialog-Style application."""

import sys


from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

endKosten = 0

class Dialog(QDialog):
    """Dialog."""
    def __init__(self, anzahl):
        """Initializer."""
        super().__init__()
        self.anzahl = anzahl
        self.diaA = uic.loadUi('dialog/dialog_instalation.ui', self)
        self.setWindowTitle('Installationskosten')
        self.diaA.checkBox.clicked.connect(self.disableHebebuehne)
        self.diaA.label_8.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #0075BE, "
                                     "stop:1 white); color: #000000;}")
        self.diaA.pushButton.clicked.connect(self.berechnung)
        self.buttonBox.accepted.connect(self.wertUebertragen)
        #self.buttonBox.rejected.connect(self.test_cancel)
        self.diaA.show()

    def berechnung(self):
        global endKosten
        anzahlArbeiter = int(self.diaA.comboBox.currentText())
        zeitProLP = int(self.diaA.lineEdit.text())
        stundenlohn = int(self.diaA.lineEdit_2.text())
        weitereKosten = int(self.diaA.lineEdit_5.text())
        if self.diaA.checkBox.isChecked():
            mitzeit = int(self.diaA.lineEdit_3.text())
            mietkosten = int(self.diaA.lineEdit_4.text())
        else:
            mitzeit = 0
            mietkosten = 0
        gesamtkosten = anzahlArbeiter * zeitProLP/60 * self.anzahl * stundenlohn + weitereKosten + (mitzeit * mietkosten)
        self.diaA.label_8.setText(str(gesamtkosten))
        endKosten = int(gesamtkosten)


    def wertUebertragen(self):
        global endKosten
        self.berechnung()
        return endKosten


    def disableHebebuehne(self):
        if self.diaA.checkBox.isChecked():
            self.diaA.lineEdit_3.show()
            self.diaA.lineEdit_4.show()
            self.diaA.label_4.show()
            self.diaA.label_5.show()
        else:
            self.diaA.lineEdit_3.hide()
            self.diaA.lineEdit_4.hide()
            self.diaA.label_4.hide()
            self.diaA.label_5.hide()