
import cv2
import numpy as np

# Load the input image
image = cv2.imread('input_image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise in the image
blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Perform Otsu's thresholding to binarize the image
_, threshold_image = cv2.threshold(blur_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Perform image segmentation using connected components
output_image = cv2.connectedComponentsWithStats(threshold_image, connectivity=4)

# Display the segmented image
segmented_image = np.zeros_like(image)
for i in range(1, output_image[0]):
    segmented_image[output_image[1] == i] = np.random.randint(0, 255, 3)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
