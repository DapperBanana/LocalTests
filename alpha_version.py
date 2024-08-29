
from PIL import Image, ImageDraw
import random

# Create a new image
width = 400
height = 400
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Draw random shapes on the image
for _ in range(100):
    shape = random.choice(['rectangle', 'ellipse'])
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)
    
    if shape == 'rectangle':
        draw.rectangle([x1, y1, x2, y2], fill=color)
    elif shape == 'ellipse':
        draw.ellipse([x1, y1, x2, y2], fill=color)

# Save the image
image.save('random_image.png')
image.show()
