
from PIL import Image

def extract_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            # Get image metadata
            metadata = img.info
            print("Metadata extracted successfully:")
            for key, value in metadata.items():
                print(f"{key}: {value}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Provide the image file path
image_path = 'image.jpg'

# Call the function to extract metadata
extract_metadata(image_path)
