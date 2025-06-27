import mysql.connector as mysql
import datetime
db = mysql.connect(host = 'localhost', user = 'root', \
                   passwd = 'root', database = 'exam')
cur = db.cursor()
qry = 'select * from dress'
cur.execute(qry)

s = cur.fetchall()
print('+-------+----------------+-------+-------+------------+')
ostr = '|{:^7}|{:^16}|{:^7}|{:^7}|{:^12}|'.format(cur.column_names[0],\
                                           cur.column_names[1],\
                                           cur.column_names[2],\
                                           cur.column_names[3],\
                                           cur.column_names[4])
print(ostr)
print('+-------+----------------+-------+-------+------------+')
for rec in s:
    obj = datetime.datetime.strptime(str(rec[4]), '%Y-%m-%d')
    df = obj.strftime('%Y-%m-%d')
    ostr = '|{:^7}|{:^16}|{:^7}|{:^7}|{:^12}|'.format(rec[0],\
                                                       rec[1],\
                                                       rec[2],
                                                        rec[3],\
                                                        df)
    print(ostr)
print('+-------+----------------+-------+-------+------------+')
print(cur.rowcount,'records found.')
'''
qry = 'show tables'
cur.execute(qry)
tbl = cur.fetchall()
print('Available Tables are:')
for i in range(cur.rowcount):
    print(i+1, ':', tbl[i][0])
ch = int(input('Enter your choice: '))
qry = 'select * from '+tbl[ch-1][0]
cur.execute(qry)
noc = len(cur.column_names)
data = cur.fetchall()
for rec in data:
    for c in range(noc):
        print(cur.column_names[c],':',rec[c])
    print()
print(cur.rowcount,'records found.')
'''