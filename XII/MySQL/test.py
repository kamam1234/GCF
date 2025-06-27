# import mysql.connector as con
# db = con.connect(host='localhost',user='root',\
#                      passwd ='root',database='exam',charset='utf8')

#      # sname = input('Enter a Name to search: ')
#      # qry = 'select * from tcoach where name = \'' + sname + '\''
  
# qry = 'select * from tcoach'
# cur = db.cursor()
# cur.execute(qry)
# data = cur.fetchall()
# print('-'*36)
# ostr = '| {:^6} | {:^15} | {:^5} |'.format(cur.column_names[0],\
#                                                cur.column_names[1],\
#                                                cur.column_names[2])
# print(ostr)
# print('-'*36)
# for rec in data:
#         ostr = '| {:^6} | {:^15} | {:^5} |'.format(rec[0],\
#                                                    rec[1],\
#                                                    rec[2])
# print(ostr)
# print('-'*36)
# print(cur.rowcount,'records found.')
        
#         # noc = len(cur.column_names)
#         # for rec in data:
#         #     for c in range(noc):
#         #         print(cur.column_names[c],':',rec[c])
#         #     print()
#         # print(cur.rowcount,'records found.')
# db.close()


import mysql.connector as con
db = con.connect(host = 'localhost', user = 'root', passwd = 'tiger', database = 'SCHOOL')

cur = db.cursor()
rno = int(input('Enter Roll No.: '))
name = input('ENter name: ')
DOB = input('Enter date of birth (YYYY-MM-DD): ')
fee = float(input('Enter fee: '))
# qry = 'insert into Student values({}, "{}", "{}", {})'
# qry.format(rno, name, DOB, fee)



qry = f'insert into student values({rno}, "{name}", "{DOB}", {fee})'




cur.execute(qry)

db.commit()
    
db.close()

