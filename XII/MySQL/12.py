import mysql.connector

try:
  cnx = mysql.connector.connect(host = 'localhost',user='root',\
                                passwd = 'root',database='ankur')
  cursor = cnx.cursor()
  cursor.execute("SELECT * bhdkdfj emp")   
  cnx.close()
except mysql.connector.ProgrammingError as err:
  pass
