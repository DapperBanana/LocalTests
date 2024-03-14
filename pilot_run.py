
import dlib
import cv2

# Load the dlib face recognition model
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load the input image
image = cv2.imread("input_image.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = detector(gray)

# Iterate over each detected face
for face in faces:
    shape = predictor(gray, face)
    face_descriptor = facerec.compute_face_descriptor(image, shape)
    
    # Perform face recognition by comparing the face descriptor with a known face descriptor
    # (You can implement your own logic here to match faces)
    
    # Draw a rectangle around the detected face
    cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)

# Display the output image
cv2.imshow("Face Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
