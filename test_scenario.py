
import rasterio
from rasterio.plot import show
from rasterio.mask import mask
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np


def analyze_vegetation(satellite_image_path, boundary_shapefile_path):
    # Read the satellite image using rasterio
    with rasterio.open(satellite_image_path) as src:
        bounds = src.bounds
        data = src.read()

    # Read the boundary shapefile using geopandas
    shapefile = gpd.read_file(boundary_shapefile_path)
    geometry = shapefile.geometry.values[0]

    # Crop the satellite image using the boundary
    cropped_image, transform = mask(dataset=data, shapes=geometry, crop=True)

    # Calculate the vegetation index (NDVI)
    red_band = cropped_image[2, :, :]
    nir_band = cropped_image[3, :, :]
    ndvi = (nir_band - red_band) / (nir_band + red_band)

    # Visualize the cropped image and NDVI
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].set_title("Cropped Image")
    show(cropped_image, ax=axs[0], transform=transform)
    axs[1].set_title("NDVI")
    axs[1].imshow(ndvi, cmap='RdYlGn', extent=[bounds.left, bounds.right, bounds.bottom, bounds.top])
    plt.show()

    # Calculate the average NDVI value within the boundary
    avg_ndvi = np.nanmean(ndvi)
    print("Average NDVI:", avg_ndvi)


# Example usage
satellite_image_path = "path/to/satellite/image.tif"
boundary_shapefile_path = "path/to/boundary/shapefile.shp"
analyze_vegetation(satellite_image_path, boundary_shapefile_path)
