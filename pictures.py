import sqlite3  

con = sqlite3.connect('test.db')
print("Opened database successfully")
cur = con.cursor()
cur.execute("CREATE TABLE users(name, pic)")


cur.execute("""
    INSERT INTO users VALUES
        ('gal', img_gal.jpg)
        
""")

con.commit()
