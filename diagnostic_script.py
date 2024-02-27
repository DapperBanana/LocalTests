
import dlib
import cv2

# Load the pre-trained face detection model
detector = dlib.get_frontal_face_detector()

# Load the pre-trained face recognition model
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

# Load the image
image = cv2.imread('test_image.jpg')

# Detect faces in the image
faces = detector(image)

# Iterate over the detected faces
for face in faces:
    # Predict facial landmarks
    landmarks = predictor(image, face)
    
    # Recognize face using the facial landmarks
    face_descriptor = facerec.compute_face_descriptor(image, landmarks)
    
    # Print the face descriptor
    print(face_descriptor)
