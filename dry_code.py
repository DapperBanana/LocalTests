
import dlib
import cv2

# Load the pre-trained face detector
detector = dlib.get_frontal_face_detector()

# Load the pre-trained face recognition model
sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

# Load the image
img = cv2.imread('test_image.jpg')

# Detect faces in the image
dets = detector(img, 1)

# Loop through each face in the image
for i, det in enumerate(dets):
    shape = sp(img, det)
    face_descriptor = facerec.compute_face_descriptor(img, shape)
    
    # Perform face recognition here
    # You can compare the face_descriptor with known face descriptors to recognize the face
    
    # Draw a rectangle around the face
    cv2.rectangle(img, (det.left(), det.top()), (det.right(), det.bottom()), (0, 255, 0), 2)

# Display the image
cv2.imshow('Face Recognition', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
