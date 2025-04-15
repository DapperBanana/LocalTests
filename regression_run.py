
import dlib
import cv2

# Load face detection and recognition models
detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_recognizer = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load a sample image
img = cv2.imread("sample_image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = detector(gray)

# Iterate over detected faces
for face in faces:
    # Get facial landmarks
    landmarks = shape_predictor(gray, face)
    
    # Get face descriptor
    face_descriptor = face_recognizer.compute_face_descriptor(img, landmarks)
    
    # Perform face recognition (compare face descriptor with known faces)
    # Here you can define a list of known face descriptors to compare with
    
    # Display the result
    cv2.rectangle(img, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)
    cv2.putText(img, "Face", (face.left(), face.top()), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
# Display the image
cv2.imshow("Face Recognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
