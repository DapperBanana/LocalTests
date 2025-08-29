
import rasterio
import numpy as np

# Open the satellite image file
sat_image_path = "path/to/satellite/image.tif"
sat_data = rasterio.open(sat_image_path)

# Read the image bands
red_band = sat_data.read(3)
nir_band = sat_data.read(4)

# Calculate the normalized difference vegetation index (NDVI)
ndvi = (nir_band - red_band) / (nir_band + red_band)

# Define threshold values for vegetation
threshold_low = 0.3
threshold_high = 0.8

# Create a binary mask for vegetation based on NDVI values
vegetation_mask = np.logical_and(ndvi > threshold_low, ndvi < threshold_high)

# Calculate the total area of vegetation
vegetation_area = np.sum(vegetation_mask) * sat_data.res[0] * sat_data.res[1]  # Multiply by pixel area

print(f"The total area of vegetation in the image is: {vegetation_area} square meters")
