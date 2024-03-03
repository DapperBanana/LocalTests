
import qrcode

def generate_qr_code(input_text, output_file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

input_text = input("Enter the text for QR code: ")
output_file = input("Enter the output file name (e.g. output.png): ")

generate_qr_code(input_text, output_file)
print(f"QR code generated and saved to {output_file}")
