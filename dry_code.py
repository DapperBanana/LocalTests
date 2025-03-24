
from PIL import Image

def convert_to_grayscale(input_image_path, output_image_path):
    # Open the input image
    image = Image.open(input_image_path)
    
    # Convert the image to grayscale
    grayscale_image = image.convert('L')
    
    # Save the grayscale image
    grayscale_image.save(output_image_path)
    
    print("Image converted to grayscale successfully.")

if __name__ == "__main__":
    # Specify the input and output image paths
    input_image_path = "input_image.jpg"
    output_image_path = "output_image.jpg"
    
    # Convert the image to grayscale
    convert_to_grayscale(input_image_path, output_image_path)
