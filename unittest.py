
import cv2
import numpy as np

# Load the image
image = cv2.imread('image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Perform thresholding to create a binary image
_, threshold_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Perform image segmentation using watershed algorithm
markers = cv2.connectedComponents(threshold_image)[1]
markers = markers + 1
markers[threshold_image == 0] = 0
segmented_image = cv2.watershed(image, markers)

cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', segmented_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
