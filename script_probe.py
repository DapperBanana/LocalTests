
from PIL import Image
from PIL.ExifTags import TAGS

def get_image_metadata(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()

    if exif_data is not None:
        metadata = {}
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            metadata[tag_name] = value
        return metadata
    else:
        return None

# Provide the path to the image file
image_path = 'example.jpg'
metadata = get_image_metadata(image_path)

if metadata is not None:
    for key, value in metadata.items():
        print(f"{key}: {value}")
else:
    print("No metadata found in the image file.")
