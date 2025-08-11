
import dlib
import cv2

# Load face detector and shape predictor models
detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_recognizer = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load a sample image for face recognition
image = cv2.imread("sample_image.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = detector(gray)

# Loop through each face and perform face recognition
for face in faces:
    landmarks = shape_predictor(gray, face)
    face_descriptor = face_recognizer.compute_face_descriptor(image, landmarks)
    
    # Perform face recognition logic here
    
    # Display the result
    cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)

cv2.imshow("Face Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
