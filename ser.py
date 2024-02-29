import sqlite3
con = sqlite3.connect('users.db')
cur = con.cursor()
# cur.execute("CREATE TABLE info(name, pic)")
cur.execute("""
    INSERT INTO info VALUES
        ('gal2', 'img_gal.jpg')

""")

con.commit()
