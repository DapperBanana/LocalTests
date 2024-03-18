
from PIL import Image, ImageDraw
import random

# Create a new RGB image of size 500x500
img = Image.new('RGB', (500, 500), 'white')
draw = ImageDraw.Draw(img)

# Generate random colors
color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
color3 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Generate random shapes
draw.rectangle((50, 50, 250, 250), fill=color1)
draw.ellipse((300, 50, 450, 250), fill=color2)
draw.polygon([(200, 400), (100, 450), (300, 450)], fill=color3)

# Save the image
img.save('random_image.png')

print('Random image generated successfully!')
