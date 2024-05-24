
from PIL import Image, ImageDraw
import random

# Set the size of the image
width = 400
height = 400

# Create a new image with a white background
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Generate random color for drawing
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Draw random shapes on the image
for _ in range(10):
    shape = random.choice(["rectangle", "circle"])
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)
    
    if shape == "rectangle":
        draw.rectangle([x1, y1, x2, y2], fill=color)
    else:
        draw.ellipse([x1, y1, x2, y2], fill=color)

# Save the image
image.save("random_image.png")

# Display the image
image.show()
