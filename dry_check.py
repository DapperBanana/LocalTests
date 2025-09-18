
import rasterio
import numpy as np

# Open the satellite image
with rasterio.open('satellite_image.tif') as src:
    # Read the image as a numpy array
    image = src.read()

    # Calculate the NDVI (Normalized Difference Vegetation Index)
    red = image[0]
    nir = image[3]
    ndvi = (nir - red) / (nir + red)

    # Calculate the mean NDVI value for the image
    mean_ndvi = np.mean(ndvi)

    # Print the mean NDVI value
    print('Mean NDVI value:', mean_ndvi)

    # Calculate the percentage of vegetation cover
    vegetation_pixels = np.where(ndvi > 0.2)[0]
    vegetation_cover = len(vegetation_pixels) / ndvi.size * 100

    # Print the percentage of vegetation cover
    print('Percentage of vegetation cover:', vegetation_cover)

    # Save the NDVI image
    profile = src.profile
    profile.update(dtype=rasterio.float32)
    with rasterio.open('ndvi_image.tif', 'w', **profile) as dst:
        dst.write(ndvi.astype(rasterio.float32))

