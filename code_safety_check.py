
from PIL import Image

def grayscale_conversion(image_path):
    # Open the image file
    img = Image.open(image_path)
    
    # Convert the image to grayscale
    img_gray = img.convert('L')
    
    # Save the grayscale image
    img_gray.save('grayscale_image.jpg')
    
    print("Grayscale image saved as 'grayscale_image.jpg'")

if __name__ == "__main__":
    image_path = 'original_image.jpg'
    grayscale_conversion(image_path)
