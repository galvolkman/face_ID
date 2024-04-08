import sqlite3
con = sqlite3.connect('users.db')
cur = con.cursor()

cur.execute("""
    SELECT pic FROM info where name = "gal";

""")
myresult = cur.fetchall()
res = myresult[0][0]


def blob_to_jpg(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
        print("Stored blob data into: ", filename, "\n")


blob_to_jpg(res, 'gal2.jpg')
