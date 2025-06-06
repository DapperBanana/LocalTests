
import cv2
import numpy as np

# Load an image
image = cv2.imread('image.jpg')

# Reshape the image so that it can be fed into the K-means clustering algorithm
reshaped_image = image.reshape((-1, 3))

# Convert the image data type to float32
reshaped_image = np.float32(reshaped_image)

# Define criteria for K-means algorithm
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

# Perform K-means clustering
k = 3
_, labels, centers = cv2.kmeans(reshaped_image, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert the centers to integers
centers = np.uint8(centers)

# Assign each pixel to its corresponding cluster center
segmented_image = centers[labels.flatten()]

# Reshape the segmented image back to its original shape
segmented_image = segmented_image.reshape(image.shape)

# Display the original and segmented image
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
