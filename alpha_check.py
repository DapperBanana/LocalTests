
from PIL import Image, ImageDraw
import random

# Set the size of the image
width = 800
height = 600

# Create a new image with white background
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Generate random colored rectangles
for _ in range(10):
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(x1, width)
    y2 = random.randint(y1, height)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.rectangle([x1, y1, x2, y2], fill=color)

# Save the generated image
image.save("random_image.png")
image.show()
