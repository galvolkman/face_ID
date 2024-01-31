import cv2
import face_recognition
"""
# Load Camera
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
# Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]"""


image = face_recognition.load_image_file("img.jpg")
face_locations = face_recognition.face_locations(image)