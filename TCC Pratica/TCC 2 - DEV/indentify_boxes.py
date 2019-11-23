import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import cv2

jogador_image = face_recognition.load_image_file("michaeloher.jpg")
jogador_image_encoding = face_recognition.face_encodings(jogador_image)[0]

known_face_encodings = [
    jogador_image_encoding,
]
known_face_names = [
    "Jogador",
]

unknown_image = face_recognition.load_image_file("michaeloher.jpg")


face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

pil_image = Image.fromarray(unknown_image)

draw = ImageDraw.Draw(pil_image)


def FaceTrue():
    cv2.rectangle(best_match_index, (left, top),
                  (right, bottom), (0, 255, 0), 2)
    cv2.rectangle(best_match_index, (left, bottom - 35),
                  (right, bottom), (0, 255, 0), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(best_match_index, name, (left + 6, bottom - 6),
                font, 1.0, (255, 255, 255), 1)


def FaceFalse():
    cv2.rectangle(best_match_index, (left, top),
                  (right, bottom), (0, 0, 255), 2)
    cv2.rectangle(best_match_index, (left, bottom - 35),
                  (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(best_match_index, name, (left + 6, bottom - 6),
                font, 1.0, (255, 255, 255), 1)


def MostraIMG(imagem):
    pil_image.show(imagem)


for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

    matches = face_recognition.compare_faces(
        known_face_encodings, face_encoding)

    name = "Unknown"

    face_distances = face_recognition.face_distance(
        known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]
        FaceTrue()
        MostraIMG(best_match_index)

    else:
        FaceFalse()

    # draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0))

    # text_width, text_height = draw.textsize(name)
    # draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(255, 0, 0), outline=(255, 0, 0))
    # draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

#del draw

# pil_image.show()
