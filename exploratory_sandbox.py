
import rasterio

# Open the satellite image file
sat_image = rasterio.open('path_to_satellite_image.tif')

# Read the bands of the image
red_band = sat_image.read(3)  # Red band
nir_band = sat_image.read(4)  # Near Infrared band

# Calculate the Normalized Difference Vegetation Index (NDVI)
ndvi = (nir_band - red_band) / (nir_band + red_band)

# Define thresholds for vegetation
vegetation_threshold = 0.4

# Count the number of pixels with NDVI above the threshold
vegetation_pixels = ndvi[ndvi > vegetation_threshold].size

# Calculate the percentage of vegetation in the image
total_pixels = ndvi.size
vegetation_percentage = (vegetation_pixels / total_pixels) * 100

print(f'Percentage of vegetation in the image: {vegetation_percentage:.2f}%')
