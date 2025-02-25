
import rasterio
import numpy as np

# Open the satellite image file
with rasterio.open('satellite_image.tif') as src:
    # Read the image as a numpy array
    image = src.read()

    # Calculate the NDVI (Normalized Difference Vegetation Index)
    red_band = image[2]  # Red band
    nir_band = image[3]  # Near-Infrared band
    ndvi = (nir_band - red_band) / (nir_band + red_band)

    # Calculate the mean NDVI value
    mean_ndvi = np.mean(ndvi)

    # Print the mean NDVI value
    print(f'Mean NDVI value: {mean_ndvi}')

    # Calculate the percentage of pixels with NDVI value greater than 0.5 (indicating vegetation)
    vegetation_pixels = np.sum(ndvi > 0.5)
    total_pixels = ndvi.size
    vegetation_percentage = (vegetation_pixels / total_pixels) * 100

    # Print the percentage of vegetation pixels
    print(f'Percentage of vegetation pixels: {vegetation_percentage}%')
