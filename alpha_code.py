
import cv2
import numpy as np

# Load an image
image = cv2.imread('input_image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a threshold to get a binary image
_, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Find contours in the binary image
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask image to store the segmented image
mask = np.zeros_like(gray_image)

# Draw contours on the mask image
cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

# Perform bitwise AND operation between the original image and the mask image
segmented_image = cv2.bitwise_and(image, image, mask=mask)

# Display the segmented image
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
