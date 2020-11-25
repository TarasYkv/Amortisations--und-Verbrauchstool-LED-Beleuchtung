"""Dialog-Style application."""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

import nachtDim
import LIMASCalc

stundenProTag = 0
tageProJahr = 0
dimmniveau = 0
meineStunden = 0
meineMinuten = 0
art = 0



class Dialog(QDialog):
    """Dialog."""
    def __init__(self):
        """Initializer."""
        super().__init__()
        self.diaA = uic.loadUi('dialog/dialog_strasse.ui', self)
        self.setWindowTitle('Brennzeiten')
        self.diaA.radioButton_3.setChecked(True)
        #self.diaA.label_8.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #0075BE, " "stop:1 white); color: #000000;}")
        self.diaA.pushButton.clicked.connect(self.berechnung)
        self.buttonBox.accepted.connect(self.wertUebertragen)
        #self.buttonBox.rejected.connect(self.test_cancel)
        self.diaA.show()
        self.diaA.spinBox.hide()
        self.diaA.comboBox.hide()
        self.diaA.comboBox_2.hide()
        self.diaA.label_5.hide()
        self.diaA.label_3.hide()
        self.diaA.label_4.hide()
        self.radioButton.toggled.connect(self.berechnung)
        self.radioButton_2.toggled.connect(self.berechnung)
        self.radioButton_3.toggled.connect(self.berechnung)
        self.diaA.pushButton_20.setIcon(QIcon('pics/frage.png'))
        self.diaA.pushButton_20.clicked.connect(lambda: LIMASCalc.window1.infoPopUp(LIMASCalc.window1, "Grundlagen sind die Zeiten der Sonnenunter- und Sonnenaufgänge im Bereich Berlin. Ein-/Ausschaltzeit ca. 15 Min."
                                                                                                       "nach Sonnenunter- bzw. Sonnenaufgang.", "Hinweis", ""))

    def berechnung(self):
        global stundenProTag
        stundenProTag = 4100 / 365
        global tageProJahr
        tageProJahr = 365
        global dimmniveau
        global meineMinuten
        global meineStunden
        global art
        if self.diaA.radioButton_3.isChecked():
            art = 1
            print("Ganznacht")
            stundenProTag = 4100/365
            tageProJahr = 365
            dimmniveau = 100
            self.diaA.label_6.setText(str(4100))
            self.diaA.label_8.setText(str(0))
            self.diaA.label_10.setText("4100")
            self.diaA.spinBox.hide()
            self.diaA.comboBox.hide()
            self.diaA.comboBox_2.hide()
            self.diaA.label_5.hide()
            self.diaA.label_3.hide()
            self.diaA.label_4.hide()
        if self.diaA.radioButton_2.isChecked():
            print("Spätnachts")
            art = 2
            tabelleValue = nachtDim.nachtDim(self.diaA.comboBox.currentText(), self.diaA.comboBox_2.currentText())
            transAn1, transAus1 = tabelleValue.translateAnAus(tabelleValue.an, tabelleValue.aus)
            meinWert = tabelleValue.catchValue(transAus1, transAn1)
            dimmniveau = 0
            meinWert = 4100 / 365 - meinWert / 365
            print("mein Wert: " + str(meinWert))
            meineStunden, meineMinuten = str(meinWert).split(".")
            print("hier meine Stunden " + str(meineStunden))
            print("hier meine Minuten " + str(round((float(str("0." + meineMinuten)) * 60), 0)))
            meineMinuten = int(round((float(str("0." + meineMinuten)) * 60), 0))
            self.diaA.label_8.setText(str(float(tageProJahr) * float(meinWert)))
            self.diaA.label_6.setText(str(4100 - float(tageProJahr) * float(meinWert)))
            self.diaA.label_10.setText("4100")
            self.diaA.comboBox.show()
            self.diaA.comboBox_2.show()
            self.diaA.label_5.show()
            self.diaA.label_3.show()
            self.diaA.label_4.show()
            self.diaA.spinBox.hide()
        if self.diaA.radioButton.isChecked():
            art = 3
            tabelleValue = nachtDim.nachtDim(self.diaA.comboBox.currentText(), self.diaA.comboBox_2.currentText())
            transAn1, transAus1 = tabelleValue.translateAnAus(tabelleValue.an, tabelleValue.aus)
            meinWert = tabelleValue.catchValue(transAus1, transAn1)
            meinWert = 4100/365-meinWert/365
            print("mein Wert: " + str(meinWert))
            meineStunden, meineMinuten = str(meinWert).split(".")
            print("hier meine Stunden " + str(meineStunden))
            print("hier meine Minuten " + str(round((float(str("0."+ meineMinuten))*60), 0)))
            meineMinuten = int(round((float(str("0."+ meineMinuten))*60), 0))
            self.diaA.label_8.setText(str(float(tageProJahr) * float(meinWert)))
            self.diaA.label_6.setText(str(4100-float(tageProJahr) * float(meinWert)))
            self.diaA.label_10.setText("4100")
            dimmniveau = self.diaA.spinBox.value()
            self.diaA.spinBox.show()
            self.diaA.comboBox.show()
            self.diaA.comboBox_2.show()
            self.diaA.label_5.show()
            self.diaA.label_3.show()
            self.diaA.label_4.show()

    def wertUebertragen(self):
        global stundenProTag
        global tageProJahr
        global dimmniveau
        global meineStunden
        global meineMinuten
        global art
        self.berechnung()
        return stundenProTag, tageProJahr, dimmniveau, meineStunden, meineMinuten, art


