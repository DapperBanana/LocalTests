
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

    qr_code_img = qr.make_image(fill_color="black", back_color="white")
    qr_code_img.save("qr_code.png")

input_data = input("Enter data for QR code generation: ")
generate_qr_code(input_data)
print("QR code generated successfully.")
