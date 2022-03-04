import qrcode, image, sys, time, os

dir = os.path.dirname(os.path.abspath(__file__))

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(.1)

sprint('Cosa devo mettere nel codice QR?')
x = input()
if x == "textFile" :
  img= qrcode.make(textData)
else :
  img= qrcode.make(x)
img.save(dir + "\output-qr.png")