
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
        return "No metadata found in the image file."

if __name__ == "__main__":
    image_path = "image.jpg"
    metadata = extract_metadata(image_path)
    print(metadata)
