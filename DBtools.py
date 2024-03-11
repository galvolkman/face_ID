import sqlite3


class DBtools:

    @staticmethod
    def jpg_to_blob(filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            blob_data = file.read()
        return blob_data

    @staticmethod
    def blob_to_jpg(data, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)
        print("Stored blob data into: ", filename, "\n")


def main():
    dbtools = DBtools()

    con = sqlite3.connect('users.db')
    print("Opened database successfully")
    cur = con.cursor()
    cur.execute("CREATE TABLE info(name TEXT NOT NULL, pic BLOB NOT NULL)")

    blob_pic = dbtools.jpg_to_blob('img_gal.jpg')
    cur.execute("""f"
        INSERT INTO info VALUES
            ('gal', {blob_pic})"

    """)

    con.commit()


if __name__ == '__main__':
    main()



