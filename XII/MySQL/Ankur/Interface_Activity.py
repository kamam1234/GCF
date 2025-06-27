import mysql.connector 

db = mysql.connector.connect(host="localhost",user="root",passwd="root",\
                             charset='utf8',database="exam")

cur = db.cursor()
qry = "SELECT * FROM ACTIVITY" 
cur.execute(qry)
data = cur.fetchall()

noc = len(cur.column_names)

for rec in data:   
    for c in range(noc):
        print(cur.column_names[c],":",rec[c])
    print()

print(cur.rowcount, "records found.")

db.close()





