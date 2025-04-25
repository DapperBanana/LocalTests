
import rasterio
import numpy as np

# Open a raster file containing satellite imagery
with rasterio.open('example_image.tif') as src:
    image = src.read()

    # Calculate the NDVI (Normalized Difference Vegetation Index)
    red_band = image[2]
    nir_band = image[3]
    ndvi = (nir_band - red_band) / (nir_band + red_band)

    # Define threshold for vegetation
    threshold = 0.3

    # Count the number of vegetation pixels
    vegetation_pixels = np.count_nonzero(ndvi > threshold)

    # Calculate percentage of vegetation coverage
    total_pixels = np.prod(ndvi.shape)
    vegetation_coverage = (vegetation_pixels / total_pixels) * 100

    print(f"Vegetation coverage: {vegetation_coverage:.2f}%")
