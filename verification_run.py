
import cv2
import numpy as np

# Load the image
image = cv2.imread('image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform thresholding to segment the image
ret, segmented_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Display the original and segmented images
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', segmented_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
