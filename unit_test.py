
from PIL import Image
import random

# Create a new RGB image
image_size = (500, 500)
image = Image.new("RGB", image_size)

# Generate random pixel values for image
pixels = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(image_size[0] * image_size[1])]

# Load pixel data into image
image.putdata(pixels)

# Display the image
image.show()
