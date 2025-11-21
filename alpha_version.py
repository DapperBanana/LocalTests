
from PIL import Image, ImageDraw
import random

# Create a new image with white background
image = Image.new('RGB', (500, 500), 'white')
draw = ImageDraw.Draw(image)

# Generate random color
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Generate random shape (rectangle or circle)
shape = random.choice(['rectangle', 'circle'])

if shape == 'rectangle':
    # Generate random rectangle coordinates
    x1 = random.randint(0, 400)
    y1 = random.randint(0, 400)
    x2 = random.randint(x1 + 50, 500)
    y2 = random.randint(y1 + 50, 500)

    draw.rectangle([(x1, y1), (x2, y2)], fill=color)

else:
    # Generate random circle coordinates
    x = random.randint(50, 450)
    y = random.randint(50, 450)
    radius = random.randint(10, 100)

    draw.ellipse([(x-radius, y-radius), (x+radius, y+radius)], fill=color)

# Display the image
image.show()
