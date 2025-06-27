import mysql.connector as con

db = con.connect(user = 'root', host = 'localhost', passwd = 'root')
cur = db.cursor()
cur.execute('select curdate()')
data = cur.fetchall()
print(data)
db.close()
