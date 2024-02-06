
import rasterio
import numpy as np

# Open the satellite image using rasterio
with rasterio.open('path/to/satellite_image.tif') as dataset:
    # Read the red, green, and blue bands
    red_band = dataset.read(3)
    green_band = dataset.read(2)
    blue_band = dataset.read(1)

    # Calculate the Normalized Difference Vegetation Index (NDVI)
    ndvi = (red_band - blue_band) / (red_band + blue_band)

    # Threshold the NDVI to identify vegetation
    vegetation = np.where(ndvi > 0.5, 1, 0)

    # Calculate the percentage of vegetation pixels
    percentage_vegetation = np.mean(vegetation) * 100

    print(f"Percentage of vegetation: {percentage_vegetation}%")
