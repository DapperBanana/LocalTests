
import qrcode

# Get user input
input_data = input("Enter the data you want to encode: ")

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to QR code instance
qr.add_data(input_data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("qrcode.png")

print("QR code generated successfully and saved as 'qrcode.png'")
