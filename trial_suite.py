
from PIL import Image
from PIL.ExifTags import TAGS

def extract_image_metadata(image_path):
    image = Image.open(image_path)
    
    metadata = {}
    
    for tag, value in image._getexif().items():
        tag_name = TAGS.get(tag, tag)
        metadata[tag_name] = value
        
    return metadata

if __name__ == "__main__":
    image_path = "image.jpg"
    
    metadata = extract_image_metadata(image_path)
    
    for tag, value in metadata.items():
        print(f"{tag}: {value}")
