#Prerequisites: 
#pip3 install qrcode Image

import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECTION_L,
    )
