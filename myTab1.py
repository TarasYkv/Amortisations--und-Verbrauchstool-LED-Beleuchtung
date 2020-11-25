"""
LIMASCalc ist ein Programm zur Kostendarstellung und Amortisationsdarstellung eines Beleuchtungssystems
Copyright (C) [2020]  [Taras Yuzkiv, [IES] - Individual Engeneering Solutions & Adolf Schuch GmbH]
Dieses Programm ist freie Software. Sie können es unter den Bedingungen der GNU General Public License, wie von der Free Software Foundation veröffentlicht, weitergeben und/oder modifizieren, entweder gemäß Version 3 der Lizenz oder (nach Ihrer Option) jeder späteren Version.
Die Veröffentlichung dieses Programms erfolgt in der Hoffnung, daß es Ihnen von Nutzen sein wird, aber OHNE IRGENDEINE GARANTIE, sogar ohne die implizite Garantie der MARKTREIFE oder der VERWENDBARKEIT FÜR EINEN BESTIMMTEN ZWECK. Details finden Sie in der GNU General Public License.
Sie sollten ein Exemplar der GNU General Public License zusammen mit diesem Programm erhalten haben. Falls nicht, siehe <http://www.gnu.org/licenses/>.
"""
import pickle

from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime, QTime
from PyQt5.QtWidgets import QFileDialog

import LIMASCalc
import os
import myTab4
import myTab3

import IndustrieDialog
import StrassenDialog


gTab1 = {"firmenname": "Platzhalter",
        "projektname": "Platzhalter",
        "strompreis": "0.0",
        "name": "Platzhalter",
        "email": "Platzhalter",
        "tel": "0123456789",
        "zeitDatum": "meinDatum",
        "neueAnlage": "False",
        "art": "1"}


class myTab1(LIMASCalc.window1):
    def __init__(self):
        super().__init__()
        self.y.toolButton.clicked.connect(self.appButtonTab1)
        self.y.toolButton_17.clicked.connect(self.pkl_offnen)
        self.y.comboBox.currentTextChanged.connect(self.artDerAnlage)

    def openDialigIndustrie(self):
        self.dlg = IndustrieDialog.Dialog()
        self.dlg.show()
        if self.dlg.exec_():
            print(self.dlg.wertUebertragen())
            stundenProTag, TageProJahr = self.dlg.wertUebertragen()
            self.y.lineEdit_30.setText(str(stundenProTag))
            self.y.lineEdit_18.setText(str(TageProJahr))

    def openDialigStrasse(self):
        self.dlg = StrassenDialog.Dialog()
        self.dlg.show()
        if self.dlg.exec_():
            print(self.dlg.wertUebertragen())
            stundenProTag, TageProJahr, dimNiveau, meineStunden, meineMinuten, art = self.dlg.wertUebertragen()
            gTab1["art"] = art
            self.y.horizontalSlider_3.setValue(int(dimNiveau))
            self.y.lineEdit_30.setText(str(stundenProTag))
            self.y.lineEdit_18.setText(str(TageProJahr))
            #print("was ist hier los " + str(meineStunden))
            #print("was ist hier los 1 " + str(meineMinuten))
            self.y.timeEdit_2.setTime(QtCore.QTime(int(meineStunden), int(meineMinuten)))


    def artDerAnlage(self):
        if self.y.comboBox.currentText() == "Kundenspezifisch":
            self.y.checkBox_2.setEnabled(True)
            self.y.checkBox_2.setChecked(False)
            self.y.lineEdit_30.setEnabled(True)
            self.y.lineEdit_18.setEnabled(True)
            self.y.checkBox.setEnabled(True)
            self.y.checkBox.setChecked(False)
            self.y.checkBox_5.setEnabled(True)
            self.y.checkBox_5.setChecked(False)
            self.y.lineEdit_30.setText(str(8))
            self.y.lineEdit_18.setText(str(365))
        if self.y.comboBox.currentText() == "Industriebeleuchtung":
            self.y.lineEdit_30.setEnabled(False)
            self.y.lineEdit_18.setEnabled(False)
            self.y.checkBox_2.setEnabled(True)
            self.y.checkBox_2.setChecked(False)
            self.y.checkBox.setEnabled(True)
            self.y.checkBox.setChecked(False)
            self.y.checkBox_5.setEnabled(True)
            self.y.checkBox_5.setChecked(False)
            self.openDialigIndustrie()
        if self.y.comboBox.currentText() == "Straßenbeleuchtung":
            self.y.lineEdit_30.setEnabled(False)
            self.y.lineEdit_18.setEnabled(False)
            self.y.checkBox_2.setEnabled(False)
            self.y.checkBox_2.setChecked(True)
            self.y.checkBox.setEnabled(False)
            self.y.checkBox.setChecked(False)
            self.y.checkBox_5.setEnabled(False)
            self.y.checkBox_5.setChecked(False)
            self.openDialigStrasse()

    def appButtonTab1(self):
        gTab1["firmenname"] = self.y.lineEdit_3.text()
        gTab1["projektname"] = self.y.lineEdit_4.text()
        gTab1["strompreis"] = self.y.lineEdit_5.text()
        gTab1["name"] = self.y.lineEdit_13.text()
        gTab1["email"] = self.y.lineEdit_14.text()
        gTab1["tel"] = self.y.lineEdit_12.text()
        gTab1["zeitDatum"] = self.y.dateTimeEdit.dateTime().toString()
        gTab1["neueAnlage"] = self.y.checkBox_14.isChecked()
        self.setNeuanlage()



    def setNeuanlage(self):
        if self.y.checkBox_14.isChecked():
            self.y.lineEdit.setEnabled(True)
            self.y.lineEdit_6.setEnabled(True)
            self.y.lineEdit_8.setEnabled(True)
            self.y.lineEdit_10.setEnabled(True)
            self.y.lineEdit_37.setEnabled(True)
            self.y.lineEdit_31.setEnabled(True)
            self.y.lineEdit_34.setEnabled(True)
            self.y.lineEdit_15.setEnabled(True)
            self.y.lineEdit_29.setEnabled(True)
            self.y.lineEdit_17.setEnabled(True)
            self.y.lineEdit_20.setEnabled(True)
            self.y.lineEdit_22.setEnabled(True)
            self.y.pushButton_13.setEnabled(True)
            self.y.pushButton_15.setEnabled(True)
            self.y.pushButton_21.setEnabled(True)
        else:
            self.y.lineEdit.setEnabled(False)
            self.y.lineEdit_6.setEnabled(False)
            self.y.lineEdit_8.setEnabled(False)
            self.y.lineEdit_10.setEnabled(False)
            self.y.lineEdit_37.setEnabled(False)
            self.y.lineEdit_31.setEnabled(False)
            self.y.lineEdit_34.setEnabled(False)
            self.y.lineEdit_15.setEnabled(False)
            self.y.lineEdit_29.setEnabled(False)
            self.y.lineEdit_17.setEnabled(False)
            self.y.lineEdit_20.setEnabled(False)
            self.y.lineEdit_22.setEnabled(False)
            self.y.pushButton_13.setEnabled(False)
            self.y.pushButton_15.setEnabled(False)
            self.y.pushButton_21.setEnabled(False)

    def pkl_offnen(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.pkl)")
        if not fname: return 0
        with open(os.path.realpath(fname), "rb") as f:
            t = pickle.load(f)
        myTab4.myTab4.b = t
        self.y.lineEdit_3.setText("hallo")
        self.y.lineEdit_3.setText(str(myTab4.myTab4.b.firmenname))
        self.y.lineEdit_36.setText(str(myTab4.myTab4.b.aufpreisLMS))
        self.y.lineEdit_4.setText(str(myTab4.myTab4.b.projektname))
        self.y.lineEdit_5.setText(str(myTab4.myTab4.b.strompreis))
        self.y.lineEdit_13.setText(str(myTab4.myTab4.b.name))
        self.y.lineEdit_14.setText(str(myTab4.myTab4.b.email))
        self.y.lineEdit_12.setText(str(myTab4.myTab4.b.tel))
        self.y.dateTimeEdit.setDateTime(QDateTime.fromString(myTab4.myTab4.b.zeitDatum))
        self.y.lineEdit.setText(str(myTab4.myTab4.b.altHersteller))
        self.y.lineEdit_6.setText(str(myTab4.myTab4.b.altModell))
        self.y.lineEdit_8.setText(str(myTab4.myTab4.b.altLeistung))
        self.y.lineEdit_10.setText(str(myTab4.myTab4.b.altAnschaffungskosten))
        self.y.lineEdit_31.setText(str(myTab4.myTab4.b.altAnzahl))
        self.y.lineEdit_29.setText(str(myTab4.myTab4.b.althProT))
        self.y.lineEdit_17.setText(str(myTab4.myTab4.b.alttProJ))
        self.y.lineEdit_20.setText(str(myTab4.myTab4.b.altWartung))
        self.y.lineEdit_22.setText(str(myTab4.myTab4.b.altLaufKosten))
        self.y.lineEdit_2.setText(str(myTab4.myTab4.b.neuHersteller))
        self.y.lineEdit_7.setText(str(myTab4.myTab4.b.neuModell))
        self.y.lineEdit_9.setText(str(myTab4.myTab4.b.neuLeistung))
        self.y.lineEdit_11.setText(str(myTab4.myTab4.b.neuAnschaffungskosten))
        self.y.lineEdit_32.setText(str(myTab4.myTab4.b.neuAnzahl))
        self.y.lineEdit_35.setText(str(myTab4.myTab4.b.neuLichtmanagement))
        self.y.lineEdit_16.setText(str(myTab4.myTab4.b.installationsKosten))
        self.y.lineEdit_30.setText(str(myTab4.myTab4.b.neuhProT))
        self.y.lineEdit_18.setText(str(myTab4.myTab4.b.neutProJ))
        self.y.lineEdit_21.setText(str(myTab4.myTab4.b.neuWartung))
        self.y.lineEdit_23.setText(str(myTab4.myTab4.b.neuLaufKosten))
        self.y.checkBox.setChecked((myTab4.myTab4.b.bewegungsmelder))
        self.y.checkBox_2.setChecked((myTab4.myTab4.b.tageslicht))
        self.y.horizontalSlider_3.setValue(int(myTab4.myTab4.b.reduzierungsNiveau))
        self.y.timeEdit_2.setTime(QTime(int(myTab4.myTab4.b.tageslichtnutzungStunden), int(myTab4.myTab4.b.tageslichtnutzungMinuten), 0, 0))
        self.y.lineEdit_25.setText(str(myTab4.myTab4.b.mehrkostenTageslicht))
        self.y.checkBox_3.setChecked((myTab4.myTab4.b.bewegungsmelderExtra))
        self.y.horizontalSlider.setValue(int(myTab4.myTab4.b.abwesenheitswert))
        self.y.horizontalSlider_2.setValue(int(myTab4.myTab4.b.anwesenheitswert))
        self.y.timeEdit.setTime(QTime(int(myTab4.myTab4.b.frequentierungStunden), int(myTab4.myTab4.b.frequentierungMinuten), 0, 0))
        self.y.lineEdit_24.setText(str(myTab4.myTab4.b.mehrkostenBewegungsmelder))
        self.y.dial.setValue(int(myTab4.myTab4.b.fadein))
        self.y.dial_2.setValue(int(myTab4.myTab4.b.fadeout))
        self.y.lineEdit_33.setText(str(myTab4.myTab4.b.anzahlAnAus))
        self.y.checkBox_5.setChecked((myTab4.myTab4.b.kalenderCheck))

        if (myTab4.myTab4.b.bewegungsmelder==True):
            self.y.horizontalSlider.setEnabled(True)
            self.y.horizontalSlider_2.setEnabled(True)
            self.y.timeEdit.setEnabled(True)
            self.y.dial.setEnabled(True)
            self.y.dial_2.setEnabled(True)
            self.y.lcdNumber.setEnabled(True)
            self.y.lcdNumber_2.setEnabled(True)
            self.y.label_30.setEnabled(True)
            self.y.lineEdit_24.setEnabled(True)
            self.y.checkBox_3.setEnabled(True)
            temp = "vorhanden (" + str(myTab4.myTab4.b.anteilBewegungsmelder) + " Leuchten werden über Bewegungsmelder gesteuert)"
            self.y.checkBox.setText(temp)
        else:
            self.y.horizontalSlider.setEnabled(False)
            self.y.horizontalSlider_2.setEnabled(False)
            self.y.timeEdit.setEnabled(False)
            self.y.dial.setEnabled(False)
            self.y.dial_2.setEnabled(False)
            self.y.lcdNumber.setEnabled(False)
            self.y.lcdNumber_2.setEnabled(False)
            self.y.label_30.setEnabled(False)
            self.y.lineEdit_24.setEnabled(False)
            self.y.checkBox_3.setEnabled(False)
            self.y.checkBox.setText("vorhanden")

        if (myTab4.myTab4.b.tageslicht == True):
            self.y.label_24.setEnabled(True)
            self.y.label_25.setEnabled(True)
            self.y.horizontalSlider_3.setEnabled(True)
            self.y.timeEdit_2.setEnabled(True)
            self.y.progressBar.setEnabled(True)
#           self.y.progressBar_2.setEnabled(True)
            self.y.label_31.setEnabled(True)
            self.y.lineEdit_25.setEnabled(True)
            temp = "vorhanden (" + str(myTab4.myTab4.b.anteilTageslichtabhSteuerung) + " Leuchten werden über tageslichtabhängige Regelung gesteuert)"
            self.y.checkBox_2.setText(temp)
        else:
            self.y.label_24.setEnabled(False)
            self.y.label_25.setEnabled(False)
            self.y.horizontalSlider_3.setEnabled(False)
            self.y.timeEdit_2.setEnabled(False)
            self.y.progressBar.setEnabled(False)
            self.y.progressBar_2.setEnabled(False)
            self.y.label_31.setEnabled(False)
            self.y.lineEdit_25.setEnabled(False)
            self.y.checkBox_2.setText("vorhanden")

        if (myTab4.myTab4.b.kalenderCheck ==True):
            self.y.label_42.setEnabled(True)
            self.y.lineEdit_33.setEnabled(True)
            self.y.pushButton_17.setEnabled(True)
        else:
            self.y.label_42.setEnabled(False)
            self.y.lineEdit_33.setEnabled(False)
            self.y.pushButton_17.setEnabled(False)

        #myTab3.anteilBewe = int(myTab4.myTab4.b.anteilBewegungsmelder)
        #myTab3.anteilLicht = int(myTab4.myTab4.b.anteilTageslichtabhSteuerung)
        #myTab3.anteilKalender = int(myTab4.myTab4.b.anzahlAnAus)
        #self.y.label_29.setText("Insgemsamt werden " + str(myTab3.anteilBewe) + " Leuchten bewegungsabhängig gesteuert. Durch die tageslichtabhängige Regelung werden " + str(myTab3.anteilLicht) + " Leuchten geregelt. " + str(int(myTab4.myTab4.b.neuAnzahl) - myTab3.anteilBewe - myTab3.anteilLicht) + " werden manuell geschaltet. Alle Leuchten \n sind durch die Kalenderfunktion an " + str(myTab3.anteilKalender) + " Tagen komplett ausgeschaltet (z.B. an Feiertagen).")