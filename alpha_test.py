
from PIL import Image, ImageDraw
import random

# Create a new blank image
image = Image.new('RGB', (500, 500), 'white')
draw = ImageDraw.Draw(image)

# Generate random color for the background
background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.rectangle([(0, 0), (500, 500)], fill=background_color)

# Generate random shapes on the image
for _ in range(10):
    shape = random.choice(['rectangle', 'circle', 'triangle'])
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    x1, y1 = random.randint(0, 500), random.randint(0, 500)
    x2, y2 = random.randint(x1, 500), random.randint(y1, 500)
    
    if shape == 'rectangle':
        draw.rectangle([(x1, y1), (x2, y2)], fill=color)
    elif shape == 'circle':
        draw.ellipse([(x1, y1), (x2, y2)], fill=color)
    elif shape == 'triangle':
        draw.polygon([(x1, y2), ((x1 + x2) // 2, y1), (x2, y2)], fill=color)

# Save the image
image.save('random_image.png')

print('Random image generated and saved as random_image.png')
