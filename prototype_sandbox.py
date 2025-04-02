
import rasterio
from rasterio.plot import show

# Load the satellite imagery
src = rasterio.open('image.tif')

# Display the satellite imagery
show(src)

# Calculate the vegetation index - Normalized Difference Vegetation Index (NDVI)
red = src.read(3)  # Red band
nir = src.read(4)  # Near Infrared band

ndvi = (nir - red) / (nir + red)

# Display the NDVI image
show(ndvi)

# Calculate the average NDVI value
average_ndvi = ndvi.mean()
print(f"Average NDVI value: {average_ndvi}")

# Determine areas with high vegetation (NDVI > 0.5)
high_vegetation = ndvi > 0.5
show(high_vegetation, cmap='viridis')

# Save the high vegetation mask to a new file
with rasterio.open('high_vegetation.tif', 'w', **src.profile) as dst:
    dst.write(high_vegetation.astype(rasterio.uint8), 1)

