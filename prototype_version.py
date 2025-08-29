
from PIL import Image

def convert_to_grayscale(image_path, output_path):
    image = Image.open(image_path)
    grayscale_image = image.convert("L")
    grayscale_image.save(output_path)
    print("Image converted to grayscale.")

if __name__ == "__main__":
    image_path = "input_image.jpg"
    output_path = "output_grayscale_image.jpg"
    convert_to_grayscale(image_path, output_path)
