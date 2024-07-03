
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
    img.save("qr_code.png")
    
    print("QR code generated successfully!")

input_data = input("Enter the data for QR code: ")
generate_qr_code(input_data)
