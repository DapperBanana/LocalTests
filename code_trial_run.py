
import cv2
import numpy as np

# Load the image
image = cv2.imread('image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to the image
blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Perform Otsu's thresholding
_, threshold_image = cv2.threshold(blur_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours in the thresholded image
contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask image to store the segmented region
mask = np.zeros_like(image)

# Draw the contours on the mask image
cv2.drawContours(mask, contours, -1, (255, 255, 255), -1)

# Display the segmented image
segmented_image = cv2.bitwise_and(image, mask)

cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
