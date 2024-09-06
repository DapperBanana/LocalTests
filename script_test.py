
from PIL import Image

def extract_metadata(image_file):
    try:
        img = Image.open(image_file)
        metadata = img.info
        for key, value in metadata.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error extracting metadata: {e}")

if __name__ == "__main__":
    image_file = "example.jpg"  # Change this to the path of the image file you want to extract metadata from
    extract_metadata(image_file)
