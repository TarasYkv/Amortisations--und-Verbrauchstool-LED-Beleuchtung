import io
import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
import urllib3
import urllib.request

app = QApplication(sys.argv)

web = QWebEngineView()
meineURL = "https://"+"www.google.de"
web.load(QUrl(meineURL))



http = urllib3.PoolManager()
r = http.request('GET', meineURL)
file = urllib.request.urlopen(meineURL)

print("Size: " + str(len(file.read())) + " Byte")
print("URL: " + meineURL)
print("Status: " + str(r.status))
print("Method: " + str(r.headers))
print("Data: " + str(r.data))

web.show()
web.resize(1640, 480)
sys.exit(app.exec_())