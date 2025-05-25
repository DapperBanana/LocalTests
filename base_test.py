
import dlib
import cv2

# Load the pre-trained facial recognition model
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load the image for face recognition
img = cv2.imread("test_image.jpg")

# Convert the image to grayscale for face detection
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = detector(gray_img)

# Loop through each face found in the image
for face in faces:
    landmarks = predictor(gray_img, face)
    face_encoding = facerec.compute_face_descriptor(img, landmarks)
    
    # Perform face recognition
    # You can compare the face encoding with known face encodings to identify the person
    
    # Display the image with face recognition results
    cv2.rectangle(img, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)
    
# Display the image
cv2.imshow("Face Recognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
