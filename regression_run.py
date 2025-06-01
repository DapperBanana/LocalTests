
import qrcode

# Get input from user
data = input("Enter text or URL to generate QR code: ")

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Save QR code as PNG file
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'")
