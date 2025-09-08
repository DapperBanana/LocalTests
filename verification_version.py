
import cv2
import numpy as np

# Load image
image = cv2.imread('image.jpg')

# Convert image to gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to segment image
ret, segmented_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Display original and segmented image
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', segmented_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
