
from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(image_path):
    metadata = {}
    img = Image.open(image_path)
    exif_data = img._getexif()

    if exif_data:
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag)
            metadata[tag_name] = value
    
    return metadata

if __name__ == "__main__":
    image_path = "example.jpg"
    metadata = extract_metadata(image_path)

    for key, value in metadata.items():
        print(f"{key}: {value}")
