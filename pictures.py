import sqlite3


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


con = sqlite3.connect('users.db')
print("Opened database successfully")
cur = con.cursor()
cur.execute("CREATE TABLE info(name TEXT NOT NULL, pic BLOB NOT NULL)")

new = convertToBinaryData('img_gal.jpg')
cur.execute("""
    INSERT INTO info VALUES
        ('gal', 'new')
        
""")

con.commit()
