
import rasterio
import numpy as np

# Open the satellite image file
img_file = "path/to/satellite/image.tif"
img = rasterio.open(img_file)

# Read the Red and Near-Infrared bands
red = img.read(3)
nir = img.read(4)

# Calculate the NDVI
ndvi = (nir - red) / (nir + red)

# Save the NDVI image
ndvi_meta = img.meta
ndvi_meta.update(driver='GTiff')
ndvi_meta.update(count=1)

with rasterio.open('ndvi.tif', 'w', **ndvi_meta) as dst:
    dst.write(ndvi, 1)

print("NDVI image generated successfully!")
