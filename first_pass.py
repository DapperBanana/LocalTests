
import rasterio
import numpy as np

# Open the satellite image file
with rasterio.open('satellite_image.tif') as src:
    # Read the red, green, and blue bands of the image
    red = src.read(1)
    green = src.read(2)
    blue = src.read(3)

# Calculate the normalized difference vegetation index (NDVI)
ndvi = (red - green) / (red + green)

# Threshold NDVI values to classify vegetation/non-vegetation
threshold = 0.3
vegetation = np.where(ndvi > threshold, 1, 0)

# Save the vegetation mask as a new raster file
with rasterio.open('vegetation_mask.tif', 'w', driver='GTiff', width=src.width, height=src.height, count=1, dtype='uint8') as dst:
    dst.write(vegetation.astype('uint8'), 1)

print("Vegetation analysis completed. Vegetation mask saved as vegetation_mask.tif.")
