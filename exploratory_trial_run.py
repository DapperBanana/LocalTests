
from PIL import Image

def extract_image_metadata(image_path):
    with Image.open(image_path) as img:
        meta_data = img.info
        for key, value in meta_data.items():
            print(f"{key}: {value}")

image_path = 'example.jpg'
extract_image_metadata(image_path)
