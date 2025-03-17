
from PIL import Image, ImageDraw
import random

# Create a new 500x500 image with a white background
image = Image.new('RGB', (500, 500), 'white')
draw = ImageDraw.Draw(image)

# Draw random colored rectangles on the image
for _ in range(50):
    x1 = random.randint(0, 500)
    y1 = random.randint(0, 500)
    x2 = random.randint(0, 500)
    y2 = random.randint(0, 500)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.rectangle([x1, y1, x2, y2], fill=color)

# Save the image to a file
image.save('random_image.png')

print('Random image generated and saved as random_image.png')
