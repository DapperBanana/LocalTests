
from PIL import Image, ImageDraw
import random

# Generate a random RGB color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Create a new image
image = Image.new('RGB', (500, 500))
draw = ImageDraw.Draw(image)

# Draw random shapes on the image
for _ in range(100):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    size = random.randint(10, 100)
    color = random_color()
    shape = random.choice(['rectangle', 'circle', 'triangle'])
    
    if shape == 'rectangle':
        draw.rectangle([x, y, x+size, y+size], fill=color)
    elif shape == 'circle':
        draw.ellipse([x, y, x+size, y+size], fill=color)
    else:
        draw.polygon([(x, y), (x+size, y), (x+(size//2), y+size)], fill=color)

# Save the image
image.save('random_image.png')

print('Random image generated and saved as "random_image.png"!')
