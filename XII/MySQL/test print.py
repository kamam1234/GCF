import mysql.connector as con
db = con.connect(host = 'localhost', user = 'root', passwd = 'root', charset = 'utf8', database = 'exam')

cur = db.cursor()
cur.execute('show tables')
dat = cur.fetchall()
print('\nTAbles in ANKUR database are:')
j = 1
for i in dat:
    print(j,':', i[0] ,"  ",sep='', end = '')
    j += 1
print()
while True:
    ch = int(input('\nEnter table you want to select: '))


    try:
        # sname = input('Enter a Name to search: ')
        # qry = 'select * from tcoach where name = \'' + sname + '\''
        
        qry = 'select * from ' + str(dat[ch-1][0])
        cur = db.cursor()
        cur.execute(qry)
        data = cur.fetchall()
        print('+------------+-----------------+-----------------+')
        ostr = '| {:^10} | {:^15} | {:^15} |'.format(cur.column_names[0],\
                                                    cur.column_names[1],\
                                                    cur.column_names[2])
        print(ostr)
        print('+------------+-----------------+-----------------+')
        for rec in data:
            ostr = '| {:^10} | {:^15} | {:^15} |'.format(rec[0],\
                                                        rec[1],\
                                                        rec[2])
            print(ostr)
        print('+------------+-----------------+-----------------+')
        print(cur.rowcount,'records found.')
            
        # noc = len(cur.column_names)
        # for rec in data:
        #     for c in range(noc):
        #         print(cur.column_names[c],':',rec[c])
        #     print()
        # print(cur.rowcount,'records found.')
            
    except Exception as e:
        print(e)
    pass
 
db.commit()
db.close()

