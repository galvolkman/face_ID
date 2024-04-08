import cv2
import time
import sqlite3
from DBtools import DBtools


def save_pic(frame, name):
    con = sqlite3.connect('users.db')
    print("Opened database successfully")
    cur = con.cursor()

    blob_pic = dbtools.jpg_to_blob(frame)
    cur.execute('''INSERT INTO info VALUES (?,?)''', (name, blob_pic))

    con.commit()


def register():
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    name = input("to register, enter your name")

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    ret, frame = cap.read()

    if ret:
        frame = cv2.flip(frame, 1)

        cv2.imshow(name, frame)
        while True:
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)

            cv2.imshow(name, frame)
            key = cv2.waitKey(1)
            if key == ord("p"):
                save_pic(frame, name)
                break
    print(f"img saved {name}")


def main():
    dbtools = DBtools()
    register()


if __name__ == '__main__':
    main()
