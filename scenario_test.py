
import rasterio
import numpy as np

# Open the satellite image file using rasterio
satellite_image = rasterio.open('path/to/satellite/image.tif')

# Read the image as a numpy array
image_array = satellite_image.read()

# Calculate the NDVI (Normalized Difference Vegetation Index)
red_band = image_array[0]
nir_band = image_array[3]

ndvi = (nir_band - red_band) / (nir_band + red_band)

# Threshold the NDVI values to classify vegetation
vegetation_mask = np.where(ndvi > 0.6, 1, 0)

# Save the vegetation mask as a new raster file
profile = satellite_image.profile
profile.update(count=1, dtype=rasterio.uint8)

with rasterio.open('path/to/vegetation/mask.tif', 'w', **profile) as dst:
    dst.write(vegetation_mask.astype(rasterio.uint8), 1)

print("Vegetation analysis completed. Vegetation mask saved as vegetation_mask.tif")
