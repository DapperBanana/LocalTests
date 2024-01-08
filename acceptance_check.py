
import qrcode

def generate_qr_code(input_data):
    # Create an instance of the QRCode class
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    # Add the input data to the QR code
    qr.add_data(input_data)
    
    # Make the QR code image
    qr.make(fit=True)
    
    # Create an image from the QR code instance
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code image
    qr_img.save("qr_code.png")
    
    print("QR code generated successfully!")

# Test the function
input_data = input("Enter the input data: ")
generate_qr_code(input_data)
