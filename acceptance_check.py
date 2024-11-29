
from PIL import Image, ImageDraw
import random

# Set the width and height of the image
width = 500
height = 500

# Create a new image with a white background
image = Image.new('RGB', (width, height), 'white')

# Create a drawing object
draw = ImageDraw.Draw(image)

# Generate random points and colors to draw random shapes on the image
for _ in range(100):
    shape = random.choice(['rectangle', 'ellipse'])
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if shape == 'rectangle':
        draw.rectangle([x1, y1, x2, y2], fill=color)
    elif shape == 'ellipse':
        draw.ellipse([x1, y1, x2, y2], fill=color)

# Save the image
image.save('random_image.png')

# Display the image
image.show()
