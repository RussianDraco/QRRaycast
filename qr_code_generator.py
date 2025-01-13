import qrcode

with open("mini.html", "r") as file:
    html_content = file.read()

qr = qrcode.QRCode(
    version=40,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(html_content)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

img.save("qr_code.png")
img.show()