"""
LIMASCalc ist ein Programm zur Kostendarstellung und Amortisationsdarstellung eines Beleuchtungssystems
Copyright (C) [2020]  [Taras Yuzkiv, [IES] - Individual Engeneering Solutions & Adolf Schuch GmbH]
Dieses Programm ist freie Software. Sie können es unter den Bedingungen der GNU General Public License, wie von der Free Software Foundation veröffentlicht, weitergeben und/oder modifizieren, entweder gemäß Version 3 der Lizenz oder (nach Ihrer Option) jeder späteren Version.
Die Veröffentlichung dieses Programms erfolgt in der Hoffnung, daß es Ihnen von Nutzen sein wird, aber OHNE IRGENDEINE GARANTIE, sogar ohne die implizite Garantie der MARKTREIFE oder der VERWENDBARKEIT FÜR EINEN BESTIMMTEN ZWECK. Details finden Sie in der GNU General Public License.
Sie sollten ein Exemplar der GNU General Public License zusammen mit diesem Programm erhalten haben. Falls nicht, siehe <http://www.gnu.org/licenses/>.
"""
import shutil
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication
import os
import myTab1
import testDialog

gTab2 = {"altHersteller": "Platzhalter",
        "altModell": "Platzhalter",
        "altLeistung": "0.0",
        "altAnschaffungskosten": "0.0",
        "altAnzahl": "0",
        "althProT": "0.0",
        "alttProJ": "0",
        "altWartung": "0.0",
        "altLaufKosten": "0.0",
        "neuHersteller": "Platzhalter",
        "neuModell": "Platzhalter",
        "neuLeistung": "0.0",
        "neuAnschaffungskosten": "0.0",
        "neuAnzahl": "0",
        "neuLichtmanagement": "0.0",
        "installationsKosten": "0.0",
        "neuhProT": "0.0",
        "neutProJ": "0.0",
        "neuWartung": "0.0",
        "neuLaufKosten": "0.0",
        "aufpreisLMS": "0.0"}

class myTab2(myTab1.myTab1):
    def __init__(self):
        super().__init__()
        self.y.toolButton_2.clicked.connect(self.appButtonTab2)
        self.y.toolButton_3.clicked.connect(self.appButtonTab2)
        self.y.pushButton_20.clicked.connect(self.openMyDialog)


    def openMyDialog(self):
        self.dlg = testDialog.Dialog(int(self.y.lineEdit_32.text()))
        self.dlg.show()
        if self.dlg.exec_():
            #print(self.dlg.wertUebertragen())
            self.y.lineEdit_16.setText(str(self.dlg.wertUebertragen()))

    def setMusterPic(self):
        if self.y.checkBox_13.isChecked():
            shutil.copy('pics/musterleuchte.jpg', 'pics/Leuchte.jpg')

    def dia_offnen(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.png)")
        if not fname: return 0
        self.fname = fname
        self.show_pic(self.fname, self.y.label_14)
        self.y.lineEdit_19.insert(os.path.realpath(self.fname))
        global lauf
        lauf = os.path.realpath(self.fname)
        shutil.copy(lauf, 'pics/Leuchte.jpg')


    def appButtonTab2(self):
        gTab2["altHersteller"] = self.y.lineEdit.text()
        gTab2["altModell"] = self.y.lineEdit_6.text()
        gTab2["altLeistung"] = self.y.lineEdit_8.text()
        gTab2["altAnschaffungskosten"] = self.y.lineEdit_10.text()
        gTab2["altAnzahl"] = self.y.lineEdit_31.text()
        gTab2["althProT"] = self.y.lineEdit_29.text()
        gTab2["alttProJ"] = self.y.lineEdit_17.text()
        gTab2["altWartung"] = self.y.lineEdit_20.text()
        gTab2["altLaufKosten"] = self.y.lineEdit_22.text()
        gTab2["neuHersteller"] = self.y.lineEdit_2.text()
        gTab2["neuModell"] = self.y.lineEdit_7.text()
        gTab2["neuLeistung"] = self.y.lineEdit_9.text()
        gTab2["neuAnschaffungskosten"] = self.y.lineEdit_11.text()
        gTab2["neuAnzahl"] = self.y.lineEdit_32.text()
        gTab2["neuLichtmanagement"] = self.y.lineEdit_35.text()
        gTab2["installationsKosten"] = self.y.lineEdit_16.text()
        gTab2["neuhProT"] = self.y.lineEdit_30.text()
        gTab2["neutProJ"] = self.y.lineEdit_18.text()
        gTab2["neuWartung"] = self.y.lineEdit_21.text()
        gTab2["neuLaufKosten"] = self.y.lineEdit_23.text()
        gTab2["aufpreisLMS"] = self.y.lineEdit_36.text()
        if self.y.comboBox.currentText() == "Straßenbeleuchtung":
            self.y.label_29.setText("Insgemsamt werden " + str(self.y.lineEdit_32.text())+ " Leuchten durch Halbnacht/Dim Regelung geschaltet." )
        else:
            self.y.label_29.setText("Insgemsamt werden 0 Leuchten bewegungsabhängig gesteuert. Durch die tageslichtabhängige Regelung werden 0 Leuchten geregelt. " + self.y.lineEdit_32.text()  +
            " werden manuell geschaltet. Alle Leuchten \nsind durch die Kalenderfunktion an 0 Tagen komplett ausgeschaltet (z.B. an Feiertagen).")

        screen = QtWidgets.QApplication.primaryScreen()
        screenshot = screen.grabWindow(self.winId())
        screenshot.save('pics/shot_tab2.jpg', 'jpg')
        self.setMusterPic()