
import rasterio
from rasterio.plot import show
import numpy as np

# Open the satellite image
path = "path/to/satellite/image.tif"
sat_data = rasterio.open(path)

# Read the red, green, and blue bands
red = sat_data.read(1)
green = sat_data.read(2)
blue = sat_data.read(3)

# Calculate NDVI (Normalized Difference Vegetation Index)
ndvi = (red - blue) / (red + blue)

# Normalize NDVI values between 0 and 1
ndvi_norm = (ndvi - np.min(ndvi)) / (np.max(ndvi) - np.min(ndvi))

# Threshold NDVI values to identify vegetation
threshold = 0.5
vegetation = np.where(ndvi_norm > threshold, 1, 0)

# Display the vegetation mask
show(vegetation)

# Calculate the percentage of vegetation cover
total_pixels = np.prod(vegetation.shape)
vegetation_pixels = np.sum(vegetation)
vegetation_cover = (vegetation_pixels / total_pixels) * 100

print("Percentage of vegetation cover: {:.2f}%".format(vegetation_cover))
