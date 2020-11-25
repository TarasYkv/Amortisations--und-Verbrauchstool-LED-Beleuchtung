#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
LIMASCalc ist ein Programm zur Kostendarstellung und Amortisationsdarstellung eines Beleuchtungssystems
Copyright (C) [2020]  [Taras Yuzkiv, [IES] - Individual Engeneering Solutions & Adolf Schuch GmbH]
Dieses Programm ist freie Software. Sie können es unter den Bedingungen der GNU General Public License, wie von der Free Software Foundation veröffentlicht, weitergeben und/oder modifizieren, entweder gemäß Version 3 der Lizenz oder (nach Ihrer Option) jeder späteren Version.
Die Veröffentlichung dieses Programms erfolgt in der Hoffnung, daß es Ihnen von Nutzen sein wird, aber OHNE IRGENDEINE GARANTIE, sogar ohne die implizite Garantie der MARKTREIFE oder der VERWENDBARKEIT FÜR EINEN BESTIMMTEN ZWECK. Details finden Sie in der GNU General Public License.
Sie sollten ein Exemplar der GNU General Public License zusammen mit diesem Programm erhalten haben. Falls nicht, siehe <http://www.gnu.org/licenses/>.
"""
import ctypes
import inspect
import sys
import os
import time
from urllib.request import urlopen

from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt, QDateTime, QByteArray
from PyQt5.QtGui import QPixmap, QIcon, QMovie
from PyQt5.QtWidgets import QListWidgetItem, QFileDialog, QToolBar, QStatusBar, QMessageBox, QSplashScreen, \
    QDesktopWidget, QMainWindow, QHeaderView, QApplication
import webbrowser
import win32com.client as win32
import subprocess
import urllib3
import threading

import myTab5
import MovieSplashScreen

version = 3.1
my_encoding = 'utf-8'

class window1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.y = uic.loadUi('untitled1.ui', self)
        self.y.setGeometry(150, 50, 1100, 600)
        self.y.setWindowTitle("SCHUCH - Wirtschaftlichkeitsberechnung LED-Leuchten mit Lichtmanagementsystem")
        self.y.setWindowIcon(QIcon('pics/SCHUCH_LOGO_FavIcon.jpg'))
        self.y.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.show_pic(os.path.dirname(sys.argv[0]) + '/pics/schuch.png', self.y.label)
        self.set_Style()
        self.y.tabWidget.setCurrentIndex(0)
        self.y.pushButton.clicked.connect(self.dia_offnen)
        self.y.horizontalSlider.valueChanged[int].connect(lambda: self.changeValue(self.y.horizontalSlider.value(), self.y.lcdNumber))
        self.y.horizontalSlider_2.valueChanged[int].connect(lambda: self.changeValue(self.y.horizontalSlider_2.value(), self.y.lcdNumber_2))
        self.y.horizontalSlider_3.valueChanged[int].connect(lambda: self.changeProgressBar(self.y.progressBar, self.y.horizontalSlider_3.value()))
        self.y.dial.valueChanged[int].connect(lambda: self.changeValue(self.y.dial.value(), self.y.lcdNumber_3))
        self.y.dial_2.valueChanged[int].connect(lambda: self.changeValue(self.y.dial_2.value(), self.y.lcdNumber_4))
        self.updateTime()
        self.y.timeEdit_2.timeChanged.connect(self.updateTime)
        self._createMenu()
        self._createToolBar()
        #self.checkBox.setToolTip("This is a ToolTip")
        self._createStatusBar()
        self.changeStatusBar("Herzlich willkommen!")
        self.y.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.myButton()
        self.myTips()
        self.y.pushButton_18.clicked.connect(lambda: self.infoPopUp(
            "Das Einsparpotential einer tageslichtabhängigen Regelung hängt von vielen Faktoren ab. Um dennoch eine Aussage darüber treffen zu können, sind unter anderem folgende Informationen von Bedeutung:\n\n"+
            "- Fenstergröße (Klein/Mittel/Groß evtl. Dachfenster)\n"+
            "- gewünschtes Beleuchtungsniveau\n"+
            "- Uhrzeiten und Dauer\n"+
            "- Jahreszeiten\n\n"+
            "Bei einer Mittleren Fenstergröße und tagsüber einer durchschnittlichen Beleuchtungsdauer von 10 Stunden können bei geforderten 500lux auf das ganze Jahr gesehen bis zu 40% eingespart werden.\n\n"+
            "Nicht zu vernachlässigen ist die (Wartungsfaktor bedingte) Überdimmensionierung der Anlage, welche einen unnötigen Stromverbrauch mit sich bringt, jedoch durch die tageslichtabhängige Regelung eingespart werden kann.\n",
            "Informationen zu tageslichtabhängigen Regelung", ""
            ))
        self.y.pushButton_12.clicked.connect(lambda: self.infoPopUp(
            "Die Emmisionsfaktoren für die ausgestossene Gase für pro kWh sind aus Veröfentlichungen des Umweltbundesamtes aus dem Jahr 2017 \n\n", "Quelle", "",
            "https://www.umweltbundesamt.de/themen/luft/emissionen-von-luftschadstoffen/spezifische-emissionsfaktoren-fuer-den-deutschen"))
        self.y.pushButton_13.clicked.connect(lambda: self.infoPopUp("Die unterschiedliche Anzahl der Arbeitstage im Jahr ergibt sich durch die verschiedenen Feiertagsregelungen in den einzelnen Bundesländern.\n\n"
                                                                              "Allgemein gilt: Arbeitstage pro Jahr für die Fünf-Tage-Woche und Sechs-Tage-Woche sind wie folgt:\n\n"
                                                                              "5 Tage Woche: 230 Arbeitstage pro Kalenderjahr\n\n"
                                                                              "6 Tage Woche: 280 Arbeitstage pro Kalenderjahr\n\n", "Hinweis", ""))

        self.y.pushButton_14.clicked.connect(lambda: self.infoPopUp("Die unterschiedliche Anzahl der Arbeitstage im Jahr ergibt sich durch die verschiedenen Feiertagsregelungen in den einzelnen Bundesländern.\n\n"
                                                                              "Allgemein gilt: Arbeitstage pro Jahr für die Fünf-Tage-Woche und Sechs-Tage-Woche sind wie folgt:\n\n"
                                                                              "5 Tage Woche: 230 Arbeitstage pro Kalenderjahr\n\n"
                                                                              "6 Tage Woche: 280 Arbeitstage pro Kalenderjahr\n\n", "Hinweis", ""))
        self.y.pushButton_23.clicked.connect(lambda: self.infoPopUp(
            "Eine Investition hat sich dann amortisiert, wenn das Volumen der angesammelten, "
            "zurückgeflossenen Erträge den Investitionsbetrag überschritten hat.\n\n"
            "Bei der Amortisationsberechnung von 'Schuch-Leuchten mit LIMAS' werden die laufenden Kosten der Bestandsanlage mit den anschaffungs- und laufenden Kosten"
            "der 'Schuch-Leuchten mit LIMAS' gegenübergestellt.\n\n"
            "Bei der Amortisationsberechnung 'LIMAS ohne Leuchten' wird die Ersparnis durch LIMAS gegenüber LIMAS Inverstitionskosten/Aufpreis dargestellt.\n\n"
            "Bei der Amortisationsberechnung mit 'Schuch-Leuchten' werden die laufenden Kosten der Bestandsanlage mit den Anschaffungs- und laufenden Kosten"
            "der 'Schuch-Leuchten' gegenübergestellt.\n\n"
                        , "Hinweis", ""))
        self.y.pushButton_15.clicked.connect(lambda: self.infoPopUp("Hier können zum Beispiel ohnehin erforderliche Investitionskosten/Reparaturkosten eingetragen werden", "Hinweis", ""))
        self.y.pushButton_16.clicked.connect(lambda: self.infoPopUp("Hier können zum Beispiel Gateway-/Cloudkosten eingetragen werden", "Hinweis", ""))
        self.y.pushButton_19.clicked.connect(self.updateSignal)
        self.uebernehmen()
        self.location_on_the_screen()
        self.y.show()


    def font_change(self):
        font, ok = QtWidgets.QFontDialog.getFont()
        if ok:
            for name, obj in inspect.getmembers(self):
                if isinstance(obj, QtWidgets.QLabel):
                    obj.setFont(font)
                if isinstance(obj, QtWidgets.QCheckBox):
                    obj.setFont(font)
                if isinstance(obj, QtWidgets.QLineEdit):
                    obj.setFont(font)
                if isinstance(obj, QtWidgets.QPushButton):
                    obj.setFont(font)
                if isinstance(obj, QtWidgets.QTabWidget):
                    obj.setFont(font)
                if isinstance(obj, QtWidgets.QToolBar):
                    obj.setFont(font)
                if isinstance(obj, QtWidgets.QFrame):
                    obj.setFont(font)
                if isinstance(obj, QtWidgets.QSlider):
                    obj.setFont(font)
                if isinstance(obj, QtWidgets.QTabWidget):
                    obj.setFont(font)
                if isinstance(obj, QtWidgets.QToolButton):
                    obj.setFont(font)
                if isinstance(obj, QtWidgets.QMenuBar):
                    obj.setFont(font)
            self.menu.setFont(font)
            self.berichte.setFont(font)

    def updateSignal(self):
        vCloud = 'https://digital-ies.de/wp-content/uploads'
        movie = QMovie(os.path.dirname(sys.argv[0]) + "/pics/loader.gif", QByteArray(), self)
        movie.setCacheMode(QMovie.CacheAll)
        movie.setSpeed(100)
        self.y.label_44.setMovie(movie)
        x = threading.Thread(target=movie.start())
        x.setDaemon(True)
        x.start()
        http = urllib3.PoolManager()
        response = http.request('GET', "https://digital-ies.de/wp-content/uploads/myActualVersion.txt")
        data = response.data.decode('utf-8')
        if str(data) != str(version):
            y = threading.Thread(target=self.meinDownload, args=(vCloud,))
            y.setDaemon(True)
            y.start()
            while not os.path.exists(os.path.dirname(sys.argv[0]) + "/setup.exe"):
                QApplication.instance().processEvents()
            time.sleep(5)
            movie.stop()
            self.y.label_44.setMovie(None)
            self.y.pushButton_19.setVisible(True)
            p2 = subprocess.Popen(os.path.dirname(sys.argv[0]) + "/unins000.exe")
            p2.wait()
            subprocess.Popen(os.path.dirname(sys.argv[0]) + "/setup.exe")
            os.system("taskkill /f /im  LIMASCalc.exe")


    def location_on_the_screen(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.y.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()-100) / 2)

    def uebernehmen(self):
        self.y.toolButton.clicked.connect(lambda: self.enableDisableTab(False, True, False, False, False))
        self.y.toolButton_3.clicked.connect(lambda: self.enableDisableTab(True, False, False, False, False))
        self.y.toolButton_2.clicked.connect(lambda: self.enableDisableTab(False, False, True, False, False))
        self.y.toolButton_4.clicked.connect(lambda: self.enableDisableTab(False, True, False, False, False))
        self.y.toolButton_5.clicked.connect(lambda: self.enableDisableTab(False, False, False, True, False))
        self.y.toolButton_10.clicked.connect(lambda: self.enableDisableTab(False, False, True, False, False))
        self.y.toolButton_8.clicked.connect(lambda: self.enableDisableTab(False, False, False, False, True))
        self.y.toolButton_12.clicked.connect(lambda: self.enableDisableTab(False, False, False, True, False))

    def enableDisableTab(self, t0, t1, t2, t3, t4):
        self.y.tabWidget.setTabEnabled(0, t0)
        self.y.tabWidget.setTabEnabled(1, t1)
        self.y.tabWidget.setTabEnabled(2, t2)
        self.y.tabWidget.setTabEnabled(3, t3)
        self.y.tabWidget.setTabEnabled(4, t4)

    def myButton(self):
        self.changeValue(self.y.horizontalSlider.value(), self.y.lcdNumber)
        self.changeValue(self.y.horizontalSlider_2.value(), self.y.lcdNumber_2)
        self.changeProgressBar(self.y.progressBar, self.y.horizontalSlider_3.value())
        self.changeValue(self.y.dial.value(), self.y.lcdNumber_3)
        self.changeValue(self.y.dial_2.value(), self.y.lcdNumber_4)
        self.enableDisableTab(True, False, False, False, False)
        #---im Null
        self.y.toolButton.clicked.connect(lambda: self.y.tabWidget.setCurrentIndex(1))
        #---im Eins
        self.y.toolButton_3.clicked.connect(lambda: self.y.tabWidget.setCurrentIndex(0))
        if self.y.comboBox.currentText() == "Straßenbeleuchtung":
            self.y.toolButton_2.clicked.connect(lambda: self.y.tabWidget.setCurrentIndex(3))
            print("soll zu 3")
        else:
            print("soll zu 2")
            self.y.toolButton_2.clicked.connect(lambda: self.y.tabWidget.setCurrentIndex(2))
        #---im Zwei
        self.y.toolButton_4.clicked.connect(lambda: self.y.tabWidget.setCurrentIndex(1))
        self.y.toolButton_5.clicked.connect(lambda: self.y.tabWidget.setCurrentIndex(3))
        #---im Drei
        if self.y.comboBox.currentText() == "Straßenbeleuchtung":
            self.y.toolButton_10.clicked.connect(lambda: self.y.tabWidget.setCurrentIndex(1))
        else:
            self.y.toolButton_10.clicked.connect(lambda: self.y.tabWidget.setCurrentIndex(2))

        self.y.toolButton_8.clicked.connect(lambda: self.y.tabWidget.setCurrentIndex(4))
        #---im Vier
        self.y.toolButton_12.clicked.connect(lambda: self.y.tabWidget.setCurrentIndex(3))


    def myTips(self):
        self.checkBox.setToolTip("auswählen wenn Steuerung durch Bewegungsmelder ausgeführt wird")
        self.checkBox_2.setToolTip("auswählen wenn Steuerung durch Lichtsensoren ausgeführt wird")

    def infoPopUp(self, massBox, massBoxTitle, informativeText="", detailedText="" ):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(massBox)
        msg.setInformativeText(informativeText)
        msg.setWindowTitle(massBoxTitle)
        msg.setDetailedText(detailedText)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()
        msg.exec_()

    def updateTime(self):
        #self.y.progressBar_2.show()
        self.myTime = int(self.y.timeEdit.time().minute())
        self.myTime = self.myTime + (60 * int(self.y.timeEdit.time().hour()))
#        if self.y.checkBox_2.isChecked() and self.y.checkBox.isChecked():
#        if self.y.checkBox_2.isChecked() and self.y.checkBox.isChecked():
            #self.y.progressBar_2.show()
#           self.y.progressBar_2.setMaximum(self.myTime)
#        else:
#            self.y.progressBar_2.setEnabled(False)
#            self.y.progressBar_2.hide()
        self.lightTime = int(self.y.timeEdit_2.time().minute())
        self.lightTime = self.lightTime + (60 * int(self.y.timeEdit_2.time().hour()))
        #self.y.progressBar_2.setValue(int(self.lightTime))
        #if self.y.checkBox.isChecked() and self.lightTime > self.myTime:
        #    self.infoPopUp("der Wert darf nicht überschritten werden. Die Tageslichtnutzung findet nur statt wenn durch Bewegungsmelder der Anwesenheitswert der Beleuchtung aktiv ist.", "Achtung")
        #    self.y.timeEdit_2.setTime(self.y.timeEdit.time())

    def changeScale(self, skalierung):
        os.environ["QT_SCREEN_SCALE_FACTORS"] = str(skalierung)
        print("ausgeführt, skaliert")

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("Menu")
        self.menu.addAction('Über', lambda: self.infoPopUp("Autor: Taras Yuzkiv, M.Sc. \nFirma: Adolf Schuch GmbH \nMainzerstr.172 \n67547 Worms \n\nKontakt: \n                 E-Mail:  taras.yuzkiv@schuch.de \n                 Tel.:       06241/4091-533", "Herstellerinformationen "))
        self.menu.addAction('Quellcode Berechnungen',
                                lambda: os.startfile(os.path.dirname(sys.argv[0]) + "/doc/LIMAScalc_korr_V4.xlsx"))
        self.Darstellung = self.menu.addMenu("Darstellung")
        self.Darstellung.addAction('Schriftgröße ändern', self.font_change)
        self.Darstellung.addAction('Maximieren', self.showMaximized)
        self.Darstellung.addAction('Minimieren', self.showMinimized)
        self.Darstellung.addAction('Größe 1100x600', lambda: self.setFixedSize(1100, 600))

        #self.skalierung = self.Darstellung.addMenu("Skalierung")
        #self.skalierung.addAction('100%', lambda: self.changeScale(str(1.0)))
        #self.skalierung.addAction('125%', lambda: self.changeScale(str(1.25)))
        #self.skalierung.addAction('150%', lambda: self.changeScale(str(1.5)))
        #self.skalierung.addAction('175%', lambda: self.changeScale(str(1.75)))
        #self.skalierung.addAction('200%', lambda: self.changeScale(str(2.0)))

        with open("version/releasNotes.txt", 'r', encoding='utf8') as file:
            readNotes = file.read()
        self.menu.addAction('Releas Notes', lambda: self.infoPopUp("Hier findest du Informationen über die Updates und Versionen des LIMASCalc. Die auf dem PC installierte Version ist Version "+str(version), "Releas Notes", "", str(readNotes)))
        file.close()
        self.menu.addSeparator()
        self.menu.addAction('Exit', self.close)
        self.berichte = self.menuBar().addMenu("Lichtmanagementsysteme")
        self.berichte.addAction('LIMAS Indoor', lambda: os.startfile(os.path.dirname(sys.argv[0])+"/doc/esave-Industry_V1.pdf"))
        self.berichte.addAction('LIMAS Line PRO', lambda: os.startfile(os.path.dirname(sys.argv[0]) + "/doc/LIMAS Line PRO.pdf"))
        self.berichte.addAction('LIMAS Line BASIC',
                                lambda: os.startfile(os.path.dirname(sys.argv[0]) + "/doc/LIMAS LINE BASIC.pdf"))
        self.berichte.addAction('easyAir', lambda: os.startfile(os.path.dirname(sys.argv[0]) + "/doc/easyAir SNH200.pdf"))
        self.berichte.addAction('touchPanel für Lichmanagement', lambda: os.startfile(os.path.dirname(sys.argv[0]) + "/doc/touchPANEL_LM_V1.2.pdf"))
        self.berichte.addAction('touchPanel für Notlichüberwachung', lambda: os.startfile(os.path.dirname(sys.argv[0]) + "/doc/touchPANEL_NOT_V1.1.pdf"))
        self.berichte.addAction('MICAS', lambda: os.startfile(os.path.dirname(sys.argv[0]) + "/doc/AUTOLIGHT 868_V1.pdf"))
        self.berichte.addAction('DALI/DALI2/D4I/ZD4I',
                                lambda: os.startfile(os.path.dirname(sys.argv[0]) + "/doc/DALI(2).pdf"))
        self.berichte.addAction('weitere Informationen folgen...')

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction(QIcon("pics/schuch.jpg"), "SCHUCH Kataloge", lambda: webbrowser.open('https://www.schuch.de', new=2))
        tools.addAction('Schuch Kataloge', lambda: webbrowser.open('https://www.schuch.de/de/service/katalog', new=2))
        tools.addAction('Datenblätter anfordern', lambda: self.emailAnfragen("ich benötige folgende Unterlagen:"))

    def emailAnfragen(self, name):
        #os.startfile("outlook")
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = "taras.yuzkiv@schuch.de"
        mail.Subject = "Anfrage weitere Informationen"
        mail.HtmlBody = "Hallo, \n ich benötige folgende Informationen:\n"
        mail.Display(True)
        #mail.send

    def _createStatusBar(self):
        self.status = QStatusBar()
        self.status.showMessage("I'm the Status Bar")
        self.setStatusBar(self.status)

    def changeProgressBar(self, myBar, mySlider):
        myBar.setValue(mySlider)

    def changeStatusBar(self, text):
        self.status.showMessage(text)

    def changeValue(self, value, LCD):
        LCD.display(value)

    def set_Style(self):
        try:
            http = urllib3.PoolManager()
            response = http.request('GET', "https://digital-ies.de/wp-content/uploads/myActualVersion.txt")
            data = response.data.decode('utf-8')
            if str(data) != str(version):
                self.y.pushButton_19.setVisible(True)
            else:
                self.y.pushButton_19.setVisible(False)
        except:
            self.infoPopUp("Es besteht leider keine Internetverbindung", "Hinweis","")
        self.y.label_2.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                     "stop:1 white); color: #000000;}")
        self.y.label_4.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                     "stop:1 white); color: #000000;}")
        self.y.label_5.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                     "stop:1 white); color: #000000;}")
        self.y.label_9.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                     "stop:1 white); color: #000000;}")
        self.y.label_10.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                      "stop:1 white); color: #000000;}")
        self.y.label_11.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                      "stop:1 white); color: #000000;}")
        self.y.label_12.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                      "stop:1 white); color: #000000;}")
        self.y.label_13.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                      "stop:1 white); color: #000000;}")
        self.y.label_26.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                      "stop:1 white); color: #000000;}")
        self.y.label_27.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                      "stop:1 white); color: #000000;}")
        self.y.label_34.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                      "stop:1 white); color: #000000;}")
        self.y.label_36.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                      "stop:1 white); color: #000000;}")
        self.y.label_40.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                      "stop:1 white); color: #000000;}")
        self.y.label_43.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                      "stop:1 white); color: #000000;}")
        self.y.label_6.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                     "stop:1 white); color: #000000;}")
        self.y.label_7.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                     "stop:1 white); color: #000000;}")
        self.y.label_8.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                     "stop:1 white); color: #000000;}")
        self.y.label_45.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                     "stop:1 white); color: #000000;}")
        self.y.label_46.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                      "stop:1 white); color: #000000;}")
        self.y.label_17.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                      "stop:1 white); color: #000000;}")
        self.y.label_18.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                      "stop:1 white); color: #000000;}")
        self.y.label_19.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                      "stop:1 white); color: #000000;}")
        self.y.label_135.setStyleSheet("* { background-color: #8E44AD;}")
        self.y.label_59.setStyleSheet("* { background-color: #00b300;}")
        self.y.label_56.setStyleSheet("* { background-color: #ff0000;}")
        self.y.label_62.setStyleSheet("* { background-color: #0075BE;}")
        self.y.label_61.setStyleSheet("* { background-color: #00b300 ;}")
        self.y.label_76.setStyleSheet("* { background-color: #ff0000;}")
        self.y.label_82.setStyleSheet("* { background-color: #0075BE;}")
        self.y.label_91.setStyleSheet("* { background-color: #E5FFE4;}")
        self.y.label_136.setStyleSheet("* { background-color: #FAEDE5;}")
        self.y.label_85.setStyleSheet("* { background-color: #00ff00;}")
        self.y.label_29.setStyleSheet("* { background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #bbe2fa, "
                                     "stop:1 white); color: #000000;}")
        self.y.lcdNumber.setStyleSheet("QLCDNumber {color: green;}")
        self.y.lcdNumber_2.setStyleSheet("QLCDNumber {color: green;}")
        self.y.lcdNumber.setDigitCount(3)
        self.y.lcdNumber_2.setDigitCount(3)

    def show_pic(self, pfad, label):
        myPixmap = QPixmap(pfad)
        myScaledPixmap = myPixmap.scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.y.label.setAlignment(Qt.AlignCenter and Qt.AlignVCenter)
        label.setPixmap(myScaledPixmap)

    def showStatus(self, text1, label1):
        self.text1 = text1
        label1.setText(self.text1)

    def stretchTable(self, table1):
        header = table1.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

    def addDoc(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.pdf)")
        self.fname = fname
        self.y.lineEdit_28.insert(os.path.realpath(self.fname))
        item = QListWidgetItem(self.fname)
        self.y.listWidget.addItem(item)
        self.y.listWidget.scrollToBottom()

    def meinDownload(self, meinV):
        f = urlopen(meinV + "/setup.exe")
        file = f.read()
        f.close()
        f2 = open(os.path.dirname(sys.argv[0]) + "/setup.exe", 'wb')
        f2.write(file)
        f2.close()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_F11:
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()

    def update_popup(self, a, w1, vCloud):
        buttonReply = QMessageBox.question(self, 'Update verfügbar',
                                           "Update durchführen? \n Falls ja, wird die veraltete Version im ersten Schritt deinstalliert.",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            #r = requests.get(vCloud + "/setup.exe", stream=True)
            #size = r.headers['content-length']
            y = threading.Thread(target=self.meinDownload, args=(vCloud,))
            y.setDaemon(True)
            y.start()
            startSplash("pics/loader.gif", a)
            while not os.path.exists(os.path.dirname(sys.argv[0]) + "/setup.exe"):
                QApplication.instance().processEvents()
            time.sleep(5)
            p1 = subprocess.Popen(os.path.dirname(sys.argv[0]) + "/unins000.exe")
            p1.wait()
            subprocess.Popen(os.path.dirname(sys.argv[0]) + "/setup.exe")
            a.exit()
            w1.close()
            os.system("taskkill /f /im  LIMASCalc.exe")
        else:
            pass
"""
    def update_popup_backup(self, a, w1, vCloud):
        buttonReply = QMessageBox.question(self, 'Update verfügbar', "Update durchführen? \n Falls ja, die veraltete Version wird im ersten Schritt deinstalliert.", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            a.exit()
            w1.close()
            subprocess.Popen(vCloud + "/setup.exe")
            #print(str(os.path.dirname(sys.argv[0]) + "/unins000.exe"))
            subprocess.Popen(os.path.dirname(sys.argv[0]) + "/unins000.exe")
            os.system("taskkill /f /im  LIMASCalc.exe")

        else:
            pass
"""
"""
def showForUpdates(vAkt, vCloud, a, w):
    try:
        text_file = open(vCloud + "/myActualVersion.txt", "r")
        lines = text_file.readlines()
        if vAkt != lines:
            window1.update_popup(w, a, w, vCloud)
        else:
            return 0
    except FileNotFoundError:
        QMessageBox.question(w, 'Keine Verbindung', "Sie sind leider nicht im SCHUCH-Netzwerk. Bitte verbinden Sie sich mit dem Schuch-Netzwerk um nach verfügbaren Updates zu suchen.", QMessageBox.Ok)
"""
def showForUpdates(vAkt, vCloud, a, w):
    try:
        http = urllib3.PoolManager()
        response = http.request('GET', vCloud + "/myActualVersion.txt")
        data = response.data.decode('utf-8')
        lines = data
        print(lines)
        print(vAkt)
        if os.path.exists(os.path.dirname(sys.argv[0]) + "/setup.exe"):
            os.remove(os.path.dirname(sys.argv[0]) + "/setup.exe")
            print("File Removed!")
        if str(vAkt) != str(lines):
            window1.update_popup(w, a, w, vCloud)
        else:
            QMessageBox.question(w, 'Update', "Es ist die aktuellste Softwareversion installiert.", QMessageBox.Ok)
    except:
        QMessageBox.question(w, 'Verbindung nicht möglich', "Es besteht keine Internetverbundung. Ohne überprüfung auf Updates fortfahren", QMessageBox.Ok)



def startSplash(meinGif, meineApp):
    pixmap = QMovie(meinGif)
    splash = MovieSplashScreen.MovieSplashScreen(pixmap)
    splash.setMask(splash.mask())
    splash.sizeHint()
    splash.setWindowFlags(Qt.SplashScreen | Qt.WindowStaysOnTopHint)
    splash.show()
    splash.acceptDrops()
    splash.paintEvent(meineApp)
    splash.showEvent(meineApp)
    while pixmap.state() == QMovie.Running and not os.path.exists(os.path.dirname(sys.argv[0]) + "/setup.exe"):
        meineApp.processEvents()


def main():
    QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)  # enable highdpi scaling
    Qt.HighDpiScaleFactorRoundingPolicy.Round
    scaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100
    if scaleFactor >= 1.5:
        os.environ["QT_SCREEN_SCALE_FACTORS"] = "1.5"
    else:
        os.environ["QT_SCREEN_SCALE_FACTORS"] = "scaleFactor"  # das ist der richtige Skalierungsfaktor
    #os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "-1"
    #QT_SCREEN_SCALE_FACTORS
    #os.environ["QT_SCALE_FACTOR"] = "1.4"
    #os.environ["QT_DEVICE_PIXEL_RATIO"] = "0.5"
    app = QApplication(sys.argv)
    pixmap = QPixmap(os.path.dirname(sys.argv[0]) + "/pics/splesh.JPG")
    splash = QSplashScreen(pixmap)
    splash.show()
    splash.showMessage("Module werden geladen...")
    app.processEvents()
    app.setStyle("Fusion")
    time.sleep(3)
    window11 = myTab5.myTab5()
    #window11.setFixedSize(1100, 600)
    #window11.resize(window11.minimumSizeHint())
    splash.finish(window11)
    showForUpdates(version, "https://digital-ies.de/wp-content/uploads", app, window11)
    app.exec_()


if __name__ == "__main__":
    main()