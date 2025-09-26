
import dlib
import numpy as np
import cv2

# Load the pre-trained face detection model
detector = dlib.get_frontal_face_detector()

# Load the pre-trained face recognition model
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_recognizer = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load a sample image for face recognition
img = cv2.imread("test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = detector(gray)

for face in faces:
    # Get the face landmarks
    landmarks = shape_predictor(gray, face)
    
    # Get the face descriptor
    face_descriptor = face_recognizer.compute_face_descriptor(img, landmarks)
    
    # Perform face recognition
    # Compare the face descriptor with a known face descriptor
    # You can store known face descriptors in a database for comparison
    
    # Print the face descriptor (for demonstration purposes)
    print(face_descriptor)

# Display the image with bounding boxes around detected faces
for face in faces:
    x, y, w, h = face.left(), face.top(), face.width(), face.height()
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Face Recognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
