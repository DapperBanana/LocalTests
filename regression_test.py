
import dlib
import cv2

# Load pre-trained face detection and face recognition models
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load an image for face recognition
img = cv2.imread("test_image.jpg")

# Detect faces in the image
detections = detector(img, 1)

# Iterate over detected faces
for detection in detections:
    shape = predictor(img, detection)
    face_descriptor = facerec.compute_face_descriptor(img, shape)
    
    # Perform face recognition here
    # You can compare the face descriptor with a database of known faces to identify the person
    
    cv2.rectangle(img, (detection.left(), detection.top()), (detection.right(), detection.bottom()), (0, 255, 0), 2)

# Display the image with detected faces
cv2.imshow("Face Recognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
