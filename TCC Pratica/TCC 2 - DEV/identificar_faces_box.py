import face_recognition
from PIL import Image, ImageDraw
import numpy as np

jogador_img = face_recognition.load_image_file("michaeloher.jpg")
jogador_img_encoding = face_recognition.face_encodings(jogador_img)[0]

known_face_encodings = [
    jogador_img_encoding,
]
known_face_names = [
    "Jogador"
]

unknown_image = face_recognition.load_image_file("michaeloher.jpg")

face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

pil_image = Image.fromarray(unknown_image)

draw = ImageDraw.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(
        known_face_encodings, face_encoding)

    name = "Unknown"

    face_distances = face_recognition.face_distance(
        known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]

    if name == "Unknow":
        draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 0))
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10),
                        (right, bottom)), fill=(255, 0, 0), outline=(255, 0, 0))
        draw.text((left + 6, bottom - text_height - 5),
                  name, fill=(255, 255, 255, 255))
    else:
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0))
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10),
                        (right, bottom)), fill=(0, 255, 0), outline=(0, 255, 0))
        draw.text((left + 6, bottom - text_height - 5),
                  name, fill=(255, 255, 255, 255))

del draw

pil_image.show()
