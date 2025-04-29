
import dlib
import cv2

detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load an image for face recognition
img = cv2.imread("test_image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = detector(gray, 1)

for face in faces:
    shape = shape_predictor(img, face)
    face_descriptor = facerec.compute_face_descriptor(img, shape)
    # You can compare the face_descriptor with known face descriptors to recognize the person

# Display the image with rectangles around detected faces
for face in faces:
    (x, y, w, h) = (face.left(), face.top(), face.right(), face.bottom())
    cv2.rectangle(img, (x, y), (w, h), (0, 255, 0), 2)

cv2.imshow("Face Recognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
