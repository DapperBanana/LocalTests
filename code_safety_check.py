
from PIL import Image
import random

# Create a new image with RGB mode
img = Image.new('RGB', (500, 500))

# Generate random pixels for the image
pixels = []
for _ in range(500):
    row = []
    for _ in range(500):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        row.append((r, g, b))
    pixels.append(row)

# Put the random pixels into the image
img.putdata([pixel for row in pixels for pixel in row])

# Save the image
img.save('random_image.png')

print("Random image generated and saved as 'random_image.png'")
