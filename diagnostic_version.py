
from PIL import Image, ImageDraw
import random

# Create a new image
img = Image.new('RGB', (500, 500), 'white')
draw = ImageDraw.Draw(img)

# Draw random shapes on the image
for _ in range(100):
    x0 = random.randint(0, 500)
    y0 = random.randint(0, 500)
    x1 = random.randint(0, 500)
    y1 = random.randint(0, 500)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    draw.rectangle([x0, y0, x1, y1], fill=color)

# Display the image
img.show()
