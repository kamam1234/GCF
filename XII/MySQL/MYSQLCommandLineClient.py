print('MYSQL Command Line Client v5.0.1')
import mysql.connector as sql

try:
    db = sql.connect(host = 'localhost', user = 'root', passwd = 'root', charset = 'utf8')
except Exception as e:
    print(e)
finally:
    print('\n\nThank You')
cur = db.cursor()

def show_db():
    qry = 'show databases'
    cur.execute(qry)
    data = cur.fetchall()
    print('\nAvailable databases are:')
    j = 1
    for i in data:
        print(j,":",i[0])
        j += 1

def select_db():
    try:
        qry = 'show databases'
        cur.execute(qry)
        data = cur.fetchall()
        base = int(input('\nSelect your database: '))
        qry = "use " + data[base-1][0]
        cur.execute(qry)
        print(f'\nYour selected Database is {data[base-1][0]}.')
    except Exception as e:
        print('\n',str(e))
        return
    
def show_table():
    try:
        qry = 'show tables'
        cur.execute(qry)
        data = cur.fetchall()
        print('\nAvailable Tables are:')
        j = 1
        for i in data:
            print(j,":",i[0])
            j += 1
    except Exception as e:
        print('\n', str(e))

def multiline_input():
    result = input("Enter multiple lines of text (press Ctrl+D or Ctrl+Z to stop): ")
    while True:
        line = input()
        result += "\n" + line
        if line == '':
            break
    return result

def create_table():
    try:
        cur = db.cursor()
        qry = multiline_input()
        cur.execute(qry)
        print("\nTable created successfully.")
    except Exception as e:
        print("\nError:")
        print(str(e))

def describe():
    try:
        table_name = input('Enter the table name: ')
        query = f'DESC {table_name}'
        cur.execute(query)
        results = cur.fetchall()
        if results != None:
            print(f'+ {"----------":<10} + {"---------------":<15} + {"-----":<7} + {"----------":<10} + {"---------":<10} + {"-----":<5} +')
            print(f'| {"Field":<10} | {"Type":<15} | {"Null":<7} | {"Key":<10} | {"Default":<10} | {"Extra":<5} |')
            print(f'+ {"----------":<10} + {"---------------":<15} + {"-----":<7} + {"----------":<10} + {"---------":<10} + {"-----":<5} +')
            for row in results:
                row = list(row)
                for i in range(len(row)):
                    if row[i] == None:
                        row[i] = ''
                print(f'| {row[0]:<10} | {row[1]:<15} | {row[2]:<7} | {row[3]:<10} | {row[4]:<10} | {row[5]:<5} |')
            print(f'+ {"----------":<10} + {"---------------":<15} + {"-----":<7} + {"----------":<10} + {"---------":<10} + {"-----":<5} +')
        else:
            print('\nTable is empty.')
    except Exception as e:
        print(f'\n{e}')

def select():
    try:
        cur = db.cursor()
        qry = 'show tables'
        cur.execute(qry)
        data = cur.fetchall() 
        #print(data)

        tbname = input('Enter the table you want to select: ')
        if tbname.isnumeric():
            query = f'SELECT * FROM '+ str(data[int(tbname)-1][0])
        else:
            query = f'SELECT * FROM {tbname}'
        cur.execute(query)
        data = cur.fetchall()
        if data != []:    
            l = len(data[0])
        else:
            print('\nThere is no data in selected Table.')
            return

        fstr = f'|'
        for i in range(l):
            fstr += f' {cur.column_names[i]:^15} |'
        print(fstr)
        
        for row in data:
            st = f'|'
            for j in range(len(row)):
                st += f' {row[j]:^15} |'    
            print(st)
    except Exception:
        print('\n'+Exception)

while True:
    print('\n\t__________________________________________________________')
    print('\t\tSelect from following commands to perform:')
    print('\t\t1: Show Database')
    print('\t\t2: Select Database')
    print('\t\t3: Show tables')
    print('\t\t4: Create table')
    print('\t\t5: View structure of table')
    print('\t\t6: Select table')
    print('\t\t7: Update table by column')
    print('\t\t0: Exit')


    try:
        ch = int(input('\nEnter your choice: '))

        if ch == 1:
            show_db()
    
        elif ch == 2:
            select_db()

        elif ch == 3:
            show_table()
        
        elif ch == 4:
            create_table()

        elif ch == 5:
            describe()
        
        elif ch == 6:
            select()

        elif ch == 0:
            print('\nThank You...\n')
            break

        else:
            print('\nInvalid input! Please enter again.\n')

    except Exception as e:
        print('\nInvalid Input!...\nError:' , str(e))
    
    
db.close()