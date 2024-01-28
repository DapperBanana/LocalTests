
import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Open the satellite image file
image_file = "path/to/satellite_image.tif"
src = rasterio.open(image_file)

# Read the image raster data into a numpy array
raster = src.read()

# Extract the red, green, and blue bands from the raster data
red = raster[0, :, :]
green = raster[1, :, :]
blue = raster[2, :, :]

# Calculate the Normalized Difference Vegetation Index (NDVI)
ndvi = (red.astype(float) - blue.astype(float)) / (red.astype(float) + blue.astype(float))

# Plot the NDVI values as a grayscale image
plt.imshow(ndvi, cmap='gray')
plt.colorbar(label='NDVI')
plt.title('Normalized Difference Vegetation Index (NDVI)')
plt.show()
