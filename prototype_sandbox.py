
import qrcode

# Get user input
data = input("Enter the data for the QR code: ")

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save QR code image
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'")
