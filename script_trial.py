
from PIL import Image, ImageDraw
import random

# Create a new image with black background
image = Image.new('RGB', (500, 500), 'black')
draw = ImageDraw.Draw(image)

# Generate random pixels
for i in range(500):
    for j in range(500):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        draw.point((i, j), fill=(r, g, b))

# Save the image
image.save('random_image.png')
