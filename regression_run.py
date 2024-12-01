
import cv2
import numpy as np

# Load image
image = cv2.imread('image.jpg')

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Perform thresholding
_, threshold_image = cv2.threshold(blur_image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Perform morphological operations
kernel = np.ones((5,5),np.uint8)
closing_image = cv2.morphologyEx(threshold_image, cv2.MORPH_CLOSE, kernel)

# Find contours
contours, _ = cv2.findContours(closing_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
output_image = image.copy()
cv2.drawContours(output_image, contours, -1, (0, 255, 0), 2)

# Display the segmented image
cv2.imshow('Segmented Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
