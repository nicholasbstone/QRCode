import qrcode

img = qrcode.make("Hello World! This is Nicholas Stone.")
img.save("mycode.png")