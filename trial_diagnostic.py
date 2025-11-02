
import dlib
import numpy as np
import cv2

# Load the pre-trained facial recognition model
face_detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_recognizer = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load the image
image = cv2.imread("sample_image.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_detector(gray)

for face in faces:
    # Get the facial landmarks for the detected face
    shape = shape_predictor(gray, face)
    face_descriptor = face_recognizer.compute_face_descriptor(image, shape)

    # Perform face recognition
    # Add your logic here to compare the face descriptor with known faces

    # Draw a rectangle around the face
    cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)

# Display the image
cv2.imshow("Face Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
