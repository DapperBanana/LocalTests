
import dlib
import cv2

# Load the face recognition model
detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_recognizer = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load an image for face recognition
img = cv2.imread("test_image.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = detector(gray)

for face in faces:
    # Get the face landmarks
    landmarks = shape_predictor(img, face)
    
    # Get the face descriptor
    face_descriptor = face_recognizer.compute_face_descriptor(img, landmarks)
    
    # Perform face recognition
    # Here you can compare the face descriptor with a known face descriptor to recognize the face
    
    # Draw a rectangle around the face
    cv2.rectangle(img, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 2)

# Display the image
cv2.imshow("Face Recognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
