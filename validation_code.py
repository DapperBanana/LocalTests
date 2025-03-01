
from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(image_path):
    image = Image.open(image_path)
    metadata = image._getexif()
    
    if metadata:
        extracted_metadata = {}
        for tag, value in metadata.items():
            tag_name = TAGS.get(tag, tag)
            extracted_metadata[tag_name] = value
        return extracted_metadata
    else:
        return "No metadata found in this image."

if __name__ == "__main__":
    image_path = "sample_image.jpg"  # Change this to the path of your image file
    metadata = extract_metadata(image_path)
    
    if isinstance(metadata, dict):
        for key, value in metadata.items():
            print(f"{key}: {value}")
    else:
        print(metadata)
