
from PIL import Image, ImageDraw
import random

# Create a new image with RGB color, change the size as needed
width = 500
height = 500
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Generate random pixels
for x in range(width):
    for y in range(height):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        draw.point((x, y), (r, g, b))

# Save the image as "random_image.png"
image.save("random_image.png")
