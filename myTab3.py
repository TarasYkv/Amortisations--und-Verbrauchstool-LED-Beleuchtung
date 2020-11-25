"""
LIMASCalc ist ein Programm zur Kostendarstellung und Amortisationsdarstellung eines Beleuchtungssystems
Copyright (C) [2020]  [Taras Yuzkiv, [IES] - Individual Engeneering Solutions & Adolf Schuch GmbH]
Dieses Programm ist freie Software. Sie können es unter den Bedingungen der GNU General Public License, wie von der Free Software Foundation veröffentlicht, weitergeben und/oder modifizieren, entweder gemäß Version 3 der Lizenz oder (nach Ihrer Option) jeder späteren Version.
Die Veröffentlichung dieses Programms erfolgt in der Hoffnung, daß es Ihnen von Nutzen sein wird, aber OHNE IRGENDEINE GARANTIE, sogar ohne die implizite Garantie der MARKTREIFE oder der VERWENDBARKEIT FÜR EINEN BESTIMMTEN ZWECK. Details finden Sie in der GNU General Public License.
Sie sollten ein Exemplar der GNU General Public License zusammen mit diesem Programm erhalten haben. Falls nicht, siehe <http://www.gnu.org/licenses/>.
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog

import myTab2
import myTab4

gTab3 = {"bewegungsmelder": "True",
        "bewegungsmelderExtra": "True",
        "abwesenheitswert": "0",
        "anwesenheitswert": "0",
        "frequentierungStunden": "0.0",
        "frequentierungMinuten": "0.0",
        "mehrkostenBewegungsmelder": "0.0",
        "fadein": "0",
        "fadeout": "0",
        "tageslicht": "True",
        "reduzierungsNiveau": "0.0",
        "tageslichtnutzungStunden": "0.0",
        "tageslichtnutzungMinuten": "0.0",
        "mehrkostenTageslicht": "0.0",
        "kalenderCheck": "True",
        "anzahlAnAus": "0"
        }
anteilBewe=0
anteilLicht=0
anteilKalender=0

class myTab3(myTab2.myTab2):
    def __init__(self):
        super().__init__()
        self.zusammenfassung(myTab4.myTab4.b.anteilBewegungsmelder, myTab4.myTab4.b.anteilTageslichtabhSteuerung,
                             myTab4.myTab4.b.anzahlAnAus)
        self.y.toolButton_5.clicked.connect(self.appButtonTab3)
        self.erweiterteBewegungsmelder()
        self.disableMSens()
        self.disableDaySens()
        self.appKalender()
        self.y.checkBox.clicked.connect(self.disableMSens)
        self.y.checkBox_2.clicked.connect(self.disableDaySens)
        self.y.checkBox_3.clicked.connect(self.disableMSensExtra)
        self.y.checkBox_10.clicked.connect(self.bewTagLichtAnteil)
        self.y.checkBox_5.clicked.connect(self.appKalender)
        self.y.pushButton_17.clicked.connect(self.appKalender)
        self.y.comboBox_2.currentTextChanged.connect(self.appKalender)



    def disableMSens(self):
        global anteilBewe
        if self.y.checkBox.isChecked():
            text, okPressed = QInputDialog.getInt(self, "Anteil der Leuchten", "Wie viele Leuchten werden durch Bewegungsmelder gesteuert :", 50, 0, 9999, 1)
            if okPressed == True and (int(text) + int(anteilLicht)) <= int(myTab2.gTab2["neuAnzahl"]):
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
                self.y.checkBox_10.setEnabled(True)
                temp = "vorhanden (" + str(text) + " Leuchten werden über Bewegungsmelder gesteuert)"
                anteilBewe = int(text)
                self.y.checkBox.setText(temp)
                self.zusammenfassung(anteilBewe, anteilLicht, anteilKalender)
            elif okPressed == True:
                self.y.checkBox.setChecked(False)
                self.infoPopUp("Insgesamt sind " + str(
                    myTab2.gTab2["neuAnzahl"]) + " Leuchten verfügbar. Es können nicht mehr als " + str(
                    myTab2.gTab2["neuAnzahl"]) + " Leuchten angegeben werden", "Hinweis", "")
                self.y.lineEdit_24.setText("0")
            else:
                anteilBewe = 0
                self.y.checkBox.setChecked(False)
                self.zusammenfassung(anteilBewe, anteilLicht, anteilKalender)
                self.y.lineEdit_24.setText("0")
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
            self.y.checkBox_10.setEnabled(False)
            self.y.checkBox.setText("vorhanden")
            anteilBewe = 0
            self.y.lineEdit_24.setText("0")
            self.zusammenfassung(anteilBewe, anteilLicht, anteilKalender)

    def disableMSensExtra(self):
        if self.y.checkBox_3.isChecked():
            self.y.label_22.show()
            self.y.dial.show()
            self.y.lcdNumber_3.show()
            self.y.label_32.show()
            self.y.lineEdit_26.show()
            self.y.dial_2.show()
            self.y.lcdNumber_4.show()
            self.y.label_23.show()
            self.y.label_33.show()
            self.y.lineEdit_27.show()
            self.y.label_21.setEnabled(False)
            self.y.timeEdit.setEnabled(False)
        else:
            self.y.label_22.hide()
            self.y.dial.hide()
            self.y.lcdNumber_3.hide()
            self.y.label_32.hide()
            self.y.lineEdit_26.hide()
            self.y.dial_2.hide()
            self.y.lcdNumber_4.hide()
            self.y.label_23.hide()
            self.y.label_33.hide()
            self.y.lineEdit_27.hide()
            self.y.label_21.setEnabled(True)
            self.y.timeEdit.setEnabled(True)

    def erweiterteBewegungsmelder(self):
        self.y.label_22.hide()
        self.y.dial.hide()
        self.y.lcdNumber_3.hide()
        self.y.label_32.hide()
        self.y.lineEdit_26.hide()
        self.y.dial_2.hide()
        self.y.lcdNumber_4.hide()
        self.y.label_23.hide()
        self.y.label_33.hide()
        self.y.lineEdit_27.hide()

    def bewTagLichtAnteil(self):
        if self.y.checkBox_10.isChecked():
            text, okPressed = QInputDialog.getInt(self, "Reduzierungsniveau", "durchschnittliche Reduzierung durch Nutzung vom Tageslicht auf ein Niveau von:", 80, 0, 100, 1)
            if okPressed == True:
                temp = int(text)
                gTab3["anwesenheitswert"] = int(text)
                #print(gTab3["anwesenheitswert"])
                self.y.horizontalSlider_2.setValue(temp)
                self.y.horizontalSlider_2.setEnabled(False)
                #test.window1.changeValue(test.window1, self.y.horizontalSlider_2.value(), self.y.lcdNumber_2)
            else:
                self.y.checkBox_10.setChecked(False)
                self.y.horizontalSlider_2.setEnabled(True)
        else:
            self.y.horizontalSlider_2.setEnabled(True)

    def disableDaySens(self):
        global anteilLicht
        if self.y.checkBox_2.isChecked():
            text, okPressed = QInputDialog.getInt(self, "Anteil der Leuchten", "Wie viele Leuchten werden\n durch die tageslichtabhängige Regelung gesteuert :", 50, 0, 9999, 1)
            if okPressed == True and (int(text) + int(anteilBewe)) <= int(myTab2.gTab2["neuAnzahl"]):
                self.y.label_24.setEnabled(True)
                self.y.label_25.setEnabled(True)
                self.y.horizontalSlider_3.setEnabled(True)
                self.y.timeEdit_2.setEnabled(True)
                self.y.progressBar.setEnabled(True)
#                self.y.progressBar_2.setEnabled(True)
                self.y.label_31.setEnabled(True)
                self.y.lineEdit_25.setEnabled(True)
                temp = "vorhanden (" + str(text) + " Leuchten werden über tageslichtabhängige Regelung gesteuert)"
                self.y.checkBox_2.setText(temp)
#                if self.y.checkBox_2.isChecked()==True:
#                    self.y.progressBar_2.show()
#                    self.y.progressBar_2.setValue(int(self.lightTime))
                anteilLicht = int(text)
                self.zusammenfassung(anteilBewe, anteilLicht, anteilKalender)
            elif okPressed == True:
                self.y.checkBox_2.setChecked(False)
                self.infoPopUp("Insgesamt sind " + str(
                    myTab2.gTab2["neuAnzahl"]) + " Leuchten verfügbar. Es können nicht mehr als " + str(
                    myTab2.gTab2["neuAnzahl"]) + " Leuchten angegeben werden", "Hinweis", "")
                self.y.lineEdit_25.setText("0")
            else:
                self.y.checkBox_2.setChecked(False)
                anteilLicht = 0
                self.y.lineEdit_25.setText("0")
                self.zusammenfassung(anteilBewe, anteilLicht, anteilKalender)
        else:
            self.y.label_24.setEnabled(False)
            self.y.label_25.setEnabled(False)
            self.y.horizontalSlider_3.setEnabled(False)
            self.y.timeEdit_2.setEnabled(False)
            self.y.progressBar.setEnabled(False)
            #self.y.progressBar_2.setEnabled(False)
            self.y.label_31.setEnabled(False)
            self.y.lineEdit_25.setEnabled(False)
            self.y.checkBox_2.setText("vorhanden")
            anteilLicht = 0
            self.zusammenfassung(anteilBewe, anteilLicht, anteilKalender)
            self.y.lineEdit_25.setText("0")

    def appKalender(self):
        global anteilKalender
        if self.y.checkBox_5.isChecked():
            self.y.label_42.setEnabled(True)
            self.y.lineEdit_33.setEnabled(True)
            self.y.pushButton_17.setEnabled(True)
            self.y.label_47.setEnabled(True)
            self.y.comboBox_2.setEnabled(True)
            if self.y.comboBox_2.currentText() == "Baden-Württemberg":
                self.y.lineEdit_33.setText(str(12))
            if self.y.comboBox_2.currentText() == "Bayern":
                self.y.lineEdit_33.setText(str(13))
            if self.y.comboBox_2.currentText() == "Berlin":
                self.y.lineEdit_33.setText(str(10))
            if self.y.comboBox_2.currentText() == "Brandenburg":
                self.y.lineEdit_33.setText(str(10))
            if self.y.comboBox_2.currentText() == "Bremen":
                self.y.lineEdit_33.setText(str(10))
            if self.y.comboBox_2.currentText() == "Hamburg":
                self.y.lineEdit_33.setText(str(10))
            if self.y.comboBox_2.currentText() == "Hessen":
                self.y.lineEdit_33.setText(str(10))
            if self.y.comboBox_2.currentText() == "Mecklenburg-Vorpommern":
                self.y.lineEdit_33.setText(str(10))
            if self.y.comboBox_2.currentText() == "Niedersachsen":
                self.y.lineEdit_33.setText(str(10))
            if self.y.comboBox_2.currentText() == "Nordrhein-Westfalen":
                self.y.lineEdit_33.setText(str(11))
            if self.y.comboBox_2.currentText() == "Rheinland-Pfalz":
                self.y.lineEdit_33.setText(str(11))
            if self.y.comboBox_2.currentText() == "Saarland":
                self.y.lineEdit_33.setText(str(12))
            if self.y.comboBox_2.currentText() == "Sachsen":
                self.y.lineEdit_33.setText(str(11))
            if self.y.comboBox_2.currentText() == "Sachsen-Anhalt":
                self.y.lineEdit_33.setText(str(11))
            if self.y.comboBox_2.currentText() == "Schleswig-Holstein":
                self.y.lineEdit_33.setText(str(10))
            if self.y.comboBox_2.currentText() == "Thüringen":
                self.y.lineEdit_33.setText(str(11))
            anteilKalender = self.y.lineEdit_33.text()
            self.zusammenfassung(anteilBewe, anteilLicht, anteilKalender)
        else:
            self.y.label_42.setEnabled(False)
            self.y.lineEdit_33.setEnabled(False)
            self.y.pushButton_17.setEnabled(False)
            self.y.label_47.setEnabled(False)
            self.y.comboBox_2.setEnabled(False)
            anteilKalender = 0
            self.zusammenfassung(anteilBewe, anteilLicht, anteilKalender)

    def zusammenfassung(self, tempBewegung=0, tempLicht=0, tempKalender=0):
        self.y.label_29.setText("Insgemsamt werden " + str(tempBewegung) + " Leuchten bewegungsabhängig gesteuert. Durch die tageslichtabhängige Regelung werden " + str(tempLicht) + " Leuchten geregelt. " + str(int(myTab2.gTab2["neuAnzahl"]) - tempBewegung - tempLicht) + " werden manuell geschaltet. Alle Leuchten \nsind durch die Kalenderfunktion an "+ str(tempKalender) + " Tagen komplett ausgeschaltet (z.B. an Feiertagen).")


    def appButtonTab3(self):
        global anteilLicht
        gTab3["bewegungsmelder"] = self.y.checkBox.isChecked()
        gTab3["bewegungsmelderExtra"] = self.y.checkBox_3.isChecked()
        gTab3["abwesenheitswert"] = self.y.horizontalSlider.value()
        gTab3["anwesenheitswert"] = self.y.horizontalSlider_2.value()
        gTab3["frequentierungStunden"] = self.y.timeEdit.time().hour()
        gTab3["frequentierungMinuten"] = self.y.timeEdit.time().minute()
        gTab3["mehrkostenBewegungsmelder"] = self.y.lineEdit_24.text()
        gTab3["fadein"] = self.y.dial.value()
        gTab3["fadeout"] = self.y.dial_2.value()
        gTab3["tageslicht"] = self.y.checkBox_2.isChecked()
        gTab3["reduzierungsNiveau"] = self.y.horizontalSlider_3.value()
        gTab3["tageslichtnutzung"] = self.y.horizontalSlider_2.value()
        gTab3["tageslichtnutzungStunden"] = self.y.timeEdit_2.time().hour()
        gTab3["tageslichtnutzungMinuten"] = self.y.timeEdit_2.time().minute()
        gTab3["mehrkostenTageslicht"] = self.y.lineEdit_25.text()
        gTab3["kalenderCheck"] = self.y.checkBox_5.isChecked()
        gTab3["anzahlAnAus"] = self.y.lineEdit_33.text()
        if (self.y.checkBox.isChecked() != False) or (self.y.checkBox_2.isChecked() != False) or (self.y.checkBox_5.isChecked() != False):
            self.y.checkBox_9.setEnabled(True)
        else:
            self.y.checkBox_9.setChecked(False)
            self.y.checkBox_9.setEnabled(False)
        if self.y.comboBox.currentText() == "Straßenbeleuchtung":
            anteilLicht = int(self.y.lineEdit_32.text())
            print(anteilLicht)
        screen = QtWidgets.QApplication.primaryScreen()
        screenshot = screen.grabWindow(self.winId())
        screenshot.save('pics/shot_tab3.jpg', 'jpg')