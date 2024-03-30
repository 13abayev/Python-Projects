import qrcode


def ConvertToQR(url : str, filename :str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")

    qr_image.save(filename) 



url = input("Please enter your url to convert to QR : ")
image_name = input("Please enter your image name to save it as : ")
filename = image_name + ".png"

ConvertToQR(url, filename)
