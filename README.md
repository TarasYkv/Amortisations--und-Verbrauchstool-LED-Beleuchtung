# Amortisations--und-Verbrauchstool-LED-Beleuchtung

# Was macht dieses Tool
Hierbei handelt es sich um ein Tool, welches dem Anwender folgende Möglichkeiten bietet:
- Verbrauch von LED-Leuchte
- Vergleich von konventioneollen Leuchten mit LED-Leuchten
- Amortisation von LED-Leuchten
- Verbrauch von LED-Leuchten mit Lichtmanagement 
- Amortisation von LED-Leuchten mit Lichtmanagement
- Erstellung einer .doc mit allen Informationen
- Erstellung und zusammensetzung einer .pdf mit allen Informationen
- Emissionsersparnis durch LED-Leuchten und Lichtmanagenet

Die App ist mit Python 3.7 implementiert worden. Die GUI ist mit PyQt5 umgesetzt worden.

# Aufbau der APP
Die App besteht insgesamt aus 5 Tabs. Man wird vom ersten bis zum letzten Tab entlang gefuhrt. Es ist nicht möglich Tabs zu überspringen. Durch die Buttons "zurück" und "weiter" kann zwischen den Tabs navigiert werden. Den Anwender kann in der App die Ergebnisse einsehen und diese anschließend in Form einer .pdf ausgeben.

# Installation
Um die Bedienung möglichst einfach zu gestalten, wird dieses Tool als eine .exe zur verfügung gestellt. Diese .exe ist eine Installationsdatei welche ohne Adminrechte installiert werden kann. Die Installationsdatei wird durch "auto-py-to-exe" und "Inno Setup Compiler" erzeugt. 

# Updates
Beim Programstart wird überprüft ob die ausgeführte Version die aktuellste ist. Falls nein, wird die aktuellste Version vom Server Heruntergeladen, die installierte Version wird deinstalliert und die heruntergeladene installiert.
