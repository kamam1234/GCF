import sqlite3 as sql

db = sql.connect('my_database.db')

cur = db.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    age INTEGER NOT NULL CHECK (age > 0)
)
''')
# cur.execute('''INSERT INTO USERS VALUES
#             (2403031260022, "KRISH PATEL", "KNPMAHADEV@GMAIL.COM", 19),
#             (2403031260023, "KISHAN PATEL", "KISHANPATEL@GMAIL.COM", 19),
#             (2403031260021, "PAL SACHIN", "PALSACHIN2006@GMAIL.COM", 19)''')

# cur.execute('''UPDATE USERS SET age = 20 WHERE id = 2403031260022''')

# cur.execute('''DELETE FROM users WHERE id = 2403031260023''')
cur.execute('''SELECT * FROM users''')
rows = cur.fetchall()
print('+---------------+---------------+--------------------------+----+')
for row in rows:
    print(f'| {row[0]:<13} | {row[1]:<13} | {row[2]:<24} | {row[3]:<2} |')
print('+---------------+---------------+--------------------------+----+')
    # print(row)
db.commit()
