
from PIL import Image
import random

# Set width and height of the image
width = 200
height = 200

# Create a new blank image
img = Image.new('RGB', (width, height))

# Generate random pixels in the image
pixels = []
for _ in range(width * height):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pixels.append((r, g, b))

# Put the pixels in the image
img.putdata(pixels)

# Save the image
img.save('random_image.png')

print('Random image generated and saved as random_image.png')
