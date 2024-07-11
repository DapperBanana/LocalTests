
import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Open the satellite image using rasterio
satellite_image_path = 'path/to/satellite/image.tif'
sat_dataset = rasterio.open(satellite_image_path)

# Read the red, green, and blue bands of the image
red_band = sat_dataset.read(1)
green_band = sat_dataset.read(2)
blue_band = sat_dataset.read(3)

# Calculate the Normalized Difference Vegetation Index (NDVI)
ndvi = (red_band - blue_band) / (red_band + blue_band)

# Plot the NDVI values
plt.figure(figsize=(10,10))
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar()
plt.title('Normalized Difference Vegetation Index (NDVI)')

# Save the output image
plt.savefig('output_ndvi.png')

# Calculate the mean NDVI value for the entire image
mean_ndvi = np.mean(ndvi)
print(f"Mean NDVI value for the image: {mean_ndvi}")

# Calculate the percentage of pixels with NDVI values greater than a threshold (e.g., 0.5)
threshold = 0.5
vegetation_pixels = np.where(ndvi > threshold)
percentage_vegetation = (len(vegetation_pixels[0]) / ndvi.size) * 100
print(f"Percentage of vegetation pixels above threshold ({threshold}): {percentage_vegetation}%")

# Close the satellite image dataset
sat_dataset.close()
