import mysql.connector as con
db = con.connect(host='localhost',user='root',passwd='root',charset='utf8',\
                 database='exam')
cur = db.cursor()
# table_name = input('Enter the table you want to select: ')
query = f'SELECT * FROM tcoach'
cur.execute(query)
data = cur.fetchall()
l = len(data[0])

fstr = f'|'
for i in range(l):
    fstr += f' {cur.column_names[i]:^10} |'
print(fstr)
   
for row in data:
    st = f'|'
    for j in range(len(row)):
        st += f' {row[j]:^10} |'    
    print(st)


db.close()
