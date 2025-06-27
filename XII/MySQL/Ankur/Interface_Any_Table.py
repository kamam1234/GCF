import mysql.connector

dbname = input("Enter database name to connect:")
print()
try:
    db = mysql.connector.connect(host="localhost",user="root",passwd="root",charset='utf8',database=dbname)

    qry = "SHOW TABLES"
    cur = db.cursor()
    cur.execute(qry)

    print("TABLES AVAILABLE UNDER '",dbname,"' DATABASE", sep ="")

    i=1
    for t in cur:
        print(i,"-",t[0].upper())
        i += 1


    tbl = input("ENTER TABLE NAME:")

    qry = "SELECT * FROM " + tbl
    print()
    cur.execute(qry)

    
    data = cur.fetchall()
    
    # print(data)
    col = len(cur.column_names)

    for rec in data:
        for c in range(col):
            print(cur.column_names[c],":",rec[c])
        print()

    print(cur.rowcount, "records found.")

    
    db.close()
except mysql.connector.errors.ProgrammingError:
    print('Such Database does not exist.')

