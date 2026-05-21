# Pip Install qrcode
# pip install image

import qrcode
import image

qr= qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data= "https://www.linkedin.com/in/h-amir-sohail-yazdan-maneka-6b4925256/"
# in link i add my Linkdin Profile Data

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black", back_color="white")
img.save("test.png")