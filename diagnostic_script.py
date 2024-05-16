
import rasterio
import matplotlib.pyplot as plt

# Open the satellite image file
filepath = "path/to/satellite_image.tif"
sat_data = rasterio.open(filepath)

# Read the red, green, and blue bands of the satellite image
red_band = sat_data.read(3)
green_band = sat_data.read(2)
blue_band = sat_data.read(1)

# Calculate the vegetation index (NDVI) using the red and near-infrared bands
ndvi = (red_band - green_band) / (red_band + green_band)

# Plot the NDVI map
plt.figure(figsize=(10, 10))
plt.imshow(ndvi, cmap='viridis')
plt.colorbar(label='NDVI')
plt.title('Normalized Difference Vegetation Index (NDVI)')
plt.show()

# Calculate the average NDVI value
avg_ndvi = ndvi.mean()
print(f'Average NDVI value: {avg_ndvi}')
