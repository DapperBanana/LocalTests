
from PIL import Image, ImageDraw
import random

# Create a new image with a white background
img = Image.new('RGB', (500, 500), 'white')
draw = ImageDraw.Draw(img)

# Generate random pixels on the image
for _ in range(1000):
    x = random.randint(0, 499)
    y = random.randint(0, 499)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.point((x, y), fill=color)

# Save the image
img.save('random_image.png')

# Display the image
img.show()
