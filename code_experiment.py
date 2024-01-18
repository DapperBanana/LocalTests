
import dlib
import cv2
import numpy as np

# Load the pre-trained facial recognition model from dlib
face_detector = dlib.get_frontal_face_detector()
face_recognizer = dlib.face_recognition_model_v1('shape_predictor_68_face_landmarks.dat')

# Load a sample image for face recognition
# Replace 'sample.jpg' with your own image file
image = cv2.imread('sample.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use the face detector to detect faces in the image
faces = face_detector(gray)

for face in faces:
    # Get the facial landmarks to align the face for recognition
    landmarks = face_recognizer.predict(gray, face)

    # Align the face using the facial landmarks
    aligned_face = dlib.get_face_chip(image, landmarks)

    # Perform face recognition
    face_encoding = face_recognizer.compute_face_descriptor(aligned_face)

    # Compare the face encoding with known faces
    # Replace 'known_face_encoding' with the known face you want to recognize
    known_face_encoding = np.array([0.1, 0.2, 0.3, ...]) # Example encoding
    distance = np.linalg.norm(face_encoding - known_face_encoding)
    
    # Define a threshold to determine if the face matches
    threshold = 0.6
    if distance < threshold:
        print("Face matches!")
    else:
        print("Face does not match.")
