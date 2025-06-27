import mysql.connector as con
    
def create():
    try:
        cur = db.cursor()
        cur.execute('create table tcoach\
                    (\
                    pcode varchar(4),\
                    name varchar(20),\
                    acode varchar(5))')
    except Exception as e:
        # print(e)
        pass

def t_ins():
    try:
        pcode = input('Enter Coach Code: ')
        name = input('Enter Coach Name: ')
        acode = input('Enter Activity Code: ')
        
        qry = f"insert into tcoach values('{pcode}','{name}','{acode}')"
        cur = db.cursor()
        cur.execute(qry)
    except Exception as e:
        # print(e)
        pass

def t_sel():
    try:
        # sname = input('Enter a Name to search: ')
        # qry = 'select * from tcoach where name = \'' + sname + '\''
        
        qry = 'select * from tcoach'
        cur = db.cursor()
        cur.execute(qry)
        data = cur.fetchall()
        print('+--------+-----------------+-------+')
        ostr = f'| {cur.column_names[0]:^6} | {cur.column_names[1]:^15} | {cur.column_names[2]:^5} |'
        print(ostr)
        print('+--------+-----------------+-------+')
        for rec in data:
            ostr = f'| {rec[0]:^6} | {rec[1]:^15} | {rec[2]:^5} |'
            print(ostr)
        print('+--------+-----------------+-------+')
        print(cur.rowcount,'records found.')
        
        # noc = len(cur.column_names)
        # for rec in data:
        #     for c in range(noc):
        #         print(cur.column_names[c],':',rec[c])
        #     print()
        # print(cur.rowcount,'records found.')
        
    except Exception as e:
        # print(e)
        pass
        
def t_upd():
    try:
        ccode = input('Enter Coach code to update: ')
        qry = 'select * from tcoach where pcode = \''+ ccode + '\''
        cur = db.cursor()
        cur.execute(qry)
        data = cur.fetchone()
        print('Coach code:',data[0])
        print('Coach name:',data[1])
        print('Activity code:',data[2])
        
        ncode = input('Enter new Coach Code (press ENTER to keep same: )')
        if ncode == '':
            ncode = data[0]
        
        cname = input('Enter new Coach Name (press ENTER to keep same: )')
        if cname == '':
            cname = data[1]
        
        acode = input('Enter new Activity Code (press ENTER to keep same: )')
        if acode == '':
            acode = data[2]
        
        qry = f"update tcoach set pcode = '{ncode}', name = '{cname}', acode = '{acode}' where \
            pcode = '{ccode}'"
        
        cur = db.cursor()
        cur.execute(qry)
        print(cur.rowcount, 'records updated.')
    except Exception as e:
        # print(e)
        pass
    
def t_del():
    try:
        code = input('Enter Coach code to delete: ')
        qry = f"delete from tcoach where pcode = '{code}'"
        cur = db.cursor()
        cur.execute(qry)
    except Exception as e:
        # print(e)
        pass
        
while True:
    db = con.connect(host='localhost',user='root',\
                      passwd ='root',database='ankur',charset='utf8')
    
    create()
    
    print('\n\nSelect operation that you want to perform on TCOACH table: ')
    print('\n1: Create Table.')
    print('2: Insert Record.')
    print('3: Select Record.')
    print('4: Update record.')
    print('5: Delete record.')
    print('0: Exit.')
    
    ch = int(input('Enter your choice: '))
    print()
    
    if ch == 1:
        create()
    
    elif ch == 2:
        t_ins()
        
    elif ch == 3:
        t_sel()
        
    elif ch == 4:
        t_upd()
        
    elif ch == 5:
        t_del()
        
    elif ch == 0:
        print('Thank You.')
        break
    
    else:
        print()
    
        
    db.commit()
    db.close()
    print('Press ENTER to continue...')
