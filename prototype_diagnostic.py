
from PIL import Image

def extract_metadata(image_file):
    try:
        with Image.open(image_file) as img:
            metadata = img.info
            for key, value in metadata.items():
                print(f"{key}: {value}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    image_file = "example.jpg"  # Change this to the path of your image file
    extract_metadata(image_file)
