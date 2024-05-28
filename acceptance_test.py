
import dlib
import face_recognition

# Load the known faces
known_face_encodings = []
known_face_names = []

# Add known faces and their names
known_face_encodings.append(face_recognition.load_image_file('known_face1.jpg'))
known_face_names.append('John Doe')
known_face_encodings.append(face_recognition.load_image_file('known_face2.jpg'))
known_face_names.append('Jane Smith')

# Load the image to recognize faces
unknown_image = face_recognition.load_image_file('unknown_face.jpg')

# Find all the faces in the image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Initialize the face recognition model
for face_encoding in face_encodings:
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = 'Unknown'

    # If a match is found, use the known name
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    print(f'Found {name} in the image')

