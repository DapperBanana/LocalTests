
from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(image_path):
    try:
        img = Image.open(image_path)
        exif_data = img._getexif()
        
        if exif_data is not None:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                print(f"{tag_name}: {value}")
    except Exception as e:
        print(f"Error: {e}")

# Specify the path to the image file
image_path = "image.jpg"

# Call the extract_metadata function with the image path
extract_metadata(image_path)
