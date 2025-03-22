
from PIL import Image, ImageDraw
import random

# Create a new image
image = Image.new("RGB", (400, 400), "white")
draw = ImageDraw.Draw(image)

# Generate random pixels
for _ in range(10000):
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.point((x, y), fill=color)

# Save the image
image.save("random_image.png")

# Display the image
image.show()
