#Prerequisites: 
#pip3 install qrcode Image

import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", black_color="white")
    img.save("qrimg.png")

url = input("Enter your url: ")
generate_qrcode(url) 