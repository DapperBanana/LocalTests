
from PIL import Image

def extract_metadata(image_path):
    img = Image.open(image_path)
    
    metadata = {
        'Format': img.format,
        'Mode': img.mode,
        'Size': img.size,
        'Exif': img.info.get('exif')
    }
    
    return metadata

if __name__ == '__main__':
    image_path = 'example.jpg'
    metadata = extract_metadata(image_path)
    
    for key, value in metadata.items():
        print(f'{key}: {value}')
