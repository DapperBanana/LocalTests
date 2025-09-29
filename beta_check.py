
import rasterio
from rasterio.plot import show

# Open the raster file containing satellite imagery
file_path = 'path_to_raster_file.tif'
raster = rasterio.open(file_path)

# Read the red, green, and blue bands from the raster file
red_band = raster.read(1)
green_band = raster.read(2)
blue_band = raster.read(3)

# Calculate the Normalized Difference Vegetation Index (NDVI) using the red and near-infrared bands
ndvi = (raster.read(4) - red_band) / (raster.read(4) + red_band)

# Plot the NDVI index
show(ndvi, cmap='RdYlGn')

# Calculate the average NDVI value to estimate vegetation coverage
average_ndvi = ndvi.mean()

print("Average NDVI value:", average_ndvi)

# Close the raster file
raster.close()
