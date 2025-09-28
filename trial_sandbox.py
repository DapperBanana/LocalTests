
from PIL import Image

def convert_to_grayscale(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert("L")
    grayscale_image.show()

if __name__ == "__main__":
    image_path = "example.jpg"
    convert_to_grayscale(image_path)
