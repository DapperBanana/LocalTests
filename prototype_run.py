
from PIL import Image

def get_image_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            metadata = img.info
            return metadata
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    image_path = "image.jpg"
    metadata = get_image_metadata(image_path)
    
    if not isinstance(metadata, str):
        print("Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    else:
        print(metadata)
