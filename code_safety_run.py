
import rasterio
import numpy as np

# Open the satellite image file
sat_image_path = "path/to/your/satellite/image.tif"
sat_image = rasterio.open(sat_image_path)

# Read the image bands as numpy arrays
red_band = sat_image.read(3)
nir_band = sat_image.read(4)

# Calculate the normalized difference vegetation index (NDVI)
ndvi = (nir_band - red_band) / (nir_band + red_band)

# Apply thresholding to classify vegetation
threshold = 0.2
vegetation_mask = np.where(ndvi > threshold, 1, 0)

# Save the vegetation mask as a new raster file
output_path = "path/to/save/vegetation_mask.tif"
with rasterio.open(output_path, 'w', driver='GTiff', height=sat_image.height, width=sat_image.width, count=1, dtype=vegetation_mask.dtype) as dst:
    dst.write(vegetation_mask, 1)

# Close the satellite image file
sat_image.close()

print("Vegetation analysis completed. Vegetation mask saved to:", output_path)
