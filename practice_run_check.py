
from PIL import Image, ImageDraw
import random

# Create a new image with RGB mode
img = Image.new('RGB', (500, 500), color = 'white')
draw = ImageDraw.Draw(img)

# Generate random pixels in the image
for i in range(500):
    for j in range(500):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        draw.point((i, j), (r, g, b))

# Save the image to a file
img.save('random_image.png')

# Display the image
img.show()
