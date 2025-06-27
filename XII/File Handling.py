# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 09:26:51 2023


---------------------------------FILE HANDLING---------------------------------

-----------------------------------TEXT FILES----------------------------------
@author: Ankur (Admin)
"""

'''
WAP that reads a file and print all of its odd paragraphs in upper
case and print all of its even paragraphs in lower case.
'''
f = open(r'C:\dfh\temp.txt','r')
ls = f.readlines()
for i in range(len(ls)):
    if i % 2 == 0:
        print(ls[i].upper())
    else:
        print(ls[i].lower())
f.close()


'''
WAP that reads a file & count how many times letter 'A' & 'E'
comes in the file.
'''
# f = open(r'C:\dfh\temp.txt','r')
# s = f.read()
# s = s.upper()
# ca = ce = 0
# for ch in s:
#     if ch == 'A':
#         ca += 1
#     elif ch == 'E':
#         ce +=1
# print('Letter \'A/a\' found',ca,'times.')
# print('Letter \'E/e\' found',ce,'times.')
# print('Letter \'A/a\' & \'E/e\' found',ca+ce,'times.')


# print('Letter \'A/a\' found',s.count('A'),'times.')
# print('Letter \'E/e\' found',s.count('E'),'times.')
# print('Letter \'A/a\' & \'E/e\' found',s.count('A')+\
#       s.count('E'),'times.')
# f.close()

'''
WAP that reads a file and display 'I' instead of "E" and vice
versa while printing data on screen.
'''
# f = open(r'C:\dfh\temp.txt','r')
# s= f.read()
# s1 = ''
# for ch in s:
#     if ch == 'E':
#         s1 += 'I'
#     elif ch == 'I':
#         s1 += 'E'
#     elif ch == 'e':
#         s1 += 'i'
#     elif ch == 'i':
#         s1 += 'e'
#     else:
#         s1 += ch
# print(s1)
# f.close()


'''
WAP that reads and
find the occurance of 'Is' 'To' 'You' independently
'''
# f = open(r'C:\dfh\temp.txt','r')
# s= f.read()
# s = s.upper().split()
# print(s)
# IS, TO, YOU = 0,0,0 
# for wrd in s:
#     if wrd == 'IS':
#         IS += 1
#     elif wrd == 'TO':
#         TO += 1
#     elif wrd == 'YOU':
#         YOU += 1
# print('Word \'IS\' is found',IS,'times.')
# print('Word \'TO\' is found',TO,'times.')
# print('Word \'YOU\' is found',YOU,'times.')

# f.close()

'''
WAP that reads and
find the line(sentences) starting with T or W
'''
# f = open(r'C:\dfh\temp.txt','r')
# s= f.read()
# s = s.split('.')
# print(s)

# for l in s:
#     l = l.strip()
#     l = l.strip('\n ')
#     print(l)
#     if len(l) != 0:
#         if l.startswith('T'):
#             print(l,'.',sep='')
#         if l.startswith('W'):
#             print(l,'.',sep='')
# f.close()

'''
WAP that reads and
Bifurcate num.txt to even.txt & odd.txt
'''
# fn = open(r'C:\dfh\num.txt','r')
# fo = open(r'C:\dfh\even.txt','w+')
# fe = open(r'C:\dfh\odd.txt','w+')
# s = fn.read()
# s = s.split()
# for v in s:
#     if int(v) % 2 == 0:
#         fe.write(v)
#         fe.write(' ')
#     else:
#         fo.write(v)
#         fo.write(' ')
        
# fe.seek(0)
# fo.seek(0)
# fev = fe.read()
# fod = fo.read()
# print('File num.txt contains:')
# for v in s:
#     print(v,end=' ')
# print('\n\nFile even.txt contains:')
# print(fev)
# print('\nFile odd.txt contains:')
# print(fod)

# fn.close()
# fo.close()
# fe.close()

'''
WAP that reads and
display character statistics os a file
'''
# def str_stat(st):
#     l = len(st)
#     up = low = dig = space = sp = 0
#     for i in range(0,l):
#         if st[i].isupper():
#             up += 1
#         elif st[i].islower():
#             low +=1
#         elif st[i].isdigit():
#             dig += 1
#         elif st[i].isspace():
#             space += 1
#         else:
#             sp += 1
#     print('\nUpper:',up)
#     print('Lower:',low)
#     print('Digit:',dig)
#     print('Space:',space)
#     print('Sp. Char.:',sp)
# f = open(r'c:\dfh\temp.txt','r')
# s = f.read()
# print(s)
# str_stat(s)
# f.close()

'''
WAP that reads and
count and display occurance
of vowel characters in a file.
'''
# f = open(r'c:\dfh\temp.txt')
# s = f.read()
# print(s)
# cnt_vow = 0
# for ch in s:
#     if ch in 'aeiouAEIOU':
#         cnt_vow += 1
# print('\nNo. of Vowel Char.:',cnt_vow)
# f.close()

'''
WAP that reads and
display the words which are either
starting with C or ending with R.
'''
# def CR():
#     f = open(r'c:\dfh\temp.txt')
#     s = f.read()
#     l = s.split()
#     for wrd in l:
#         wrd = wrd.strip('\'\",.<>;:')
#         if wrd[0] in 'Cc' or wrd[-1] in 'Rr':
#             print(wrd)
#     f.close()
# CR()

'''
WAP that reads and
create another file storing
text in camel case.
'''
# def strcap(st):
#     n_st = ''
#     n_st += st[0].upper()
#     i = 1
#     while i < len(st):
#         if st[i] != ' ':
#             n_st += st[i].lower()
#             i += 1
#         elif st[i] == ' ' and st[i+1] != ' ':
#             n_st += ' '
#             n_st += st[i+1].upper()
#             i+=2
#         else:
#             i+=1
#     return n_st
# fr = open(r'c:\dfh\temp.txt','r')
# fw = open(r'c:\dfh\camelcase.txt','w')
# s = fr.read()
# s = strcap(s)
# print('\nData of file:\n')
# print(s)
# fw.write(s)
# fr.close()
# fw.close()



'''
---------------------------CSV-&-BINARY FILES----------------------------------
'''

'''
WAP that performs menu driven reading an writing operations on
CSV file containing students' record (Roll No., Name, Marks).
'''

# import csv
# def write():
#     f = open(r'c:\dfh\studetails.csv','a',newline='')
#     s_writer = csv.writer(f)
#     s = f.tell()
    
#     if s == 0:
#         s_writer.writerow(['Roll No.','Name','Marks'])
        
#     record = []
    
#     while True:
#         r = int(input('\nEnter roll no.: '))
#         n = input('Enter name: ')
#         m = float(input('Enter marks: '))
#         data = [r,n,m]
#         record.append(data)
        
#         ch = input('\nDo you want to enter more records (y/n): ')
        
#         if ch in 'nN':
#             break
        
#     s_writer.writerows(record)
    
#     f.close()
    
# def read():
#     f = open(r'c:\dfh\studetails.csv','r')
#     s_reader = csv.reader(f)
#     # print(tuple(s_reader))
    
#     cnt = 0
    
#     for i in s_reader:
#         cnt += 1
        
#         if cnt == 1:
#             print('='*43)
#             obj_string = '{:<6} {:^25} {:>10}'
#             print(obj_string.format(i[0],i[1],i[2]))
#             print('='*43)
            
#         else:
#             obj_string = '{:<6} {:^25} {:>8}'
#             print(obj_string.format(i[0],i[1],i[2]))
            
#     print('='*43)
#     print(cnt-1,'record(s) found.')
    
#     f.close()

# def src():
#     f = open(r'c:\dfh\studetails.csv','r')
#     s_reader = csv.reader(f)
#     #print(list(s_reader))
    
#     roll = int(input('\nEnter roll no. to search: '))
    
#     cnt= 0
    
#     s = 0
    
#     for i in s_reader:
#         cnt += 1
        
#         if cnt == 1:
#             print('='*43)
#             obj_string = '{:<6} {:^25} {:>8}'
#             print(obj_string.format(i[0],i[1],i[2]))
#             print('='*43)
            
#         else:
#             if (int(i[0])) == roll:
#                 s += 1
#                 obj_string = '{:<6} {:^25} {:>8}'
#                 print(obj_string.format(i[0],i[1],i[2]))
                
#     print('='*43)
#     print(s,'record(s) found.')
    
#     f.close()
    
# while True:
    
#     print('\n\nChoose an option from following:')
#     print('1: Write records in a new file')
#     print('2: Read records from a file')
#     print('3: Search records from a file')
#     print('0: Exit.')
    
#     ch = int(input('\nEnter your choice: '))
    
#     if ch == 1:
#         write()
        
#     elif ch == 2:
#         read()
        
#     elif ch == 3:
#         src()
        
#     elif ch== 0:
#         break
    
#     else:
#         print('\nInvalid Input.')
        
#     input('Press ENTER to continue...')


'''
WAP that performs following menu driven operations on binary files
containing students records (Roll No., Name, Marks)
1. Write records in new file
2. Append records in existing file
3. Read records from a file
4. Search records by roll no.
5. Update record by roll no.
'''

# import pickle

# def write():
#     f = open(r'c:\dfh\stu_rec.dat','wb')
#     record = []
    
#     while True:
#         rno = int(input('\nEnter roll no.: '))
#         name = input('Enter name: ')
#         marks = float(input('Enter marks: '))
#         data = [rno,name,marks]
#         record.append(data)
        
#         ch = input('\nDo you want to enter more records (y/n): ')
        
#         if ch in 'nN':
#             break
        
#     pickle.dump(record,f)
    
#     f.close()
    
# def appendr():
#     f = open(r'c:\dfh\stu_rec.dat')
#     record = []
#     while True:
#         rno = int(input('Enter roll no.: '))
#         name = input('Enter name: ')
#         marks = float(input('Enter marks: '))
#         data = [rno,name,marks]
#         record.append(data)
#         ch = int(input('Do you want to enter more records (y/n): '))
#         if ch in 'NOnoNonO':
#             break
#     pickle.dump(record,f)
#     f.close()
    
# def read():
#     f = open(r'c:\dfh\stu_rec.dat','rb')
#     print('='*41)
#     obj_str = '{:<8}{:^25}{:>8}'
#     print(obj_str.format('Roll no.', 'Name','Marks'))
#     print('='*41)
#     rec = 0
#     while True:
#         try:
#             record = pickle.load(f)
#             for data in record:
#                 rec += 1
#                 rno = data[0]
#                 name = data[1]
#                 marks = data[2]
#                 obj_str = '{:<8}{:^27}{:>6.2f}'
#                 print(obj_str.format(rno,name,marks))
#         except EOFError:
#             print('='*41)
#             print(rec,'record(s) found.')
#             break
#     f.close()
    
# def srcmarks():
#     f = open(r'c:\dfh\stu_rec.dat','rb')
#     print('='*41)
#     obj_string = '{:8}{:^25}{:>6}'
#     print(obj_string.format('Roll No.','Name','Marks'))
#     print('='*41)
#     rec = 0
#     while True:
#         try:
#             record = pickle.load(f)
#             for data in record:
#                 if data[2] >= 60:
#                     rec += 1
#                     obj_string = '{:<8}{:^25}{:>6.2f}'
#                     print(obj_string.format(data[0],data[1],data[2]))
#         except EOFError:
#             print('='*41)
#             print(rec,'record(s) found.')
#             break
#     f.close()
    
# def search():
#     f = open(r'c:\dfh\stu_rec.dat','rb')
#     roll = int(input('Enter roll no to search: '))
#     rec = 0
#     print('='*41)
#     obj_string = '{:8}{:^25}{:>6}'
#     print(obj_string.format('Roll No.','Name','Marks'))
#     print('='*41)
#     while True:
#         try:
#             record = pickle.load(f)
#             for data in record:
#                 if roll == data[0]:
#                     rec += 1
#                     obj_string = '{:<8}{:^25}{:>6.2f}'
#                     print(obj_string.format(data[0],data[1],data[2]))
#         except EOFError:
#             print('='*41)
#             print(rec,'record(s) found.')
#             break
#     f.close()
    
# while True:
#     print('Choose from the following options:')
#     print('1: Write records in a new file')
#     print('2: Append records in an existing file')
#     print('3: Read records from a file')
#     print('4: Search records by roll no.')
#     print("5: Display records having marks >= 60")
#     print('0: Exit')
#     ch = int(input('Enter your choice: '))
#     if ch == 1:
#         write()
#     elif ch == 2:
#         appendr()
#     elif ch == 3:
#         read()
#     elif ch  == 4:
#         search()
#     elif ch == 5:
#         srcmarks()
#     elif ch == 0:
#         break
#     else:
#         print('Invalid Input.')
#     input('\n\nPress enter to continue...')



'''
WAP that performs following menu driven operarations on binary files
containing students' records (Roll No., Name, Marks)
1: Write records in a new file
2: Append records in existing file
3: Read records from a file
4: Search records by roll no.
5: Display records having marks >= 60
6: Update records by roll no.
7: Delete records by roll no.
8: Display sorted records by marks (desc)
'''

# import pickle
# import os

# def write():
#     f = open(r'c:\dfh\stu_recl.dat','wb')
#     while True:
#         rno = int(input('\nEnter Roll No.: '))
#         name = input('Enter Name: ')
#         marks = float(input('Enter Marks: '))
#         data = [rno, name, marks]
#         pickle.dump(data,f)
#         ch = input('Do you want to enter more records (y/n): ')
#         if ch.upper in 'NO':
#             break
#     f.close()
    
# def appendr():
#     f = open(r'c:\dfh\stu_recl.dat','ab')
#     while True:
#         rno = int(input('Enter Roll No.: '))
#         name = input('Enter Name: ')
#         marks = float(input('Enter Marks: '))
#         data = [rno, name, marks]
#         pickle.dump(data,f)
#         ch = input('Do you want to enter more records (y/n): ')
#         if ch.upper() in 'NO':
#             break
#     f.close()
    
# def read():
#     try:
#         f = open(r'c:\dfh\stu_recl.dat','rb')
#     except IOError:
#         print('File not found.')
#         return
#     print()
#     print('+--------+-------------------------+-------+')
#     obj_string = '{:1}{:^8}{:1}{:^25}{:1}{:^7}{:1}'
#     print(obj_string.format('|','Roll No.','|','Name','|','Marks','|',sep=''))
#     print('+--------+-------------------------+-------+')
                     
#     rec = 0
#     while True:
#         try:
#             data = pickle.load(f)
#             rec += 1
#             rno = data[0]
#             name = data[1]
#             marks = data[2]
#             obj_string = '{:1}{:^8}{:1}{:^25}{:1}{:^7.2f}{:1}'
#             print(obj_string.format('|',rno,'|',name,'|',marks,'|'))
#         except EOFError:
#             if rec == 0:
#                 print('|        |                         |       |')
#             print('+--------+-------------------------+-------+')
#             if rec == 0:
#                 print('0 records found.')
#             elif rec == 1:
#                 print('1 record found.')
#             else:
#                 print(rec,'record(s) found.')
#             break
#     f.close()

# def srcmarks():
#     try:
#         f = open(r'c:\dfh\stu_recl.dat','rb')
#     except IOError:
#         print('File not found.')
#         return
#     print('+--------+-------------------------+-------+')
#     obj_string = '{:1}{:8}{:1}{:^25}{:1}{:^7}{:1}'
#     print(obj_string.format('|','Roll No.','|','Name','|','Marks','|',sep=''))
#     print('+--------+-------------------------+-------+')
#     rec = 0
#     while True:
#         try:
#             data = pickle.load(f)
#             if data[2]>60:
#                 rec += 1
#                 obj_string = '{:1}{:^8}{:1}{:^25}{:1}{:^7.2f}{:1}'
#                 print(obj_string.format('|',data[0],'|',data[1],'|',data[2],'|'))
#         except EOFError:
#             print('+--------+-------------------------+-------+')
#             if rec == 0:
#                 print('0 records found.')
#             elif rec == 1:
#                 print('1 record found.')
#             else:
#                 print(rec,'record(s) found.')
#             break
#     f.close()

# def search():
#     f = open(r'c:\dfh\stu_recl.dat','rb')
#     roll = int(input('Enter roll no. to search: '))
#     rec = 0
#     while True:
#         try:
#             data = pickle.load(f)
#             if roll == data[0]:
#                 rec += 1
#                 print('\nRoll No.:',data[0])
#                 print('Name:',data[1])
#                 print('Marks:',data[2])
#         except EOFError:
#             if rec == 0:
#                 print('There is no record with such roll no.')
#             else:
#                 if rec == 0:
#                     print('0 records found.')
#                 elif rec == 1:
#                     print('1 record found.')
#                 else:
#                     print(rec,'record(s) found.')
#             break
#     f.close()

# def update():
#     sf = open(r'c:\dfh\stu_recl.dat','rb')
#     tp = open(r'c:\dfh\temp.dat','wb')
#     roll = int(input('Enter roll to update: '))
#     rec = 0
#     while True:
#         try:
#             data = pickle.load(sf)
#             if data[0] == roll:
#                 rec += 1
#                 print('\nRoll No.: ',data[0])
#                 print('Name:',data[1])
#                 print('Marks:',data[2])
#                 data[0] = int(input('Enter Roll no.: '))
#                 data[1] = input('Enter Name: ')
#                 data[2] = float(input('Enter marks: '))
#             pickle.dump(data,tp)
#         except EOFError:
#             if rec == 0:
#                 print('0 records found.')
#             elif rec == 1:
#                 print('1 record found.')
#             else:
#                 print(rec,'record(s) found.')
#             break
#     sf.close()
#     tp.close()
#     os.remove(r'c:\dfh\stu_recl.dat')
#     os.rename(r'c:\dfh\temp.dat',r'c:\dfh\stu_recl.dat')

# def delete():
#     sf = open(r'c:\dfh\stu_recl.dat','rb')
#     tp = open(r'c:\dfh\temp.dat','wb')
#     roll = int(input('Enter Roll No. to delete: '))
#     rec = 0
#     while True:
#         try:
#             data = pickle.load(sf)
#             if data[0] == roll:
#                 print('\nRoll No.:',data[0])
#                 print('Name:',data[1])
#                 print('Marks:',data[2])
#                 ch = input('Are you sure (y/n): ')
#                 if ch in 'YESYesYeSyEsyES':
#                     rec+= 1
#                 else:
#                     pickle.dump(data,tp)             
#             else:
#                 pickle.dump(data,tp)
#         except EOFError:
#             if rec == 0:
#                 print('0 records found.')
#             elif rec == 1:
#                 print('1 record found.')
#             else:
#                 print(rec,'record(s) found.')
#             break
#     sf.close()
#     tp.close()
#     os.remove(r'c:\dfh\stu_recl.dat')
#     os.rename(r'c:\dfh\temp.dat',r'c:\dfh\stu_recl.dat')

# def sorted_data():
#     try:
#         f = open(r'c:\dfh\stu_recl.dat','rb')
#     except IOError:
#         print('File not found.')
#         return
#     print('+--------+-------------------------+-------+')
#     obj_string = '{:1}{:8}{:1}{:^25}{:1}{:^7}{:1}'
#     print(obj_string.format('|','Roll No.','|','Name','|','Marks','|',sep=''))
#     print('+--------+-------------------------+-------+')
#     lst_rec = []
#     while True:
#         try:
#             data = pickle.load(f)
#             d = [data[2],data[1],data[0]]
#             lst_rec.append(d)
#         except EOFError:
#             lst_rec.sort(reverse=True)
#             for i in lst_rec:
#                 obj_string = '{:1}{:^8}{:1}{:^25}{:1}{:^7.2f}{:1}'
#                 print(obj_string.format('|',i[2],'|',i[1],'|',i[0],'|'))
#             print('+--------+-------------------------+-------+')
#             break
#     f.close()
    
# while True:
#     print('\n\nChoose an option from the following:')
#     print('1: Write records in new file.')
#     print('2: Append records in existing file.')
#     print('3: Read records from a file.')
#     print('4: Search records from a file.')
#     print('5: Display records having marks >= 60.')
#     print('6: Update records by roll number.')
#     print('7: Delete records by roll number.')
#     print('8: Display sorted records by Marks (DESC).')
#     print('0: Exit.')
#     ch  = int(input('Enter your choice: '))
#     if ch == 1:
#         write()
#     elif ch == 2:
#         appendr()
#     elif ch == 3:
#         read()
#     elif ch == 4:
#         search()
#     elif ch == 5:
#         srcmarks()
#     elif ch == 6:
#         update()
#     elif ch == 7:
#         delete()
#     elif ch == 8:
#         sorted_data()
#     elif ch == 0:
#         break
#     else:
#         print('Invalid input.')
#     input('Press Enter to continue...')