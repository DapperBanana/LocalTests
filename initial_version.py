
import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Open satellite image file
sat_image = rasterio.open('satellite_image.tif')

# Read image bands
red = sat_image.read(3)
nir = sat_image.read(4)

# Calculate NDVI (Normalized Difference Vegetation Index)
ndvi = (nir - red) / (nir + red)

# Define vegetation threshold
threshold = 0.5

# Create a mask based on NDVI threshold
vegetation_mask = np.where(ndvi > threshold, 1, 0)

# Plot NDVI image
plt.figure(figsize=(10, 10))
plt.imshow(vegetation_mask, cmap='viridis')
plt.colorbar(label='Vegetation')
plt.title('Vegetation Mask')
plt.show()
