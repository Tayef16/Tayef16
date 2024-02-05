import qrcode
from PIL import Image

qr=qrcode.QRCode(version=20,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=10, )
qr.add_data("https://chat.openai.com/")
qr.make(fit=True)
img=qr.make_image(fill_color="yellow",back_color="BLACK")
img.save("chatgpt.png")
