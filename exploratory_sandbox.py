
from PIL import Image

def extract_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            meta_data = img.info
            print("Metadata for image file:", image_path)
            for key, value in meta_data.items():
                print(key, ":", value)
    except IOError:
        print("Unable to open or read image file")

# Replace 'image.jpg' with the path to your image file
image_path = 'image.jpg'
extract_metadata(image_path)
