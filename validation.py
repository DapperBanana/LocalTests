
from PIL import Image

def get_image_metadata(file_path):
    with Image.open(file_path) as img:
        metadata = img.info
        return metadata

file_path = "example.jpg"
metadata = get_image_metadata(file_path)

for key, value in metadata.items():
    print(f"{key}: {value}")
