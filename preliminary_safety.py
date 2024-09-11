
import dlib
import cv2

# Load the face detector
detector = dlib.get_frontal_face_detector()

# Load the facial landmark predictor
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Load the face recognition model
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load the input image
image = cv2.imread("input.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = detector(gray)

for face in faces:
    # Get the facial landmarks
    landmarks = predictor(gray, face)
    
    # Get the face descriptor
    face_descriptor = facerec.compute_face_descriptor(image, landmarks)
    
    # Perform face recognition
    # Add your own face recognition logic here
    
    # Draw a rectangle around the face
    cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)

# Display the output image
cv2.imshow("Face Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
