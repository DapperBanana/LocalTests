
import rasterio
import numpy as np

# Open the satellite image using rasterio
image_path = "path/to/satellite/image.tif"
sat_data = rasterio.open(image_path)

# Read the image bands
red_band = sat_data.read(3)
nir_band = sat_data.read(4)

# Calculate the NDVI (Normalized Difference Vegetation Index)
ndvi = (nir_band - red_band) / (nir_band + red_band)

# Define a threshold for vegetation presence
threshold = 0.3

# Count the number of pixels with NDVI above the threshold
vegetation_pixels = np.sum(ndvi > threshold)

# Calculate the percentage of vegetation cover
total_pixels = np.prod(ndvi.shape)
vegetation_cover = (vegetation_pixels / total_pixels) * 100

print(f"The percentage of vegetation cover in the image is: {vegetation_cover:.2f}%")
