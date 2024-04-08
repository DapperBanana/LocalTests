
from PIL import Image
from PIL.ExifTags import TAGS

def get_metadata(image_path):
    # Open the image file
    image = Image.open(image_path)
    
    # Extract the EXIF data
    exif_data = image._getexif()
    
    # Create a dictionary to store the metadata
    metadata = {}
    
    if exif_data:
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            metadata[tag_name] = value
    
    return metadata

# Path to the image file
image_path = 'image.jpg'

# Get the metadata from the image
metadata = get_metadata(image_path)

# Print the metadata
for tag, value in metadata.items():
    print(f"{tag}: {value}")
