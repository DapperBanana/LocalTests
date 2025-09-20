
import cv2

# Load the image
image = cv2.imread('image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original and grayscale images
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)

# Save the grayscale image
cv2.imwrite('gray_image.jpg', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
