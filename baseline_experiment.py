
import cv2

# Load the image
image = cv2.imread('image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to segment the image
ret, segmented_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Display the segmented image
cv2.imshow('Segmented Image', segmented_image)

# Save the segmented image
cv2.imwrite('segmented_image.jpg', segmented_image)

# Close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
