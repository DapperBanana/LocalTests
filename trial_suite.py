
from PIL import Image
from PIL.ExifTags import TAGS

def get_image_metadata(image_path):
    with Image.open(image_path) as img:
        exif_data = img._getexif()
        if exif_data:
            metadata = {}
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                metadata[tag] = value
            return metadata
        else:
            return None

image_path = 'example.jpg'
metadata = get_image_metadata(image_path)

if metadata:
    for key, value in metadata.items():
        print(f'{key}: {value}')
else:
    print('No metadata found for this image.')
