
import qrcode

def generate_qr_code(input_data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")
    print("QR code generated and saved as qrcode.png")

if __name__ == "__main__":
    input_data = input("Enter text or URL to generate QR code: ")
    generate_qr_code(input_data)
