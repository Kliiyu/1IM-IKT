import qrcode


def CreateQR(data):
    img = qrcode.make(data)
    img.save("qrcode.png")
    img.show()


inputData = input("QRCode Data: ")
CreateQR(str(inputData))