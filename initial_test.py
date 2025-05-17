
from PIL import Image

def grayscale_conversion(image_path):
    try:
        # Open the image file
        image = Image.open(image_path)
        
        # Convert the image to grayscale
        grayscale_image = image.convert('L')
        
        # Save the grayscale image
        grayscale_image.save('grayscale_image.jpg')
        
        print("Grayscale conversion completed. Saved as 'grayscale_image.jpg'")
    
    except IOError:
        print("Unable to open image file. Please check the file path.")

# Specify the path to the image file
image_path = "image.jpg"

# Perform grayscale conversion
grayscale_conversion(image_path)
