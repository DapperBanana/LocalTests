
import qrcode

# Take input from the user
data = input("Enter the data for the QR code: ")

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create a QR code image
img = qr.make_image(fill_color="black", back_color="white")
filename = "qrcode.png"
img.save(filename)

print("QR code generated successfully. Saved as", filename)
