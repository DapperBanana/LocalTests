
import rasterio
import numpy as np

# Path to the input satellite image
input_image_path = 'path/to/satellite/image.tif'

# Open the satellite image
with rasterio.open(input_image_path) as src:
    red = src.read(3)  # Read the red band (band 3)
    nir = src.read(4)  # Read the near-infrared band (band 4)

    # Calculate NDVI
    ndvi = (nir - red) / (nir + red)

    # Get the metadata of the input image
    meta = src.meta

# Write the NDVI values to a new raster file
output_path = 'output_ndvi.tif'
with rasterio.open(output_path, 'w', **meta) as dst:
    dst.write(ndvi, 1)

print("NDVI calculated and saved to", output_path)
