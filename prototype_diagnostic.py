
from PIL import Image

def extract_metadata(image_path):
    with Image.open(image_path) as img:
        metadata = {
            "format": img.format,
            "mode": img.mode,
            "size": img.size,
            "info": img.info
        }
        
        return metadata

if __name__ == "__main__":
    image_path = "image.jpg"   # Update with the path to your image file
    metadata = extract_metadata(image_path)
    
    print("Metadata:")
    print(metadata)
