
from PIL import Image, ImageDraw
import random

# Create a new image with size 500x500
img = Image.new('RGB', (500, 500), color='white')
draw = ImageDraw.Draw(img)

# Generate random pixels and draw them on the image
for _ in range(10000):
    x = random.randint(0, 499)
    y = random.randint(0, 499)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    draw.point((x, y), fill=(r, g, b))

# Save the image as a file
img.save('random_image.png')

# Display the image
img.show()
