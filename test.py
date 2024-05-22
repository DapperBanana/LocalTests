
import rasterio
import numpy as np

# Open the satellite image file
with rasterio.open('satellite_image.tif') as src:
    red_band = src.read(3)
    nir_band = src.read(4)
    profile = src.profile

# Calculate the Normalized Difference Vegetation Index (NDVI)
ndvi = (nir_band - red_band) / (nir_band + red_band)

# Threshold the NDVI values to identify vegetation
vegetation_mask = np.where(ndvi > 0.6, 1, 0)

# Write the vegetation mask to a new file
profile.update(count=1, dtype=rasterio.uint8)
with rasterio.open('vegetation_mask.tif', 'w', **profile) as dst:
    dst.write(vegetation_mask.astype(rasterio.uint8), 1)

print('Vegetation mask has been saved to vegetation_mask.tif')
