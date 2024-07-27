
import dlib
import numpy as np
import cv2

# Load the pre-trained face recognition model
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load the image
img = cv2.imread("test_image.jpg")

# Detect faces in the image
faces = detector(img)

# Loop through each face found
for face in faces:
    shape = predictor(img, face)
    face_descriptor = facerec.compute_face_descriptor(img, shape)
    
    # Perform face recognition here using the computed face descriptor
    
    # Draw rectangle around the face
    cv2.rectangle(img, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 3)
    
# Display the image with detected faces
cv2.imshow("Face Recognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
