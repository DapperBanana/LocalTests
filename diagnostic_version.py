
import dlib
import numpy as np
import cv2

# Load the pre-trained face detection model
detector = dlib.get_frontal_face_detector()

# Load the pre-trained face recognition model
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load the image to be recognized
img = cv2.imread("test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = detector(gray)

# Iterate over each detected face
for face in faces:
    shape = shape_predictor(gray, face)
    face_descriptor = facerec.compute_face_descriptor(img, shape)

    # Sample face descriptor for recognition
    known_face_descriptor = np.array([0.1, 0.2, 0.3, ..., 0.9])

    # Calculate the Euclidean distance between the known face descriptor and the current face descriptor
    distance = np.linalg.norm(face_descriptor - known_face_descriptor)

    # Define a threshold for face recognition
    threshold = 0.6

    if distance < threshold:
        print("Face recognized!")
    else:
        print("Unknown face")

# Display the image with rectangles drawn around detected faces
for face in faces:
    x, y, w, h = face.left(), face.top(), face.right() - face.left(), face.bottom() - face.top()
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Face Recognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
