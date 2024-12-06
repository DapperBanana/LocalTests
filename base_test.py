
from PIL import Image, ImageDraw
import random

# Create a new RGB image
width = 500
height = 500
img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)

# Generate random colors
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Generate random shapes
shape = random.choice(['rectangle', 'circle'])
if shape == 'rectangle':
    draw.rectangle([random.randint(0, width), random.randint(0, height), random.randint(0, width), random.randint(0, height)], fill=color)
else:
    draw.ellipse([random.randint(0, width), random.randint(0, height), random.randint(0, width), random.randint(0, height)], fill=color)

# Save the image
img.save("random_image.png")

print("Random image generated and saved as 'random_image.png'")
