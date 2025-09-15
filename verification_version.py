
from PIL import Image

def extract_metadata(image_path):
    img = Image.open(image_path)
    
    metadata = img.info
    
    return metadata

image_path = 'image.jpg'
metadata = extract_metadata(image_path)

for key, value in metadata.items():
    print(f'{key}: {value}')
