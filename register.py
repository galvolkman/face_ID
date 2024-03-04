import cv2
import time
import sqlite3


name = input("to register, enter your name")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

ret, frame = cap.read()

if ret:
    frame = cv2.flip(frame, 1)

    cv2.imshow(name, frame)
    while True:

        key = cv2.waitKey(1)
        if key == ord("q"):
            break

con = sqlite3.connect('users1.db')
cur = con.cursor()
cur.execute("""
    INSERT INTO users VALUES
        ('gal2', 'img_gal.jpg')

""")

con.commit()