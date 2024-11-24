
import rasterio
import numpy as np

# Open the satellite image file
sat_image = rasterio.open('path_to_your_satellite_image.tif')

# Read the red, green, and blue bands of the image
red_band = sat_image.read(3)
green_band = sat_image.read(2)
blue_band = sat_image.read(1)

# Calculate the Normalized Difference Vegetation Index (NDVI)
ndvi = (red_band - near_infrared) / (red_band + near_infrared)

# Threshold NDVI values to identify areas with vegetation
vegetation_mask = np.where(ndvi > 0.5, 1, 0)

# Write the vegetation mask to a new raster file
with rasterio.open('vegetation_mask.tif', 'w', driver='GTiff', width=sat_image.width, height=sat_image.height, count=1, crs=sat_image.crs, transform=sat_image.transform, dtype='uint8') as dst:
    dst.write(vegetation_mask, 1)

# Close the satellite image file
sat_image.close()
