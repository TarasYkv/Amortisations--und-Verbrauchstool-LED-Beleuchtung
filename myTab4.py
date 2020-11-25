"""
LIMASCalc ist ein Programm zur Kostendarstellung und Amortisationsdarstellung eines Beleuchtungssystems
Copyright (C) [2020]  [Taras Yuzkiv, [IES] - Individual Engeneering Solutions & Adolf Schuch GmbH]
Dieses Programm ist freie Software. Sie können es unter den Bedingungen der GNU General Public License, wie von der Free Software Foundation veröffentlicht, weitergeben und/oder modifizieren, entweder gemäß Version 3 der Lizenz oder (nach Ihrer Option) jeder späteren Version.
Die Veröffentlichung dieses Programms erfolgt in der Hoffnung, daß es Ihnen von Nutzen sein wird, aber OHNE IRGENDEINE GARANTIE, sogar ohne die implizite Garantie der MARKTREIFE oder der VERWENDBARKEIT FÜR EINEN BESTIMMTEN ZWECK. Details finden Sie in der GNU General Public License.
Sie sollten ein Exemplar der GNU General Public License zusammen mit diesem Programm erhalten haben. Falls nicht, siehe <http://www.gnu.org/licenses/>.
"""
import sys
import os
import matplotlib.pyplot as plt
import pygame
import numpy as np
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QMovie, QIcon
from PyQt5.QtWidgets import QTableWidgetItem, QApplication

import pickle
import myTab3
import myTab2
import myTab1
import emiTable
import myData
import LIMASCalc

tTab1 = myTab1.gTab1
tTab2 = myTab2.gTab2
tTab3 = myTab3.gTab3
myTableEmi = emiTable.emi()

class myTab4(myTab3.myTab3):
    b = myData.myData(tTab1, tTab2, tTab3)
    myCount = 0
    platzHalter = ""
    def __init__(self):
        super().__init__()
        self.y.pushButton_2.clicked.connect(self.berechnungWerte)
        self.y.toolBox.currentChanged.connect(self.switchFrame)
        self.showZoom()
        self.y.toolButton_16.clicked.connect(lambda: self.saveAll(self.b))
        self.y.pushButton_7.clicked.connect(lambda: self.openPLT1('pics/bild1Tab.jpg', 'Kosten ohne Reparatur- & Zusatzkosten'))
        self.y.pushButton_9.clicked.connect(lambda: self.openPLT1('pics/bild1Tab2.jpg', 'Zusammenfassung Kosten und Ersparnis'))
        self.y.pushButton_11.clicked.connect(lambda: self.openPLT1('pics/bild1Tab3.jpg', 'Amortisationszeitraum Schuch Leuchten, Leuchten mit LIMAS und nur LIMAS'))
        self.y.pushButton_10.clicked.connect(lambda: self.openPLT1('pics/bild1Tab4.jpg', 'Emissionen durch Energieverbrauch'))
        self.y.tableWidget_2.itemSelectionChanged.connect(self.changeRowTable)

    def switchLIMAS(self):
        if self.y.comboBox.currentText() == "Kundenspezifisch":
            self.platzHalter = "LIMAS"
        if self.y.comboBox.currentText() == "Industriebeleuchtung":
            self.platzHalter = "LIMAS"
        if self.y.comboBox.currentText() == "Straßenbeleuchtung":
            if self.b.art == 1:
                self.platzHalter = "Ganznachtbetrieb"
            if self.b.art == 2:
                self.platzHalter = "Abschaltung spätnachts"
            if self.b.art == 3:
                self.platzHalter = "Dimmung spätnachts"


    def refreshAllPics(self):
        self.y.tableWidget_2.selectRow(0)
        self.clickedMyTable("Schwefeldioxid", (self.b.verbrauchAlt * (emiTable.emi.Schwefeldioxid / 1000)),
                            (self.b.verbrauchNeu * (emiTable.emi.Schwefeldioxid / 1000)),
                            (self.b.GesamtverbrauchInkW * (emiTable.emi.Schwefeldioxid / 1000)),
                            "", "kg pro Jahr")
        self.y.tableWidget_2.selectRow(1)
        self.clickedMyTable("Stickstoffdioxid", (self.b.verbrauchAlt * (emiTable.emi.Stickstoffdioxid / 1000)),
                            (self.b.verbrauchNeu * (emiTable.emi.Stickstoffdioxid / 1000)),
                            (self.b.GesamtverbrauchInkW * (emiTable.emi.Stickstoffdioxid / 1000)),
                            "", "kg pro Jahr")
        self.y.tableWidget_2.selectRow(2)
        self.clickedMyTable("Staub", (self.b.verbrauchAlt * (emiTable.emi.Staub / 1000)),
                            (self.b.verbrauchNeu * (emiTable.emi.Staub / 1000)),
                            (self.b.GesamtverbrauchInkW * (emiTable.emi.Staub / 1000)),
                            "", "kg pro Jahr")
        self.y.tableWidget_2.selectRow(3)
        self.clickedMyTable("PM10", (self.b.verbrauchAlt * (emiTable.emi.PM10 / 1000)),
                            (self.b.verbrauchNeu * (emiTable.emi.PM10 / 1000)),
                            (self.b.GesamtverbrauchInkW * (emiTable.emi.PM10 / 1000)),
                            "", "kg pro Jahr")
        self.y.tableWidget_2.selectRow(4)
        self.clickedMyTable("Kohlenmonoxid", (self.b.verbrauchAlt * (emiTable.emi.Kohlenmonoxid / 1000)),
                            (self.b.verbrauchNeu * (emiTable.emi.Kohlenmonoxid / 1000)),
                            (self.b.GesamtverbrauchInkW * (emiTable.emi.Kohlenmonoxid / 1000)),
                            "", "kg pro Jahr")
        self.y.tableWidget_2.selectRow(5)
        self.clickedMyTable("Kohlendioxid", (self.b.verbrauchAlt * (emiTable.emi.Kohlendioxid)),
                            (self.b.verbrauchNeu * (emiTable.emi.Kohlendioxid)),
                            (self.b.GesamtverbrauchInkW * (emiTable.emi.Kohlendioxid)),
                            "", "kg pro Jahr")
        self.y.tableWidget_2.selectRow(6)
        self.clickedMyTable("Lachgas", (self.b.verbrauchAlt * (emiTable.emi.Lachgas)),
                            (self.b.verbrauchNeu * (emiTable.emi.Lachgas)),
                            (self.b.GesamtverbrauchInkW * (emiTable.emi.Lachgas)),
                            "", "kg pro Jahr")
        self.y.tableWidget_2.selectRow(7)
        self.clickedMyTable("Methan", (self.b.verbrauchAlt * (emiTable.emi.Methan / 1000)),
                            (self.b.verbrauchNeu * (emiTable.emi.Methan / 1000)),
                            (self.b.GesamtverbrauchInkW * (emiTable.emi.Methan / 1000)),
                            "", "kg pro Jahr")
        self.y.tableWidget_2.selectRow(8)
        self.clickedMyTable("NMVOC", (self.b.verbrauchAlt * (emiTable.emi.NMVOC / 1000)),
                            (self.b.verbrauchNeu * (emiTable.emi.NMVOC / 1000)),
                            (self.b.GesamtverbrauchInkW * (emiTable.emi.NMVOC / 1000)),
                            "", "kg pro Jahr")
        self.y.tableWidget_2.selectRow(9)
        self.clickedMyTable("Quecksilber", (self.b.verbrauchAlt * (emiTable.emi.Quecksilber / 1000)),
                            (self.b.verbrauchNeu * (emiTable.emi.Quecksilber / 1000)),
                            (self.b.GesamtverbrauchInkW * (emiTable.emi.Quecksilber / 1000)),
                            "", "g pro Jahr")

    def changeRowTable(self):
        if self.y.tableWidget_2.currentRow()==0:
            self.clickedMyTable("Schwefeldioxid", (self.b.verbrauchAlt * (emiTable.emi.Schwefeldioxid / 1000)),
            (self.b.verbrauchNeu * (emiTable.emi.Schwefeldioxid / 1000)), (self.b.GesamtverbrauchInkW * (emiTable.emi.Schwefeldioxid / 1000)),
                                "", "kg pro Jahr")
        if self.y.tableWidget_2.currentRow() == 1:
            self.clickedMyTable("Stickstoffdioxid", (self.b.verbrauchAlt * (emiTable.emi.Stickstoffdioxid / 1000)),
                                (self.b.verbrauchNeu * (emiTable.emi.Stickstoffdioxid / 1000)),
                                (self.b.GesamtverbrauchInkW * (emiTable.emi.Stickstoffdioxid / 1000)),
                                "", "kg pro Jahr")
        if self.y.tableWidget_2.currentRow() == 2:
            self.clickedMyTable("Staub", (self.b.verbrauchAlt * (emiTable.emi.Staub / 1000)),
                                (self.b.verbrauchNeu * (emiTable.emi.Staub / 1000)),
                                (self.b.GesamtverbrauchInkW * (emiTable.emi.Staub / 1000)),
                                "", "kg pro Jahr")
        if self.y.tableWidget_2.currentRow() == 3:
            self.clickedMyTable("PM10", (self.b.verbrauchAlt * (emiTable.emi.PM10 / 1000)),
                                (self.b.verbrauchNeu * (emiTable.emi.PM10 / 1000)),
                                (self.b.GesamtverbrauchInkW * (emiTable.emi.PM10 / 1000)),
                                "", "kg pro Jahr")
        if self.y.tableWidget_2.currentRow() == 4:
            self.clickedMyTable("Kohlenmonoxid", (self.b.verbrauchAlt * (emiTable.emi.Kohlenmonoxid / 1000)),
                                (self.b.verbrauchNeu * (emiTable.emi.Kohlenmonoxid / 1000)),
                                (self.b.GesamtverbrauchInkW * (emiTable.emi.Kohlenmonoxid / 1000)),
                                "", "kg pro Jahr")
        if self.y.tableWidget_2.currentRow() == 5:
            self.clickedMyTable("Kohlendioxid", (self.b.verbrauchAlt * (emiTable.emi.Kohlendioxid)),
                                (self.b.verbrauchNeu * (emiTable.emi.Kohlendioxid )),
                                (self.b.GesamtverbrauchInkW * (emiTable.emi.Kohlendioxid)),
                                "", "kg pro Jahr")
        if self.y.tableWidget_2.currentRow() == 6:
            self.clickedMyTable("Lachgas", (self.b.verbrauchAlt * (emiTable.emi.Lachgas)),
                                (self.b.verbrauchNeu * (emiTable.emi.Lachgas )),
                                (self.b.GesamtverbrauchInkW * (emiTable.emi.Lachgas)),
                                "", "kg pro Jahr")
        if self.y.tableWidget_2.currentRow() == 7:
            self.clickedMyTable("Methan", (self.b.verbrauchAlt * (emiTable.emi.Methan / 1000)),
                                (self.b.verbrauchNeu * (emiTable.emi.Methan / 1000)),
                                (self.b.GesamtverbrauchInkW * (emiTable.emi.Methan / 1000)),
                                "", "kg pro Jahr")
        if self.y.tableWidget_2.currentRow() == 8:
            self.clickedMyTable("NMVOC", (self.b.verbrauchAlt * (emiTable.emi.NMVOC / 1000)),
                                (self.b.verbrauchNeu * (emiTable.emi.NMVOC / 1000)),
                                (self.b.GesamtverbrauchInkW * (emiTable.emi.NMVOC / 1000)),
                                "", "kg pro Jahr")
        if self.y.tableWidget_2.currentRow() == 9:
            self.clickedMyTable("Quecksilber", (self.b.verbrauchAlt * (emiTable.emi.Quecksilber / 1000)),
                                (self.b.verbrauchNeu * (emiTable.emi.Quecksilber / 1000)),
                                (self.b.GesamtverbrauchInkW * (emiTable.emi.Quecksilber / 1000)),
                                "", "g pro Jahr")


    def clickedMyTable(self, stoff, zahl1, zahl2, zahl3, xAchse, yAchse):
        labels = [stoff]
        balken2 = [round(zahl1, 2)]
        balken3 = [round(zahl2, 2)]
        balken4 = [round(zahl3, 2)]
        width = 0.4  # the width of the bars: can also be len(x) sequence
        fig, ax = plt.subplots()
        x = np.arange(len(labels))  # the label locations
        if (self.b.neueAnlage != False):
            rects3 = ax.bar(x - 0.25, balken2, width, label='Bestand', color='#ff0000')
        rects1 = ax.bar(x, balken3, width, label='mit Schuch-Leuchten', color='#ffff00')
        if (self.b.bewegungsmelder != False) or (self.b.tageslicht != False) or (self.b.kalenderCheck != False):
            rects2 = ax.bar(x + 0.25, balken4, width, label='mit Schuch-Leuchten & \n' + self.platzHalter, color='#00ff00')
        if (self.b.neueAnlage != False):
            self.autolabel(rects3, ax)
        self.autolabel(rects1, ax)
        if (self.b.bewegungsmelder != False) or (self.b.tageslicht != False) or (self.b.kalenderCheck != False):
            self.autolabel(rects2, ax)
        ax.set_ylabel(yAchse)
        ax.set_title('Emissionen')
        plt.xlabel(stoff)
        ax.get_xaxis().set_ticks([])
        #plt.grid(True)
        ax.legend(loc='best', bbox_to_anchor=(0.65, 1))
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        fig.tight_layout()
        plt.savefig('pics/bild1Tab3_' + stoff + '.jpg', bbox_extra_artists=(ax,), bbox_inches='tight', dpi=300)
        plt.savefig('pics/bild1Tab4.jpg', bbox_extra_artists=(ax,), bbox_inches='tight', dpi=300)
        self.show_pic('pics/bild1Tab3_' + stoff + '.jpg', self.y.label_38)
        plt.close(fig)


    def testBar(self):
        labels = ['Schuch-Leuchten']
        labels1 = ['Bestand']
        labels2 = ['Schuch-Leuchten mit\n ' + self.platzHalter]
        balken2 = self.b.stromUndReparaturAlt
        balken3 = self.b.stromUndReparaturNeu
        balken4 = self.b.ersparnisAltNeu
        balken5 = self.b.Gesamtkosten
        balken6 = self.b.minusJährlicheZusatzkosten
        width = 0.85  # the width of the bars: can also be len(x) sequence
        fig, ax = plt.subplots()
        if self.b.neueAnlage != False:
            rects3 = ax.bar(labels1, balken2, width, label='Kosten Bestand', color='#ff0000')
            rects2 = ax.bar(labels, balken4, width, bottom=balken3, alpha=0.1, label='Ersparnis durch Schuch-Leuchten',
                            color='#00ff00')
        rects1 = ax.bar(labels, balken3, width, label='Kosten Schuch-Leuchten', color='#0075BE')
        if (self.b.bewegungsmelder != False) or (self.b.tageslicht != False) or (self.b.kalenderCheck != False):
            rects4 = ax.bar(labels2, balken5, width, label='Kosten Schuch-Leuchten \nmit ' + self.platzHalter, color='#8E44AD')
            rects5 = ax.bar(labels2, balken6, width, bottom=balken5, alpha=0.1, label='Ersparnis Schuch-Leuchten \nmit ' + self.platzHalter, color='#D35400')
        if (self.b.neueAnlage != False):
            self.autolabel(rects3, ax)
            self.autolabel(rects2, ax)
        self.autolabel(rects1, ax)
        if (self.b.bewegungsmelder != False) or (self.b.tageslicht != False) or (self.b.kalenderCheck != False):
            self.autolabel(rects4, ax)
            self.autolabel(rects5, ax)
        ax.set_ylabel('in € pro Jahr')
        ax.set_title('Stromkosten mit Reparatur- & Zusatzkosten')
        ax.legend(loc='best', bbox_to_anchor=(0.65, 1))
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.savefig('pics/bild1Tab.jpg', bbox_extra_artists=(ax,), bbox_inches='tight', dpi=300)
        plt.close(fig)

    def testBar1(self):
        labels = ['Schuch-Leuchten']
        labels1 = ['Bestand']
        labels2 = ['Schuch-Leuchten \nmit ' + self.platzHalter]
        balken2 = [round(self.b.stromUndReparaturAlt, 2)]
        balken3 = [round(self.b.stromUndReparaturNeu, 2)]
        balken4 = [round(self.b.Gesamtkosten, 2)]
        width = 0.85  # the width of the bars: can also be len(x) sequence
        fig, ax = plt.subplots()
        if (self.b.neueAnlage != False):
            rects3 = ax.bar(labels1, balken2, width, label='Kosten Bestand', color='#ff0000')
        rects1 = ax.bar(labels, balken3, width, label='Kosten Schuch-Leuchten', color='#0075BE')
        if (self.b.bewegungsmelder != False) or (self.b.tageslicht != False) or (self.b.kalenderCheck != False):
            rects2 = ax.bar(labels2, balken4, width, label='Kosten Schuch-Leuchten \nmit ' + self.platzHalter, color='#00ff00')
        if (self.b.neueAnlage != False):
            self.autolabel(rects3, ax)
        self.autolabel(rects1, ax)
        if (self.b.bewegungsmelder != False) or (self.b.tageslicht != False) or (self.b.kalenderCheck != False):
            self.autolabel(rects2, ax)
        ax.set_ylabel('in € pro Jahr')
        ax.set_title('Stromkosten mit Reparatur- & Zusatzkosten')
        ax.legend(loc='best', bbox_to_anchor=(0.65, 1))
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.savefig('pics/bild1Tab2.jpg', bbox_extra_artists=(ax,), bbox_inches='tight', dpi=300)
        plt.close(fig)

    def testBar2(self):
        labels = ['Schuch-Leuchten \nmit ' + self.platzHalter]
        labels1 = ['Schuch-Leuchten']
        labels2 = [self.platzHalter + ' ohne Leuchten']
        balken2 = [round(self.b.AmortisationszeitraumInJahren, 2)]
        balken3 = [round(self.b.gesamtInJahren, 2)]
        balken4 = [round(self.b.amortisationNurLIMASinJahren, 2)]
        width = 0.85  # the width of the bars: can also be len(x) sequence
        fig, ax = plt.subplots()
        if (self.b.neueAnlage != False):
            rects3 = ax.bar(labels1, balken2, width, label='Amortisation Schuch-Leuchten', color='#ff0000')
        if ((self.b.bewegungsmelder != False) or (self.b.tageslicht != False) or (self.b.kalenderCheck != False)) and self.y.comboBox.currentText() != "Straßenbeleuchtung":
            if (self.b.neueAnlage != False):
                rects1 = ax.bar(labels, balken3, width, label='Amortisation Schuch-Leuchten mit LIMAS', color='#0075BE')
            rects2 = ax.bar(labels2, balken4, width, label='Amortisation LIMAS ohne Leuchten', color='#00ff00')

        if (self.b.neueAnlage != False):
            self.autolabel(rects3, ax)
        if ((self.b.bewegungsmelder != False) or (self.b.tageslicht != False) or (self.b.kalenderCheck != False)) and self.y.comboBox.currentText() != "Straßenbeleuchtung":
            if (self.b.neueAnlage != False):
                self.autolabel(rects1, ax)
            self.autolabel(rects2, ax)
        ax.set_ylabel('Jahre')
        ax.set_title('Amortisationsübersicht')
        ax.legend(loc='best', bbox_to_anchor=(0.65, 1))
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.savefig('pics/bild1Tab3.jpg', bbox_extra_artists=(ax,), bbox_inches='tight', dpi=300)
        plt.close(fig)



    def testBar3_X(self):
        labels = ['Schwefeldioxid', 'Stickstoffdioxid', 'Staub', 'PM10', 'Kohlenmonoxid', 'Kohlendioxid', 'Lachgas', 'Methan', 'NMVOC', 'Quecksilber' ]
        bestand = [(round(self.b.verbrauchAlt * (emiTable.emi.Schwefeldioxid / 1000), 0)), (round(self.b.verbrauchAlt * (emiTable.emi.Stickstoffdioxid / 1000), 0)),
                   (round(self.b.verbrauchAlt * (emiTable.emi.Staub / 1000), 0)), (round(self.b.verbrauchAlt * (emiTable.emi.PM10 / 1000), 0)),
                    (round(self.b.verbrauchAlt * (emiTable.emi.Kohlenmonoxid / 1000), 0)), (round(self.b.verbrauchAlt * (emiTable.emi.Kohlendioxid/ 1000), 0)),
                   (round(self.b.verbrauchAlt * (emiTable.emi.Lachgas / 1000), 0)), (round(self.b.verbrauchAlt * (emiTable.emi.Methan / 1000), 0)),
                   (round(self.b.verbrauchAlt * (emiTable.emi.NMVOC / 1000), 0)), (round(self.b.verbrauchAlt * (emiTable.emi.Quecksilber / 1000), 0))]
        neueLeuchten = [(round(self.b.verbrauchNeu * (emiTable.emi.Schwefeldioxid / 1000), 0)), (round(self.b.verbrauchNeu * (emiTable.emi.Stickstoffdioxid / 1000), 0)),
                   (round(self.b.verbrauchNeu * (emiTable.emi.Staub / 1000), 0)), (round(self.b.verbrauchNeu * (emiTable.emi.PM10 / 1000), 0)),
                    (round(self.b.verbrauchNeu * (emiTable.emi.Kohlenmonoxid / 1000), 0)), (round(self.b.verbrauchNeu * (emiTable.emi.Kohlendioxid/ 1000), 0)),
                   (round(self.b.verbrauchNeu * (emiTable.emi.Lachgas / 1000), 0)), (round(self.b.verbrauchNeu * (emiTable.emi.Methan / 1000), 0)),
                   (round(self.b.verbrauchNeu * (emiTable.emi.NMVOC / 1000), 0)), (round(self.b.verbrauchNeu * (emiTable.emi.Quecksilber / 1000), 0))]
        neueLeuchtenMitLIMAS = [(round(self.b.GesamtverbrauchInkW * (emiTable.emi.Schwefeldioxid / 1000), 0)), (round(self.b.GesamtverbrauchInkW * (emiTable.emi.Stickstoffdioxid / 1000), 0)),
                   (round(self.b.GesamtverbrauchInkW * (emiTable.emi.Staub / 1000), 0)), (round(self.b.GesamtverbrauchInkW * (emiTable.emi.PM10 / 1000), 0)),
                    (round(self.b.GesamtverbrauchInkW * (emiTable.emi.Kohlenmonoxid / 1000), 0)), (round(self.b.GesamtverbrauchInkW * (emiTable.emi.Kohlendioxid/ 1000), 0)),
                   (round(self.b.GesamtverbrauchInkW * (emiTable.emi.Lachgas / 1000), 0)), (round(self.b.GesamtverbrauchInkW * (emiTable.emi.Methan / 1000), 0)),
                   (round(self.b.GesamtverbrauchInkW * (emiTable.emi.NMVOC / 1000), 0)), (round(self.b.GesamtverbrauchInkW * (emiTable.emi.Quecksilber / 1000), 0))]
        x = np.arange(len(labels))  # the label locations
        fig, ax = plt.subplots()
        rects1 = ax.bar(x - 0.25, bestand, 0.25, label='Bestand')
        rects2 = ax.bar(x, neueLeuchten, 0.25, label='Schuch-Leuchten')
        rects3 = ax.bar(x + 0.25, neueLeuchtenMitLIMAS, 0.25, label='mit ' + self.platzHalter)
        #rects1 = ax.bar(x, bestand, 0.85, label='Bestand')
        #rects2 = ax.bar(x, neueLeuchten, 0.55, label='Schuch-Leuchten')
        #rects3 = ax.bar(x, neueLeuchtenMitLIMAS, 0.25, label='mit LIMAS')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Emission')
        ax.set_title('Übersicht Emissionen')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        self.autolabel(rects1, ax)
        self.autolabel(rects2, ax)
        self.autolabel(rects3, ax)
        plt.savefig('pics/bild1Tab4.jpg', bbox_extra_artists=(ax,), bbox_inches='tight', dpi=300)
        fig.tight_layout()

    def autolabel(self, rects, ax):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(round(height, 1)),
                        xy=(rect.get_x() + rect.get_width() / 2, rect.get_y() + (height / 2)),
                        xytext=(0, -1),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='center')


    def openPLT1(self, myPic, bezeichnung):
        # activate the pygame library .
        # initiate pygame and give permission
        # to use pygame's functionality.
        pygame.init()
        # define the RGB value
        # for white colour
        white = (255, 255, 255)
        # assigning values to X and Y variable
        X = 1105
        Y = 650
        # create the display surface object
        # of specific dimension..e(X, Y).
        display_surface = pygame.display.set_mode((X, Y))
        # set the pygame window name
        pygame.display.set_caption(bezeichnung)
        # create a surface object, image is drawn on it.
        image = pygame.image.load(myPic)
        image = pygame.transform.scale(image, (1105, 650))
        # completely fill the surface object
        # with white colour
        display_surface.fill(white)
        # copying the image surface object
        # to the display surface object at
        # (0, 0) coordinate.
        display_surface.blit(image, (0, 0))
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return pygame.quit()
            pygame.display.update()
        pygame.display.quit()
        pygame.quit()

    def saveAll(self, t):
        with open("projekte/"+self.b.projektname +".pkl", "wb") as f:
            pickle.dump(t, f, pickle.HIGHEST_PROTOCOL)
        LIMASCalc.window1.infoPopUp("Hinweis", "Die Eingaben wurden erfolgreich unter \"" + self.b.projektname + ".pkl\" im Ordner " + os.path.dirname(sys.argv[0]) + "/projekte gespeichert", "Hinweis")



    def writeToLabel(self):
        self.y.label_56.setText(str(round(self.b.stromUndReparaturAlt, 2)))
        self.y.label_62.setText(str(round(self.b.stromUndReparaturNeu, 2)))
        self.y.label_91.setText(str(round(self.b.ersparnisAltNeuMinusZusatzkosten, 2)))
        self.y.label_135.setText(str(round(self.b.Gesamtkosten, 2)))
        self.y.label_61.setText(str(round(self.b.AmortisationszeitraumInJahren, 2)))
        #self.y.label_59.setText(str(round(self.b.AmortisationszeitraumInMonaten, 2)))
        #Window Nr.2
        self.y.label_136.setText(str(round(self.b.minusJährlicheZusatzkosten, 2)))
        self.y.label_59.setText(str(round(self.b.gesamtInJahren, 2)))
        #window Nr.3
        self.y.label_76.setText(str(round(self.b.stromUndReparaturAlt, 2)))
        self.y.label_82.setText(str(round(self.b.stromUndReparaturNeu, 2)))
        self.y.label_85.setText(str(round(self.b.Gesamtkosten, 2)))
        #window Nr.4
        self.y.tableWidget_3.setItem(0, 0, QTableWidgetItem(str(round(self.b.AmortisationszeitraumInJahren, 2))))
        self.y.tableWidget_3.setItem(0, 1, QTableWidgetItem(str(round(self.b.AmortisationszeitraumInMonaten, 2))))
        self.y.tableWidget_3.setItem(1, 0, QTableWidgetItem(str(round(self.b.gesamtInJahren, 2))))
        self.y.tableWidget_3.setItem(1, 1, QTableWidgetItem(str(round(self.b.gesamtInMonaten, 2))))
        self.y.tableWidget_3.setItem(2, 0, QTableWidgetItem(str(round(self.b.amortisationNurLIMASinJahren, 2))))
        self.y.tableWidget_3.setItem(2, 1, QTableWidgetItem(str(round(self.b.amortisationNurLIMASinMonaten, 2))))
        # window Nr. 5
        #---spalte_1
        self.y.tableWidget_2.setItem(0, 0, QTableWidgetItem(str(round(self.b.verbrauchAlt * (emiTable.emi.Schwefeldioxid/1000), 3))))
        self.y.tableWidget_2.setItem(1, 0, QTableWidgetItem(str(round(self.b.verbrauchAlt * (emiTable.emi.Stickstoffdioxid/1000), 3))))
        self.y.tableWidget_2.setItem(2, 0, QTableWidgetItem(str(round(self.b.verbrauchAlt * (emiTable.emi.Staub/1000), 3))))
        self.y.tableWidget_2.setItem(3, 0, QTableWidgetItem(str(round(self.b.verbrauchAlt * (emiTable.emi.PM10/1000), 3))))
        self.y.tableWidget_2.setItem(4, 0, QTableWidgetItem(str(round(self.b.verbrauchAlt * (emiTable.emi.Kohlenmonoxid/1000), 3))))
        self.y.tableWidget_2.setItem(5, 0, QTableWidgetItem(str(round(self.b.verbrauchAlt * (emiTable.emi.Kohlendioxid), 3))))
        self.y.tableWidget_2.setItem(6, 0, QTableWidgetItem(str(round(self.b.verbrauchAlt * (emiTable.emi.Lachgas/1000), 3))))
        self.y.tableWidget_2.setItem(7, 0, QTableWidgetItem(str(round(self.b.verbrauchAlt * (emiTable.emi.Methan/1000), 3))))
        self.y.tableWidget_2.setItem(8, 0, QTableWidgetItem(str(round(self.b.verbrauchAlt * (emiTable.emi.NMVOC/1000), 3))))
        self.y.tableWidget_2.setItem(9, 0, QTableWidgetItem(str(round(self.b.verbrauchAlt * (emiTable.emi.Quecksilber/1000), 3))))
        #----spalte_2
        self.y.tableWidget_2.setItem(0, 1, QTableWidgetItem(str(round(self.b.verbrauchNeu * (emiTable.emi.Schwefeldioxid/1000), 3))))
        self.y.tableWidget_2.setItem(1, 1, QTableWidgetItem(str(round(self.b.verbrauchNeu * (emiTable.emi.Stickstoffdioxid/1000), 3))))
        self.y.tableWidget_2.setItem(2, 1, QTableWidgetItem(str(round(self.b.verbrauchNeu * (emiTable.emi.Staub/1000), 3))))
        self.y.tableWidget_2.setItem(3, 1, QTableWidgetItem(str(round(self.b.verbrauchNeu * (emiTable.emi.PM10/1000), 3))))
        self.y.tableWidget_2.setItem(4, 1, QTableWidgetItem(str(round(self.b.verbrauchNeu * (emiTable.emi.Kohlenmonoxid/1000), 3))))
        self.y.tableWidget_2.setItem(5, 1, QTableWidgetItem(str(round(self.b.verbrauchNeu * emiTable.emi.Kohlendioxid, 3))))
        self.y.tableWidget_2.setItem(6, 1, QTableWidgetItem(str(round(self.b.verbrauchNeu * (emiTable.emi.Lachgas/1000), 3))))
        self.y.tableWidget_2.setItem(7, 1, QTableWidgetItem(str(round(self.b.verbrauchNeu * (emiTable.emi.Methan/1000), 3))))
        self.y.tableWidget_2.setItem(8, 1, QTableWidgetItem(str(round(self.b.verbrauchNeu * (emiTable.emi.NMVOC/1000), 3))))
        self.y.tableWidget_2.setItem(9, 1, QTableWidgetItem(str(round(self.b.verbrauchNeu * (emiTable.emi.Quecksilber/1000), 3))))
        # ----spalte_3
        self.y.tableWidget_2.setItem(0, 2, QTableWidgetItem(str(round(self.b.GesamtverbrauchInkW * (emiTable.emi.Schwefeldioxid / 1000), 3))))
        self.y.tableWidget_2.setItem(1, 2, QTableWidgetItem(str(round(self.b.GesamtverbrauchInkW * (emiTable.emi.Stickstoffdioxid / 1000), 3))))
        self.y.tableWidget_2.setItem(2, 2, QTableWidgetItem(str(round(self.b.GesamtverbrauchInkW * (emiTable.emi.Staub / 1000), 3))))
        self.y.tableWidget_2.setItem(3, 2, QTableWidgetItem(str(round(self.b.GesamtverbrauchInkW * (emiTable.emi.PM10 / 1000), 3))))
        self.y.tableWidget_2.setItem(4, 2, QTableWidgetItem(str(round(self.b.GesamtverbrauchInkW * (emiTable.emi.Kohlenmonoxid / 1000), 3))))
        self.y.tableWidget_2.setItem(5, 2, QTableWidgetItem(str(round(self.b.GesamtverbrauchInkW * emiTable.emi.Kohlendioxid, 3))))
        self.y.tableWidget_2.setItem(6, 2, QTableWidgetItem(str(round(self.b.GesamtverbrauchInkW * (emiTable.emi.Lachgas / 1000), 3))))
        self.y.tableWidget_2.setItem(7, 2, QTableWidgetItem(str(round(self.b.GesamtverbrauchInkW * (emiTable.emi.Methan / 1000), 3))))
        self.y.tableWidget_2.setItem(8, 2, QTableWidgetItem(str(round(self.b.GesamtverbrauchInkW * (emiTable.emi.NMVOC / 1000), 3))))
        self.y.tableWidget_2.setItem(9, 2, QTableWidgetItem(str(round(self.b.GesamtverbrauchInkW * (emiTable.emi.Quecksilber / 1000), 3))))
        # ende zeichne alles
        self.testBar()
        self.testBar1()
        self.testBar2()
        self.changeRowTable()
        self.refreshAllPics()
        self.show_pic('pics/bild1Tab.jpg', self.y.label_78)
        self.show_pic('pics/bild1Tab2.jpg', self.y.label_37)
        self.show_pic('pics/bild1Tab3.jpg', self.y.label_39)
        #splash.close()


    def showZoom(self):
        self.y.pushButton_7.setIcon(QIcon('pics/zoom.webp'))
        self.y.pushButton_9.setIcon(QIcon('pics/zoom.webp'))
        self.y.pushButton_10.setIcon(QIcon('pics/zoom.webp'))
        self.y.pushButton_11.setIcon(QIcon('pics/zoom.webp'))
        self.y.pushButton_12.setIcon(QIcon('pics/Information_icon.svg'))
        self.y.pushButton_23.setIcon(QIcon('pics/Information_icon.svg'))
        self.y.pushButton_13.setIcon(QIcon('pics/frage.png'))
        self.y.pushButton_20.setIcon(QIcon('pics/config_icon.jpg'))
        self.y.pushButton_21.setIcon(QIcon('pics/config_icon.jpg'))
        self.y.pushButton_22.setIcon(QIcon('pics/config_icon.jpg'))
        self.y.pushButton_14.setIcon(QIcon('pics/frage.png'))
        self.y.pushButton_15.setIcon(QIcon('pics/frage.png'))
        self.y.pushButton_16.setIcon(QIcon('pics/frage.png'))
        self.y.pushButton_18.setIcon(QIcon('pics/frage.png'))
        self.y.pushButton_5.setIcon(QIcon('pics/pfeil_rechts.png'))
#        self.y.pushButton_23.setIcon(QIcon('pics/config_icon.jpg'))


    def switchFrame(self):
        if self.y.toolBox.currentIndex() == 0:
            self.y.stackedWidget.setCurrentIndex(0)
        if self.y.toolBox.currentIndex() == 1:
            self.y.stackedWidget.setCurrentIndex(1)
        if self.y.toolBox.currentIndex() == 2:
            self.y.stackedWidget.setCurrentIndex(2)
        if self.y.toolBox.currentIndex() == 3:
            self.y.stackedWidget.setCurrentIndex(3)
        if self.y.toolBox.currentIndex() == 4:
            self.y.stackedWidget.setCurrentIndex(4)

    def berechnungWerte(self):
        QApplication.setOverrideCursor(
            Qt.WaitCursor)
        a = myData.myData(tTab1, tTab2, tTab3)
        a = self.investKosten(a)
        a = self.berechnungOhneLMS(a)
        a = self.anteilSteuerung(a)
        a = self.verbrauchLeuchten(a)
        a = self.bewegungsmelderVerbrauchOFeiertage(a)
        a = self.tageslichtabhRegelungVerbrauchProJahrOhneFeiertage(a)
        a = self.keineSteuerungOderRegelungOhneFeiertage(a)
        a = self.mitLMS(a)
        a = self.amortisationMitLMS(a)
        a = self.amortisationLMSselbst(a)
        self.b = a
        self.switchLIMAS()
        self.writeToLabel()
        QApplication.restoreOverrideCursor()
        print("Hier die Art:" + str(a.art))
        #self.b.printAllValue()


    def berechnungOhneLMS(self, t):
        if t.neueAnlage == False:
            t.stromUndReparaturAlt = 0
        else:
            t.stromUndReparaturAlt = ((t.altLeistung/1000) * t.altAnzahl * t.althProT * t.alttProJ * t.strompreis) + t.altWartung
        t.verbrauchAlt = ((t.altLeistung / 1000) * t.altAnzahl * t.althProT * t.alttProJ)
        t.verbrauchNeu = ((t.neuLeistung / 1000) * t.neuAnzahl * t.neuhProT * t.neutProJ)
        t.stromUndReparaturNeu = ((t.neuLeistung/1000) * t.neuAnzahl * t.neuhProT * t.neutProJ * t.strompreis) + t.neuWartung
        t.ersparnisAltNeu = t.stromUndReparaturAlt - t.stromUndReparaturNeu
        if t.neueAnlage == False:
            t.ersparnisAltNeuMinusZusatzkosten = 0
            t.AmortisationszeitraumInJahren = 0
            t.AmortisationszeitraumInMonaten = 0
        else:
            t.ersparnisAltNeuMinusZusatzkosten = t.ersparnisAltNeu
            t.AmortisationszeitraumInJahren = t.gesamtInvestitionsKosten/t.ersparnisAltNeuMinusZusatzkosten
            t.AmortisationszeitraumInMonaten = t.AmortisationszeitraumInJahren * 12

        return t

    def investKosten(self, t):
        t.investKosten = t.neuAnschaffungskosten * t.neuAnzahl
        t.gesamtInvestitionsKosten = t.investKosten + t.installationsKosten
        return t

    def anteilSteuerung(self, t):
        t.anteilBewegungsmelder = myTab3.anteilBewe
        t.anteilTageslichtabhSteuerung = myTab3.anteilLicht
        print(str(t.anteilTageslichtabhSteuerung)+"---anteilTageslichtabhSteuerung---")
        print(str(t.anteilBewegungsmelder) + "---anteilBewegungsmelder---")
        t.anteilKeineStoderReg = t.neuAnzahl - t.anteilBewegungsmelder - t.anteilTageslichtabhSteuerung
        print(str(t.anteilBewegungsmelder) + "---anteilKeineStoderReg---")
        return t

    def verbrauchLeuchten(self, t):
        t.verbrauchOhneLMS = t.neuLeistung/1000
        t.verbrauchMitAbwesenheitswert = t.verbrauchOhneLMS * (t.abwesenheitswert/100)
        t.verbrauchMitAnwesenheitswert = t.verbrauchOhneLMS * (t.anwesenheitswert / 100)
        t.verbrauchMitTageslichtreduzierung = t.verbrauchOhneLMS * (t.reduzierungsNiveau / 100)
        return t

    def bewegungsmelderVerbrauchOFeiertage(self, t):
        t.frequentierungGesamt = t.frequentierungStunden + t.frequentierungMinuten/60
        t.verbrauchGesamtAbwesenheitswert = t.verbrauchMitAbwesenheitswert * t.anteilBewegungsmelder * (t.neuhProT-t.frequentierungGesamt) * (t.neutProJ-t.anzahlAnAus)
        t.verbrauchGesamtAnwesenheitswert = t.verbrauchMitAnwesenheitswert * t.anteilBewegungsmelder * t.frequentierungGesamt * (t.neutProJ-t.anzahlAnAus) #* (t.bewegungsmelderTageslichtwert/100)
        #t.verbrauchGesamtAbwesenheitswert = t.verbrauchMitAbwesenheitswert * (t.neuhProT-t.frequentierungGesamt) * ((t.anteilBewegungsmelder * t.neuAnzahl)/100) * (t.neutProJ-t.anzahlAnAus)
        #t.verbrauchGesamtAnwesenheitswert = t.verbrauchMitAnwesenheitswert * t.frequentierungGesamt * (t.anteilBewegungsmelder/100 * t.neuAnzahl) * (t.neutProJ - t.anzahlAnAus)
        t.verbrauchGesamtDurchBewegungsmelderLeuchten = t.verbrauchGesamtAbwesenheitswert + t.verbrauchGesamtAnwesenheitswert
        return t

    def tageslichtabhRegelungVerbrauchProJahrOhneFeiertage(self, t):
        t.tageslichtnutzungGesamt = t.tageslichtnutzungStunden + t.tageslichtnutzungMinuten/60
        t.tageslichtabhRegelungAn = t.verbrauchMitTageslichtreduzierung * t.anteilTageslichtabhSteuerung * t.tageslichtnutzungGesamt * (t.neutProJ-t.anzahlAnAus)
        t.tageslichtabhRegelungAus = t.verbrauchOhneLMS * t.anteilTageslichtabhSteuerung * (t.neuhProT - t.tageslichtnutzungGesamt) * (t.neutProJ - t.anzahlAnAus)
        t.tageslichtabhRegelungGesamtverbrauchProJahr = t.tageslichtabhRegelungAn + t.tageslichtabhRegelungAus
        return t

    def keineSteuerungOderRegelungOhneFeiertage(self, t):
        t.verbrauchRestlicheLeuchten = t.verbrauchOhneLMS * t.anteilKeineStoderReg * t.neuhProT * (t.neutProJ-t.anzahlAnAus)
        return t

    def mitLMS(self, t):
        t.GesamtverbrauchInkW = t.verbrauchGesamtDurchBewegungsmelderLeuchten + t.tageslichtabhRegelungGesamtverbrauchProJahr + t.verbrauchRestlicheLeuchten
        t.Gesamtkosten = t.GesamtverbrauchInkW * t.strompreis + t.neuLaufKosten + t.neuWartung #hier + t.neuLaufKosten + t.neuWartung hinzugefügt
        t.ErsparnisZuOhneLMS = t.stromUndReparaturNeu - t.Gesamtkosten
        print(str(t.tageslicht))
        t.minusJährlicheZusatzkosten = t.ErsparnisZuOhneLMS # hier - t.neuLaufKosten - t.neuWartung weggemacht
        if (t.bewegungsmelder == False) and (t.tageslicht == False) and (t.kalenderCheck == False):
            t.Gesamtkosten = 0
            t.minusJährlicheZusatzkosten = 0
        if t.bewegungsmelder == False:
            t.verbrauchMitAbwesenheitswert = t.verbrauchOhneLMS
            t.verbrauchMitAnwesenheitswert = t.verbrauchOhneLMS
            t.anteilBewegungsmelder = 0
            t.mehrkostenBewegungsmelder = 0
        if t.tageslicht == False:
            t.verbrauchMitTageslichtreduzierung = t.verbrauchOhneLMS
            t.anteilTageslichtabhSteuerung = 0
            t.mehrkostenTageslicht = 0
        if t.kalenderCheck == False:
            t.anzahlAnAus = 0
        return t

    def amortisationMitLMS(self, t):
        if ((t.bewegungsmelder != False) or (t.tageslicht != False) or (t.kalenderCheck != False)) and t.neueAnlage == True:
            t.gesamtInJahren = (t.neuLichtmanagement + t.mehrkostenBewegungsmelder + t.mehrkostenTageslicht + t.gesamtInvestitionsKosten + (t.aufpreisLMS * t.neuAnzahl)) / (t.minusJährlicheZusatzkosten + t.ersparnisAltNeuMinusZusatzkosten)
            t.gesamtInMonaten = t.gesamtInJahren * 12
        else:
            t.gesamtInJahren = 0
            t.gesamtInMonaten = 0
        return t

    def amortisationLMSselbst(self, t):
        if ((t.bewegungsmelder != False) or (t.tageslicht != False) or (t.kalenderCheck != False)) and t.minusJährlicheZusatzkosten!=0:
            t.amortisationNurLIMASinJahren = (t.neuLichtmanagement + t.mehrkostenBewegungsmelder + t.mehrkostenTageslicht + (t.aufpreisLMS * t.neuAnzahl))/t.minusJährlicheZusatzkosten
            t.amortisationNurLIMASinMonaten = t.amortisationNurLIMASinJahren * 12
        else:
            t.amortisationNurLIMASinJahren = 0
            t.amortisationNurLIMASinMonaten = 0
        return t



