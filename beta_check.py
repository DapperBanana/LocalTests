
import qrcode

def generate_qr_code(input_text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_text)
    qr.make(fit=True)

    qr_code = qr.make_image(fill_color="black", back_color="white")
    qr_code.save("qrcode.png")
    print("QR code generated successfully!")

if __name__ == "__main__":
    input_text = input("Enter text to generate QR code: ")
    generate_qr_code(input_text)
