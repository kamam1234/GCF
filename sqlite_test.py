import sqlite3

# Create an object for database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

#Create
cursor.execute('''CREATE TABLE IF NOT EXISTS  students(id INTEGER PRIMARY KEY AUTOINCREMENT, 
name TEXT NOT NULL, age INTEGER)''')


# Insert
cursor.execute("INSERT INTO students(name,age)VALUES(?,?)",("Harsh",21))
cursor.execute("INSERT INTO students(name,age)VALUES(?,?)",("Bob",25))

conn.commit()

cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

# Update data 
cursor.execute("UPDATE students SET age =? WHERE name = ?",(17,"Bob"))
conn.commit()


#Delete
cursor.execute("DELETE FROM students WHERE name =? ",("Bob",))
conn.commit()
