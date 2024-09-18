
from PIL import Image
from PIL.ExifTags import TAGS

def get_image_metadata(image_path):
    with Image.open(image_path) as img:
        meta_data = img._getexif()
        
        if meta_data:
            for tag, value in meta_data.items():
                tag_name = TAGS.get(tag, tag)
                print(f"{tag_name}: {value}")
        else:
            print("No metadata found in the image.")

image_path = "image.jpg"
get_image_metadata(image_path)
