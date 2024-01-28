
from PIL import Image

def extract_metadata(filename):
    try:
        image = Image.open(filename)
        if 'exif' in image.info:
            exif_data = image._getexif()
            if exif_data is not None:
                for tag, value in exif_data.items():
                    tag_name = Image.TAGS.get(tag, tag)
                    print(f"{tag_name}: {value}")
        else:
            print("No EXIF data found.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print("Error:", str(e))

# Usage example
filename = "example.jpg"
extract_metadata(filename)
