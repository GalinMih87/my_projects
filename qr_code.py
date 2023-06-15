import pyqrcode
import png
from pyqrcode import QRCode

adres = "https://www.imot.bg/pcgi/imot.cgi?act=5&adv=1e164083412037828&slink=7n7f8r&f1=1"
url = pyqrcode.create(adres)
url.png('Apartament.png', scale=8)



