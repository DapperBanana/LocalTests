
import cv2

def convert_to_grayscale(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Check if image exists
    if image is None:
        print(f"Failed to open image at {image_path}")
        return

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display original and grayscale images
    cv2.imshow('Original Image', image)
    cv2.imshow('Grayscale Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Run the program
if __name__ == '__main__':
    # Image path
    image_path = 'path_to_image.jpg'

    # Convert image to grayscale
    convert_to_grayscale(image_path)
