import pyqrcode

url = input("Qr kod yapmak istediğiniz url girin:")

qrCode=pyqrcode.create(url)
qrCode.svg("qr.svg")
