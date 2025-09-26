
import cv2
import numpy as np

# Load image
image = cv2.imread('image.jpg')

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Apply thresholding
_, threshold_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Perform segmentation using connected components
_, labels, stats, centroids = cv2.connectedComponentsWithStats(threshold_image)

# Get the largest connected component (excluding background)
largest_label = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1

# Create a mask for the largest connected component
mask = np.uint8(labels == largest_label) * 255

# Apply the mask to the original image
segmented_image = cv2.bitwise_and(image, image, mask=mask)

# Display the segmented image
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
