
import rasterio
import numpy as np

def calculate_vegetation_index(red_band, nir_band):
    vegetation_index = (nir_band - red_band) / (nir_band + red_band)
    return vegetation_index

def analyze_satellite_imagery(image_path):
    with rasterio.open(image_path) as src:
        red_band = src.read(3)
        nir_band = src.read(4)
        vegetation_index = calculate_vegetation_index(red_band, nir_band)

        mean_vegetation_index = np.mean(vegetation_index)
        max_vegetation_index = np.max(vegetation_index)
        min_vegetation_index = np.min(vegetation_index)

        print("Mean Vegetation Index:", mean_vegetation_index)
        print("Max Vegetation Index:", max_vegetation_index)
        print("Min Vegetation Index:", min_vegetation_index)

if __name__ == "__main__":
    image_path = "path/to/satellite/image.tif"
    analyze_satellite_imagery(image_path)
