import qrcode

im = qrcode.make("https://www.linkedin.com/in/pardaz-banu/")
im.save("qr3.png", "PNG")