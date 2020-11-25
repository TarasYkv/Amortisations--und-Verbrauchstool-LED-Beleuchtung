"""
LIMASCalc ist ein Programm zur Kostendarstellung und Amortisationsdarstellung eines Beleuchtungssystems
Copyright (C) [2020]  [Taras Yuzkiv, [IES] - Individual Engeneering Solutions & Adolf Schuch GmbH]
Dieses Programm ist freie Software. Sie können es unter den Bedingungen der GNU General Public License, wie von der Free Software Foundation veröffentlicht, weitergeben und/oder modifizieren, entweder gemäß Version 3 der Lizenz oder (nach Ihrer Option) jeder späteren Version.
Die Veröffentlichung dieses Programms erfolgt in der Hoffnung, daß es Ihnen von Nutzen sein wird, aber OHNE IRGENDEINE GARANTIE, sogar ohne die implizite Garantie der MARKTREIFE oder der VERWENDBARKEIT FÜR EINEN BESTIMMTEN ZWECK. Details finden Sie in der GNU General Public License.
Sie sollten ein Exemplar der GNU General Public License zusammen mit diesem Programm erhalten haben. Falls nicht, siehe <http://www.gnu.org/licenses/>.
"""
class myData:
    firmenname = "Platzhalter"
    projektname = "Platzhalter"
    strompreis = 0.0
    name = "Platzhalter"
    email = "Platzhalter"
    tel = 000
    zeitDatum = "meineZeitDatum"
    neueAnlage = False
    altHersteller = "Platzhalter"
    altModell = "Platzhalter"
    altLeistung = 0.0
    altAnschaffungskosten = 0.0
    altAnzahl = 0
    althProT = 0.0
    alttProJ = 0
    altWartung = 0.0
    altLaufKosten = 0.0
    neuHersteller = "Platzhalter"
    neuModell = "Platzhalter"
    neuLeistung = 0.0
    neuAnschaffungskosten = 0.0
    neuAnzahl = 0
    neuLichtmanagement = 0.0
    installationsKosten = 0.0
    neuhProT = 0.0
    neutProJ = 0.0
    neuWartung = 0.0
    neuLaufKosten = 0.0
    tageslicht = True
    bewegungsmelder = True
    bewegungsmelderExtra = True
    abwesenheitswert = 0
    anwesenheitswert = 0
    frequentierungStunden = 0.0
    frequentierungMinuten = 0.0
    mehrkostenBewegungsmelder = 0.0
    fadein = 0
    fadeout = 0
    tageslichtnutzung = 0.0
    reduzierungsNiveau = 0.0
    tageslichtnutzungStunden = 0.0
    tageslichtnutzungMinuten = 0.0
    mehrkostenTageslicht = 0.0
    kalenderCheck = True
    anzahlAnAus = 0
    aufpreisLMS = 0.0
    #------berechnete Daten-----
    verbrauchProJahrAlt = 0.0
    kostenProJahrAlt = 0.0
    stromUndReparaturAlt = 0.0
    stromUndReparaturNeu = 0.0
    ersparnisAltNeu = 0.0
    ersparnisAltNeuMinusZusatzkosten = 0.0
    investKosten = 0.0
    gesamtInvestitionsKosten = 0.0
    anteilBewegungsmelder = 0
    tageslichtnutzungGesamt = 0.0
    anteilTageslichtabhSteuerung = 0
    anteilKeineStoderReg = 0
    verbrauchOhneLMS = 0.0
    AmortisationszeitraumInJahren = 0.0
    AmortisationszeitraumInMonaten = 0.0
    verbrauchMitAbwesenheitswert = 0.0
    verbrauchMitAnwesenheitswert = 0.0
    verbrauchMitTageslichtreduzierung = 0.0
    verbrauchGesamtDurchBewegungsmelderLeuchten = 0.0
    tageslichtabhRegelungAn = 0.0
    tageslichtabhRegelungAus = 0.0
    frequentierungGesamt = 0.0
    tageslichtabhRegelungGesamtverbrauchProJahr = 0.0
    verbrauchRestlicheLeuchten = 0.0
    GesamtverbrauchInkW = 0.0
    Gesamtkosten = 0.0
    ErsparnisZuOhneLMS = 0.0
    minusJährlicheZusatzkosten = 0.0
    gesamtInJahren = 0.0
    gesamtInMonaten = 0.0
    verbrauchAlt = 0.0
    verbrauchNeu = 0.0
    amortisationNurLIMASinJahren = 0.0
    amortisationNurLIMASinMonaten = 0.0
    art = 0

    def __init__(self, tab1, tab2, tab3):
        self.firmenname = str(tab1["firmenname"])
        self.projektname = str(tab1["projektname"])
        self.strompreis = float(tab1["strompreis"])
        self.name = str(tab1["name"])
        self.email = str(tab1["email"])
        self.tel = str(tab1["tel"])
        self.zeitDatum = str(tab1["zeitDatum"])
        print(str((tab1["neueAnlage"])) + " hier ist myData")
        self.neueAnlage = (tab1["neueAnlage"])
        #tab1 ende
        self.altHersteller = str(tab2["altHersteller"])
        self.altModell = str(tab2["altModell"])
        self.altLeistung = float(tab2["altLeistung"])
        self.altAnschaffungskosten = 0.0
        self.altAnzahl = int(tab2["altAnzahl"])
        self.althProT = float(tab2["althProT"])
        self.alttProJ = int(tab2["alttProJ"])
        self.altWartung = float(tab2["altWartung"])
        self.altLaufKosten = float(tab2["altLaufKosten"])
        self.neuHersteller = tab2["neuHersteller"]
        self.neuModell = tab2["neuModell"]
        self.neuLeistung = float(tab2["neuLeistung"])
        self.neuAnschaffungskosten = float(tab2["neuAnschaffungskosten"])
        self.neuAnzahl = int(tab2["neuAnzahl"])
        self.neuLichtmanagement = float(tab2["neuLichtmanagement"])
        self.installationsKosten = float(tab2["installationsKosten"])
        self.neuhProT = float(tab2["neuhProT"])
        self.neutProJ = float(tab2["neutProJ"])
        self.neuWartung = float(tab2["neuWartung"])
        self.neuLaufKosten = float(tab2["neuLaufKosten"])
        self.aufpreisLMS = float(tab2["aufpreisLMS"])
        #print(self.neuLaufKosten)
        #tab2 Ende
        self.bewegungsmelder = (tab3["bewegungsmelder"])
        self.bewegungsmelderExtra = (tab3["bewegungsmelderExtra"])
        self.abwesenheitswert = int(tab3["abwesenheitswert"])
        self.anwesenheitswert = int(tab3["anwesenheitswert"])
        self.frequentierungStunden = (tab3["frequentierungStunden"])
        self.frequentierungMinuten = (tab3["frequentierungMinuten"])
        self.mehrkostenBewegungsmelder = float(tab3["mehrkostenBewegungsmelder"])
        self.fadein = int(tab3["fadein"])
        self.fadeout = int(tab3["fadeout"])
        self.tageslicht = (tab3["tageslicht"])
        self.reduzierungsNiveau = float(tab3["reduzierungsNiveau"])
        self.tageslichtnutzungStunden = float(tab3["tageslichtnutzungStunden"])
        self.tageslichtnutzungMinuten = float(tab3["tageslichtnutzungMinuten"])
        self.mehrkostenTageslicht = float(tab3["mehrkostenTageslicht"])
        self.anzahlAnAus = int(tab3["anzahlAnAus"])
        self.kalenderCheck = (tab3["kalenderCheck"])
        self.art = int(tab1["art"])
        #tab3 Ende

    def printAll(self):
        print(type(self.firmenname))
        print(type(self.projektname))
        print(type(self.strompreis))
        print(type(self.name))
        print(type(self.email))
        print(type(self.tel))
        print(type(self.zeitDatum))
        print(type(self.neueAnlage))
        print(type(self.altHersteller))
        print(type(self.altModell))
        print(type(self.altLeistung))
        print(type(self.altAnschaffungskosten))
        print(type(self.altAnzahl))
        print(type(self.althProT))
        print(type(self.alttProJ))
        print(type(self.altWartung))
        print(type(self.altLaufKosten))
        print(type(self.neuHersteller))
        print(type(self.neuModell))
        print(type(self.neuLeistung))
        print(type(self.neuAnschaffungskosten))
        print(type(self.neuAnzahl))
        print(type(self.neuLichtmanagement))
        print(type(self.installationsKosten))
        print(type(self.neuhProT))
        print(type(self.neutProJ))
        print(type(self.neuWartung))
        print(type(self.neuLaufKosten))
        print(type(self.bewegungsmelder))
        print(type(self.bewegungsmelderExtra))
        print(type(self.abwesenheitswert))
        print(type(self.anwesenheitswert))
        print(type(self.frequentierungGesamt))
        print(type(self.mehrkostenBewegungsmelder))
        print(type(self.fadein))
        print(type(self.fadeout))
        print(type(self.tageslicht))
        print(type(self.reduzierungsNiveau))
        print(type(self.tageslichtnutzung))
        print(type(self.mehrkostenTageslicht))
        print(type(self.anzahlAnAus))
        print(type(self.kalenderCheck))
        print(type(self.aufpreisLMS))
        #print(type(self.bewTaglichtWert))
        #bewTaglichtWert
        #print(type(self.gesamtkostenMinusJZusatzkosten))
        #print(dir(myData))

    def printAllValue(self):
        print("firmenname: " + str(self.firmenname))
        print("projektname: " + str(self.projektname))
        print("strompreis: " + str(self.strompreis))
        print("name: " + str(self.name))
        print("email: " + str(self.email))
        print("tel: " + str(self.tel))
        print("zeitDatum: " + str(self.zeitDatum))
        print("neueAnlage: " + str(self.neueAnlage))
        print("altHersteller: " + str(self.altHersteller))
        print("altModell: " + str(self.altModell))
        print("altLeistung: " + str(self.altLeistung))
        print("altAnschaffungskosten: " + str(self.altAnschaffungskosten))
        print("altAnzahl: " + str(self.altAnzahl))
        print("althProT: " + str(self.althProT))
        print("alttProJ: " + str(self.alttProJ))
        print("altWartung: " + str(self.altWartung))
        print("altLaufKosten: " + str(self.altLaufKosten))
        print("neuHersteller: " + str(self.neuHersteller))
        print("neuModell: " + str(self.neuModell))
        print("neuLeistung: " + str(self.neuLeistung))
        print("neuAnschaffungskosten: " + str(self.neuAnschaffungskosten))
        print("neuAnzahl: " + str(self.neuAnzahl))
        print("neuLichtmanagement: " + str(self.neuLichtmanagement))
        print("installationsKosten: " + str(self.installationsKosten))
        print("neuhProT: " + str(self.neuhProT))
        print("neutProJ: " + str(self.neutProJ))
        print("neuWartung: " + str(self.neuWartung))
        print("neuLaufKosten: " + str(self.neuLaufKosten))
        print("bewegungsmelder: " + str(self.bewegungsmelder))
        print("bewegungsmelderExtra: " + str(self.bewegungsmelderExtra))
        print("abwesenheitswert: " + str(self.abwesenheitswert))
        print("anwesenheitswert: " + str(self.anwesenheitswert))
        print("frequentierungGesamt: " + str(self.frequentierungGesamt))
        print("mehrkostenBewegungsmelder: " + str(self.mehrkostenBewegungsmelder))
        print("fadein: " + str(self.fadein))
        print("fadeout: " + str(self.fadeout))
        print("tageslicht: " + str(self.tageslicht))
        print("reduzierungsNiveau: " + str(self.reduzierungsNiveau))
        print("tageslichtnutzung: " + str(self.tageslichtnutzung))
        print("mehrkostenTageslicht: " + str(self.mehrkostenTageslicht))
        print("anzahlAnAus: " + str(self.anzahlAnAus))
        print("verbrauchProJahrAlt: " + str(self.verbrauchProJahrAlt))
        print("kostenProJahrAlt: " + str(self.kostenProJahrAlt))
        print("stromUndReparaturAlt: " + str(self.stromUndReparaturAlt))
        print("stromUndReparaturNeu: " + str(self.stromUndReparaturNeu))
        print("ersparnisAltNeu: " + str(self.ersparnisAltNeu))
        print("ersparnisAltNeuMinusZusatzkosten: " + str(self.ersparnisAltNeuMinusZusatzkosten))
        print("investKosten: " + str(self.investKosten))
        print("gesamtInvestitionsKosten: " + str(self.gesamtInvestitionsKosten))
        print("anteilBewegungsmelder: " + str(self.anteilBewegungsmelder))
        print("anteilTageslichtabhSteuerung: " + str(self.anteilTageslichtabhSteuerung))
        print("anteilKeineStoderReg: " + str(self.anteilKeineStoderReg))
        print("verbrauchOhneLMS: " + str(self.verbrauchOhneLMS))
        print("verbrauchMitAbwesenheitswert: " + str(self.verbrauchMitAbwesenheitswert))
        print("verbrauchMitAnwesenheitswert: " + str(self.verbrauchMitAnwesenheitswert))
        print("verbrauchMitTageslichtreduzierung: " + str(self.verbrauchMitTageslichtreduzierung))
        print("verbrauchGesamtDurchBewegungsmelderLeuchten: " + str(self.verbrauchGesamtDurchBewegungsmelderLeuchten))
        print("tageslichtabhRegelungAn: " + str(self.tageslichtabhRegelungAn))
        print("tageslichtabhRegelungAus: " + str(self.tageslichtabhRegelungAus))
        print("tageslichtabhRegelungGesamtverbrauchProJahr: " + str(self.tageslichtabhRegelungGesamtverbrauchProJahr))
        print("verbrauchRestlicheLeuchten: " + str(self.verbrauchRestlicheLeuchten))
        print("GesamtverbrauchInkW: " + str(self.GesamtverbrauchInkW))
        print("Gesamtkosten: " + str(self.Gesamtkosten))
        print("ErsparnisZuOhneLMS: " + str(self.ErsparnisZuOhneLMS))
        print("minusJährlicheZusatzkosten: " + str(self.minusJährlicheZusatzkosten))
        print("gesamtInJahren: " + str(self.gesamtInJahren))
        print("gesamtInMonaten: " + str(self.gesamtInMonaten))
        print("AmortisationszeitraumInJahren: " + str(self.AmortisationszeitraumInJahren))
        print("AmortisationszeitraumInMonaten: " + str(self.AmortisationszeitraumInMonaten))
        print("kalenderCheck: " + str(self.kalenderCheck))
        print("aufpreisLMS: " + str(self.aufpreisLMS))
        #print("bewTaglichtWert: " + str(self.bewTaglichtWert))


    def getAllValue(self, b):
        r = str(str("firmenname: ") + str(b.firmenname) + "\n" +
        str("projektname: ") + str(b.projektname) + "\n" +
        str("strompreis: ") + str(b.strompreis) + "\n" +
        str("name: ") + str(b.name) + "\n" +
        str("email: ") + str(b.email) + "\n" +
        str("tel: ") + str(b.tel) + "\n" +
        str("zeitDatum: ") + str(b.zeitDatum) + "\n" +
        str("neueAnlage: ") + str(b.neueAnlage) + "\n" +
        str("altHersteller: ") + str(b.altHersteller) + "\n" +
        str("altModell: ") + str(b.altModell) + "\n" +
        str("altLeistung: ") + str(b.altLeistung) + "\n" +
        str("altAnschaffungskosten: ") + str(b.altAnschaffungskosten) + "\n" +
        str("altAnzahl: ") + str(b.altAnzahl) + "\n" +
        str("althProT: ") + str(b.althProT) + "\n" +
        str("alttProJ: ") + str(b.alttProJ) + "\n" +
        str("altLaufKosten: ") + str(b.altLaufKosten) + "\n" +
        str("neuHersteller: ") + str(b.neuHersteller) + "\n" +
        str("neuModell: ") + str(b.neuModell) + "\n" +
        str("neuLeistung: ") + str(b.neuLeistung) + "\n" +
        str("neuAnschaffungskosten: ") + str(b.neuAnschaffungskosten) + "\n" +
        str("neuAnzahl: ") + str(b.neuAnzahl) + "\n" +
        str("neuLichtmanagement: ") + str(b.neuLichtmanagement) + "\n" +
        str("installationsKosten: ") + str(b.installationsKosten) + "\n" +
        str("neuhProT: ") + str(b.neuhProT) + "\n" +
        str("neutProJ: ") + str(b.neutProJ) + "\n" +
        str("neuWartung: ") + str(b.neuWartung) + "\n" +
        str("neuLaufKosten: ") + str(b.neuLaufKosten) + "\n" +
        str("bewegungsmelder: ") + str(b.bewegungsmelder) + "\n" +
        str("bewegungsmelderExtra: ") + str(b.bewegungsmelderExtra) + "\n" +
        str("abwesenheitswert: ") + str(b.abwesenheitswert) + "\n" +
        str("anwesenheitswert: ") + str(b.anwesenheitswert) + "\n" +
        str("frequentierungGesamt: ") + str(b.frequentierungGesamt) + "\n" +
        str("mehrkostenBewegungsmelder: ") + str(b.mehrkostenBewegungsmelder) + "\n" +
        str("fadein: ") + str(b.fadein) + "\n" +
        str("fadeout: ") + str(b.fadeout) + "\n" +
        str("tageslicht: ") + str(b.tageslicht) + "\n" +
        str("reduzierungsNiveau: ") + str(b.reduzierungsNiveau) + "\n" +
        str("tageslichtnutzung: ") + str(b.tageslichtnutzung) + "\n" +
        str("mehrkostenTageslicht: ") + str(b.mehrkostenTageslicht) + "\n" +
        str("anzahlAnAus: ") + str(b.anzahlAnAus) + "\n" +
        str("verbrauchProJahrAlt: ") + str(b.verbrauchProJahrAlt) + "\n" +
        str("kostenProJahrAlt: ") + str(b.kostenProJahrAlt) + "\n" +
        str("stromUndReparaturAlt: ") + str(b.stromUndReparaturAlt) + "\n" +
        str("stromUndReparaturNeu: ") + str(b.stromUndReparaturNeu) + "\n" +
        str("ersparnisAltNeu: ") + str(b.ersparnisAltNeu) + "\n" +
        str("ersparnisAltNeuMinusZusatzkosten: ") + str(b.ersparnisAltNeuMinusZusatzkosten) + "\n" +
        str("investKosten: ") + str(b.investKosten) + "\n" +
        str("gesamtInvestitionsKosten: ") + str(b.gesamtInvestitionsKosten) + "\n" +
        str("anteilBewegungsmelder: ") + str(b.anteilBewegungsmelder) + "\n" +
        str("anteilTageslichtabhSteuerung: ") + str(b.anteilTageslichtabhSteuerung) + "\n" +
        str("anteilKeineStoderReg: ") + str(b.anteilKeineStoderReg) + "\n" +
        str("verbrauchOhneLMS: ") + str(b.verbrauchOhneLMS) + "\n" +
        str("verbrauchMitAbwesenheitswert: ") + str(b.verbrauchMitAbwesenheitswert) + "\n" +
        str("verbrauchMitAnwesenheitswert: ") + str(b.verbrauchMitAnwesenheitswert) + "\n" +
        str("verbrauchMitTageslichtreduzierung: ") + str(b.verbrauchMitTageslichtreduzierung) + "\n" +
        str("verbrauchGesamtDurchBewegungsmelderLeuchten: ") + str(b.verbrauchGesamtDurchBewegungsmelderLeuchten) + "\n" +
        str("tageslichtabhRegelungAn: ") + str(b.tageslichtabhRegelungAn) + "\n" +
        str("tageslichtabhRegelungAus: ") + str(b.tageslichtabhRegelungAus) + "\n" +
        str("tageslichtabhRegelungGesamtverbrauchProJahr: ") + str(b.tageslichtabhRegelungGesamtverbrauchProJahr) + "\n" +
        str("verbrauchRestlicheLeuchten: ") + str(b.verbrauchRestlicheLeuchten) + "\n" +
        str("GesamtverbrauchInkW: ") + str(b.GesamtverbrauchInkW) + "\n" +
        str("Gesamtkosten: ") + str(b.Gesamtkosten) + "\n" +
        str("ErsparnisZuOhneLMS: ") + str(b.ErsparnisZuOhneLMS) + "\n" +
        str("minusJährlicheZusatzkosten: ") + str(b.minusJährlicheZusatzkosten) + "\n" +
        str("gesamtInJahren: ") + str(b.gesamtInJahren) + "\n" +
        str("gesamtInMonaten: ") + str(b.gesamtInMonaten) + "\n" +
        str("AmortisationszeitraumInJahren: ") + str(b.AmortisationszeitraumInJahren) + "\n" +
        str("AmortisationszeitraumInMonaten: ") + str(b.AmortisationszeitraumInMonaten) + "\n" +
        str("kalenderCheck: ") + str(b.kalenderCheck)+ "\n" +
        str("aufpreisLMS: ") + str(b.aufpreisLMS))
        #str("bewTaglichtWert: ") + str(b.bewTaglichtWert))
        return r