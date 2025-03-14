
import rasterio
import numpy as np

# Open the satellite image file using rasterio
image_file = 'path/to/your/satellite/image.tif'
dataset = rasterio.open(image_file)

# Read the image bands (assuming the image has red, green, and blue bands)
red_band = dataset.read(1)
green_band = dataset.read(2)
blue_band = dataset.read(3)

# Calculate the normalized difference vegetation index (NDVI)
ndvi = (red_band - blue_band) / (red_band + blue_band)

# Threshold NDVI values to identify vegetation
vegetation_pixels = np.where(ndvi > 0.5)

# Calculate the percentage of vegetation in the image
vegetation_percentage = len(vegetation_pixels[0]) / (dataset.width * dataset.height) * 100

print(f'Percentage of vegetation in the image: {vegetation_percentage:.2f}%')

# Close the dataset
dataset.close()
