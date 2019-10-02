import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

vinicius_img = face_recognition.load_image_file("vinicius.jpeg")
vinicius_encoding = face_recognition.face_encodings(vinicius_img)[0]

wevisky_img = face_recognition.load_image_file("wevisky.jpeg")
wevirky_encoding = face_recognition.face_encodings(wevisky_img)[0]

known_face_encodings = [
    vinicius_encoding,
    wevirky_encoding
]
known_face_names = [
    "Vinicius",
    "Wevisky"
]

def FaceTrue():
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2);
    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED);
    font = cv2.FONT_HERSHEY_DUPLEX;
    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1);

def FaceFalse():
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2);
    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED);
    font = cv2.FONT_HERSHEY_DUPLEX;
    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1);

def Printar(e):
    print(e);

while True:
    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"
        
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        
        if matches[best_match_index]:
            name = known_face_names[best_match_index];
            FaceTrue();
            Printar(name)
        else:
            FaceFalse();
            Printar(name);
        

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
