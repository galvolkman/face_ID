import cv2
import threading
import face_recognition
import ctypes
import time


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

ref_img = cv2.imread("img.jpg")


def check_face(frame):
    global face_match

    known_image = face_recognition.load_image_file("img.jpg")
    unknown_image = frame
    known_encoding = face_recognition.face_encodings(known_image)[0]
    try:
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    except IndexError:
        results = [False]
        print(results)
        face_match = results[0]
        return

    results = face_recognition.compare_faces([known_encoding], unknown_encoding)
    print(results)
    face_match = results[0]


while True:
    ret, frame = cap.read()

    if ret:
        frame = cv2.flip(frame, 1)
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(), )).start()
            except ValueError:
                pass

        counter += 1

        if not face_match:

            ctypes.windll.user32.BlockInput(True)
            ctypes.windll.user32.LockWorkStation()
            # time.sleep(1)

        #cv2.imshow("video", frame)


    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
counter = 0
face_match = False





