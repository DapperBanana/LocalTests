
import rasterio
import numpy as np

# Open the satellite image file using rasterio
image_file = "satellite_image.tif"
sat_data = rasterio.open(image_file)

# Read the red, green, and blue bands from the image
red_band = sat_data.read(3)
green_band = sat_data.read(2)
blue_band = sat_data.read(1)

# Calculate the Normalized Difference Vegetation Index (NDVI) to identify vegetation
ndvi = (red_band - blue_band) / (red_band + blue_band)

# Calculate the average NDVI value to determine the amount of vegetation in the image
average_ndvi = np.mean(ndvi)

print("Average NDVI value:", average_ndvi)

# Threshold NDVI value to identify areas with vegetation
threshold = 0.2
vegetation_mask = np.where(ndvi > threshold, 1, 0)

# Save the vegetation mask as a new image file
output_file = "vegetation_mask.tif"
with rasterio.open(output_file, 'w', driver='GTiff', width=sat_data.width, height=sat_data.height, count=1, dtype=vegetation_mask.dtype) as dst:
    dst.write(vegetation_mask, 1)

print("Vegetation mask saved as", output_file)
