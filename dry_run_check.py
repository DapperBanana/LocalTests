
from PIL import Image, ImageDraw
import random

width = 500
height = 500

# Create a new image
img = Image.new('RGB', (width, height), color = 'white')
draw = ImageDraw.Draw(img)

# Generate random shapes on the image
for i in range(100):
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)
    
    shape = random.choice(['rectangle', 'circle', 'line'])
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    if shape == 'rectangle':
        draw.rectangle([x1, y1, x2, y2], fill=color)
    elif shape == 'circle':
        draw.ellipse([x1, y1, x2, y2], fill=color)
    elif shape == 'line':
        draw.line([x1, y1, x2, y2], fill=color, width=3)

# Save the image
img.save('random_image.png')
