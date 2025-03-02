
from PIL import Image, ImageDraw
import random

width = 500
height = 500

# Create a new image with white background
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Generate random pixels for the image
for x in range(width):
    for y in range(height):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        draw.point((x, y), fill=(r, g, b))

# Display the image
image.show()
