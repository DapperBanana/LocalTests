
from PIL import Image, ImageDraw
import random

# Create a new RGB image of size 500x500
image = Image.new('RGB', (500, 500))

# Create a drawing object
draw = ImageDraw.Draw(image)

# Fill the image with a random color
red = random.randint(0, 255)
green = random.randint(0, 255)
blue = random.randint(0, 255)
draw.rectangle((0, 0, 500, 500), fill=(red, green, blue))

# Draw some random shapes on the image
for _ in range(10):
    x0 = random.randint(0, 500)
    y0 = random.randint(0, 500)
    x1 = random.randint(0, 500)
    y1 = random.randint(0, 500)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.rectangle((x0, y0, x1, y1), fill=color)

# Save the generated image
image.save('random_image.png')

# Display the generated image
image.show()
