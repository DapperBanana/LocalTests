
import dlib
import numpy as np
import cv2

# Load the pre-trained face detection model
detector = dlib.get_frontal_face_detector()

# Load the pre-trained face recognition model
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_recognizer = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load the image for face recognition
image = cv2.imread("sample_image.jpg")

# Detect faces in the image
faces = detector(image)

for face in faces:
    # Get the face landmarks
    landmarks = shape_predictor(image, face)

    # Compute the face descriptor
    face_descriptor = face_recognizer.compute_face_descriptor(image, landmarks)

    # Perform face recognition by comparing the face descriptor with a known face descriptor
    # In this example, we are just printing the face descriptor
    print(np.array(face_descriptor))

    # Draw a rectangle around the face
    top_left = (face.left(), face.top())
    bottom_right = (face.right(), face.bottom())
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 3)

    # Display the image
    cv2.imshow("Face Recognition", image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
