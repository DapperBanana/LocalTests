
import rasterio
import numpy as np

# Load the satellite imagery file
sat_image = "path_to_satellite_image.tif"
sat_data = rasterio.open(sat_image)

# Read the red, green, and blue bands of the image
red_band = sat_data.read(1)
green_band = sat_data.read(2)
blue_band = sat_data.read(3)

# Calculate the NDVI (Normalized Difference Vegetation Index)
ndvi = (red_band - blue_band) / (red_band + blue_band)

# Define threshold for vegetation
threshold = 0.5

# Create a binary mask for vegetation based on the NDVI values
vegetation_mask = np.where(ndvi > threshold, 1, 0)

# Calculate the total area of vegetation in the image
vegetation_area = np.sum(vegetation_mask) * sat_data.res[0] * sat_data.res[1]

print(f"Total area of vegetation: {vegetation_area} square meters")
