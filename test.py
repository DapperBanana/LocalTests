
import qrcode

def generate_qr(input_data):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(input_data)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save("qrcode.png")

    print("QR code generated successfully!")

if __name__ == "__main__":
    input_data = input("Enter the data for which you want to generate a QR code: ")
    generate_qr(input_data)
