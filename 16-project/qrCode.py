#Install: "pip install PyQRCode"
import pyqrcode

userInputURL = str(input("Enter a URL to generate QR-code: \n "))

QR = pyqrcode.create(userInputURL)

QR.svg('wbQR.svg', scale=8)
QR.eps('wbQR.png', scale=8)

print(QR.terminal(quiet_zone=1))
