
from PIL import Image

def grayscale_conversion(image_path):
    # Open the image file
    img = Image.open(image_path)
    
    # Convert the image to grayscale
    grayscale_img = img.convert('L')
    
    # Save the grayscale image
    grayscale_img.save('grayscale_image.jpg')
    
    print("Image converted to grayscale successfully!")

# Specify the path to the image file
image_path = 'example.jpg'

# Perform grayscale conversion on the image
grayscale_conversion(image_path)
