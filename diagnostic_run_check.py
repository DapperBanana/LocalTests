
import cv2
import numpy as np

# Load image
image = cv2.imread('image.jpg')
image = cv2.resize(image, (400, 400))  # Resize image for faster processing

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply thresholding
_, threshold = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)

# Perform morphological operations to clean up image
kernel = np.ones((5, 5), np.uint8)
closed = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)

# Find contours
contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contour on original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# Display results
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
