
from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Get the metadata dictionary
    metadata = image.info

    # Print out the metadata
    for tag, value in metadata.items():
        tag_name = TAGS.get(tag, tag)
        print(f"{tag_name}: {value}")

# Specify the path to the image file
image_path = 'example.jpg'

# Extract metadata from the image file
extract_metadata(image_path)
