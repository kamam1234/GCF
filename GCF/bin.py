import pickle

import os

def write():
    try:
        f = open(r'stu_recl.dat','wb')
    except IOError:
        print('File not found.')
        return

    while True:
        rno = int(input('\nEnter Roll No.: '))
        name = input('Enter Name: ')
        marks = float(input('Enter Marks: '))

        data = [rno, name, marks]
        pickle.dump(data,f)

        ch = input('Do you want to enter more records (y/n): ')
        if ch.upper() in ['NO','N']:
            break

    f.close()

def appendr():
    try:
        f = open(r'stu_recl.dat','ab') # Changed 'wb' to 'ab' for append mode
    except IOError:
        print('File not found.')
        return

    while True:
        rno = int(input('Enter Roll No.: '))
        name = input('Enter Name: ')
        marks = float(input('Enter Marks: '))
        data = [rno, name, marks]
        pickle.dump(data,f)
        ch = input('Do you want to enter more records (y/n): ')
        if ch.upper() in ['NO','N']: # Added 'N' to the condition
            break

    f.close()

def read():
    try:
        f = open(r'stu_recl.dat','rb')

    except IOError:
        print('File not found.')
        return

    print()

    print('+--------+---------------+-------+')
    obj_string = '{:1}{:^8}{:1}{:^15}{:1}{:^7}{:1}'
    print(obj_string.format('|','Roll No.','|','Name','|','Marks','|',sep=''))

    print('+--------+---------------+-------+')

    rec = 0

    while True:

        try:
            data = pickle.load(f)

            rec += 1

            rno = data[0]
            name = data[1]
            marks = data[2]

            obj_string = '{:1}{:^8}{:1}{:^15}{:1}{:^7.2f}{:1}'
            print(obj_string.format('|',rno,'|',name,'|',marks,'|'))

        except EOFError:

            if rec == 0:
                print('|        |               |       |')
            print('+--------+---------------+-------+')

            print(rec,'record(s) found.')
            break

    f.close()

def srcmarks():

    try:
        f = open(r'stu_recl.dat','rb')

    except IOError:
        print('File not found.')
        return

    print('+--------+-------------------------+-------+')
    obj_string = '{:1}{:^8}{:1}{:^25}{:1}{:^7}{:1}'
    print(obj_string.format('|','Roll No.','|','Name','|','Marks','|'))
    print('+--------+-------------------------+-------+')

    rec = 0

    while True:
        try:
            data = pickle.load(f)

            if data[2]>=60:
                rec += 1

                obj_string = '{:1}{:^8}{:1}{:^25}{:1}{:^7.2f}{:1}'
                print(obj_string.format('|',data[0],'|',data[1],'|',data[2],'|'))

        except EOFError:
            print('+--------+-------------------------+-------+')

            print(rec,'record(s) found.')
            break

    f.close()

def search():
    try:
        f = open('stu_recl.dat','rb')
    except IOError:
        print('File not found.')
        return

    roll = int(input('Enter roll no. to search: '))

    rec = 0

    while True:
        try:
            data = pickle.load(f)
            if roll == data[0]:
                rec += 1
                print('\nRoll No.:',data[0])
                print('Name:',data[1])
                print('Marks:',data[2])
        except EOFError:
            if rec == 0:
                print('No record found.')
            else:
                print(rec, 'record(s) found.')
            break

    f.close()

def sorted_data():

    try:
        f = open(r'stu_recl.dat','rb')

    except IOError:
        print('File not found.')
        return

    print('+--------+-------------------------+-------+')
    obj_string = '{:1}{:^8}{:1}{:^25}{:1}{:^7}{:1}'
    print(obj_string.format('|','Roll No.','|','Name','|','Marks','|',sep=''))
    print('+--------+-------------------------+-------+')

    lst_rec = []

    while True:
        try:
            data = pickle.load(f)
            d = [data[2],data[1],data[0]]
            lst_rec.append(d)

        except EOFError:
            lst_rec.sort(reverse=True)

            for i in lst_rec:
                obj_string = '{:1}{:^8}{:1}{:^25}{:1}{:^7.2f}{:1}'
                print(obj_string.format('|',i[2],'|',i[1],'|',i[0],'|')) 

            print('+--------+-------------------------+-------+')

            rec = len(lst_rec)

            print(rec,'record(s) found.')
            break

    f.close()


def delete():
    try:
        sf = open('stu_recl.dat', 'rb')
    except IOError:
        print('File not found.')
        return

    tp = open('temp.dat', 'wb')
    roll = int(input('Enter roll no. to delete: '))
    rec = 0

    while True:
        try:
            data = pickle.load(sf)
            if roll == data[0]:
                rec += 1
                # Do not write this record to temp file (deleting)
            else:
                pickle.dump(data, tp)
        except EOFError:
            print(rec, 'record(s) deleted.')
            break

    sf.close()
    tp.close()

    os.remove('stu_recl.dat')
    os.rename('temp.dat', 'stu_recl.dat')

while True:

    print('\n\nChoose an option from the following:')
    print('1: Write records in new file.')
    print('2: Append records in existing file.')
    print('3: Read records from a file.')
    print('4: Search records from a file.')
    print('5: Display records having marks ^= 60.')
    print('6: Update records by roll number.')
    print('7: Delete records by roll number.')
    print('8: Display sorted records by Marks (DESC).')
    print('0: Exit.')
    ch = int(input('Enter your choice: '))

    if ch == 1:
        write()

    elif ch == 2:
        appendr()

    elif ch == 3:
        read()

    elif ch == 4:
        search()

    elif ch == 5:
        srcmarks()

    elif ch == 6:
        update()

    elif ch == 7:
        delete()

    elif ch == 8:
        sorted_data()

    elif ch == 0:
        break

    else:
        print('Invalid input.')

    input('Press Enter to continue...')