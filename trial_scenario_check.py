
import dlib
import cv2

# Load the pre-trained face detection model
detector = dlib.get_frontal_face_detector()

# Load the pre-trained face recognition model
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_recognizer = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load the image
image = cv2.imread("face.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = detector(gray)

for face in faces:
    # Get the facial landmarks
    landmarks = shape_predictor(image, face)

    # Get the face descriptor
    face_descriptor = face_recognizer.compute_face_descriptor(image, landmarks)

    # Perform face recognition here using the face descriptor

    # Draw a rectangle around the face
    x, y, w, h = face.left(), face.top(), face.width(), face.height()
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the image
    cv2.imshow("Face Recognition", image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
