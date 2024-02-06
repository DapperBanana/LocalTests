
import rasterio
import numpy as np

def calculate_ndvi(red_band, nir_band):
    ndvi = (nir_band - red_band) / (nir_band + red_band)
    return ndvi

# Open the satellite imagery file
with rasterio.open('image.tif') as file:
    # Read the red and near-infrared bands
    red = file.read(3).astype('float32')
    nir = file.read(4).astype('float32')

    # Calculate the NDVI
    ndvi = calculate_ndvi(red, nir)

    # Compute statistics
    min_ndvi = np.min(ndvi)
    max_ndvi = np.max(ndvi)
    mean_ndvi = np.mean(ndvi)
    std_ndvi = np.std(ndvi)

    # Print the results
    print(f"Minimum NDVI: {min_ndvi}")
    print(f"Maximum NDVI: {max_ndvi}")
    print(f"Mean NDVI: {mean_ndvi}")
    print(f"Standard Deviation NDVI: {std_ndvi}")
