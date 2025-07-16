
import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Open the raster file containing satellite imagery
file_path = "path_to_raster_file.tif"
sat_data = rasterio.open(file_path)

# Read the red, green, and blue bands of the satellite imagery
red_band = sat_data.read(1)
green_band = sat_data.read(2)
blue_band = sat_data.read(3)

# Calculate the normalized difference vegetation index (NDVI)
ndvi = np.where((red_band+green_band)==0, 0, (red_band-green_band)/(red_band+green_band))

# Plot the NDVI image
plt.figure(figsize=(10,10))
plt.imshow(ndvi, cmap='viridis')
plt.colorbar()
plt.title('Normalized Difference Vegetation Index')
plt.show()

# Calculate the average NDVI value for vegetation
vegetation_mask = np.where(ndvi > 0.4, 1, 0)
vegetation_pixels = np.sum(vegetation_mask)
total_pixels = np.prod(ndvi.shape)
average_ndvi = vegetation_pixels / total_pixels

print("Average NDVI value for vegetation: ", average_ndvi)
