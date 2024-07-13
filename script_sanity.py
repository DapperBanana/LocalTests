
from PIL import Image
from PIL.ExifTags import TAGS

def get_metadata(image_path):
    img = Image.open(image_path)
    exif_data = img._getexif()
    
    if exif_data:
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            print(f"{tag_name}: {value}")
    else:
        print("No metadata found for this image.")

if __name__ == "__main__":
    image_path = "path/to/your/image.jpg"
    get_metadata(image_path)
