
import rasterio
import numpy as np

# Open the satellite image file using rasterio
file_path = 'path_to_your_satellite_image.tif'
sat_data = rasterio.open(file_path)

# Read the image data as a numpy array
img = sat_data.read()

# Extract the red, green, and blue bands from the image
red_band = img[0]
green_band = img[1]
blue_band = img[2]

# Calculate the vegetation index (NDVI) using the formula: (NIR - Red) / (NIR + Red)
nir_band = img[3]
ndvi = (nir_band - red_band) / (nir_band + red_band)

# Threshold the NDVI values to identify areas with high vegetation
vegetation_threshold = 0.5
vegetation_mask = np.where(ndvi > vegetation_threshold, 1, 0)

# Calculate the percentage of vegetation coverage in the image
vegetation_coverage = np.sum(vegetation_mask) / np.size(vegetation_mask) * 100

print(f"Percentage of vegetation coverage in the image: {vegetation_coverage}%")
