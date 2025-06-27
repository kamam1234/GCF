# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 13:40:22 2023
Journal
@author: Ankur (Admin)
"""

'''
1 WAP to find sum of two durations in hours and minutes
'''
# h1 = int(input('Enter 1st hour: '))
# m1 = int(input('Enter 1st min: '))
# h2 = int(input('Enter 2nd hour: '))
# m2 = int(input('Enter 2nd min: '))
# tm = (h1*60) + (h2*60) + m1 + m2
# th = tm //60
# sm = tm % 60
# print('\nDuration 1: ',h1,':',m1,sep = '')
# print('Duration 2: ',h2,':',m2,sep = '')
# print('Total Duration: ',th,':',sm,sep = '')

'''
2 Wap that prints if a year is a leap year or not.
'''
# y = int(input('Enter a year: '))
# if (y%1000 == 0) or (y%100 != 0) and (y%4 == 0):
#     print(y,'is a leap year.')
# else:
#     print(y,'is not a leap year.')

'''
3 Wap to print fibonacci series upto the number entered by the user
'''
# n = int(input("Enter the value of N: "))
# a = 0
# b = 1
# if n <= 0:
#     print("Invalid input!")
# elif n == 1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(2, n):
#         c = a + b
#         a = b
#         b = c
#         if c < n:
#             print(c)

'''
4 WaP to print factor of a given number.
'''
# n = int(input('Enter a number: '))
# print('Factors of',n,'are:')
# for i in range(1,(n//2)+1):
#     if n % i == 0:
#         print(i,end=' ')
# print(n)

'''
5 WAp to print alphabetic series
    1. A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    2. Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Oo Pp Qq Rr Ss
       Tt Uu Vv Ww Xx Yy Zz
    3. A b C d E f G h I j K l M n O p Q r S t U v W x Y z
    4. ABc DEf GHi JKl MNo PQr STu VWx YZ
    5. aBc dEf gHi jKl mNo pQr sTu vWx yZ
    6. AB cd EF gh IJ kl MN op QR st UV wx YZ
'''
# print('\n\nSeries 1:')
# for i in range(1,27):
#     print(chr(i+64),end = ' ')
    
# print('\n\nSeries 2:')
# for i in range(1,27):
#     print(chr(i+64),chr(i+96),end = ' ',sep='')
    
# print('\n\nSeries 3:')
# for i in range(1,27):
#     if i % 2 == 0:
#         print(chr(i+96),end = ' ')
#     else:
#         print(chr(i+64),end=' ')


# print('\n\nSeries 4:')
# for i in range(1,27):
#     if i% 3 == 1:
#         print(chr(i+64),end = '')
#     elif i % 3 ==2:
#         print(chr(i+64),end = '')
#     else:
#         print(chr(i+96),end = ' ')
        
# print('\n\nSeries 5:')
# for i in range(1,27):
#     if i% 3 == 1:
#         print(chr(i+96),end = '')
#     elif i % 3 ==2:
#         print(chr(i+64),end = '')
#     else:
#         print(chr(i+96),end = ' ')
        
# print('\n\nSeries 6:')
# for i in range(1,27):
#     if i% 4 == 1:
#         print(chr(i+64),end = '')
#     elif i % 4 ==2:
#         print(chr(i+64),end = ' ')
#     elif i % 4 == 3:
#         print(chr(i+96),end = '')
#     else:
#         print(chr(i+96),end = ' ')

'''
6 WAP that prints prime numbers between 2 & 100
'''
# print('Prime numbers between 2 & 100 are:')
# for x in range(2,101):
#     for i in range(2,x):
#         if (x%i==0):
#             break
#     else:
#         print(x,end=' ')


'''
7 WAP that prints armstrong numbers between 1 & 1000
'''
# print("Armstrong no.s between 1 and 1000: ")
# for i in range(1,1001):
#     soc = 0
#     j = i
#     while i > 0:
#         soc += (i%10)**3
#         i = i//10
#     if soc == j:
#         print(j,end=" ")


'''
8 WAP that finds the occurence of a character in a string.
Also print the position where character is found.
'''
# st = input('Enter a string: ')     ## Occurence is also to be found
# ch = input('Enter character to find: ')
# f = 0
# print('\nCharacter found at position(s):')
# for i in range(0,len(st)):
#     if st[i].upper() == ch.upper():
#         print(i+1,end= ' ')
#         f += 1
# print('\nCharacter found',f,'times.')


'''
9 WAP that accepts a list and print the sum of even values
and sum of odd values. Also print sum of even positioned 
values and odd positioned values.
'''
# lst = eval(input('Enter a list: '))
# so  = se = sop = sep = 0
# for i in range(0,len(lst)):
#     if i % 2 == 0:
#         sop += lst[i]
#     else:
#         sep += lst[i]
#     if lst[i]%2 == 0:
#         se += lst[i]
#     else:
#         so += lst[i]
# print('\nEntered list:',lst)
# print('Sum of odd positioned values:',sop)
# print('Sum of even positioned values:',sep)
# print('Sum of odd values:',so)
# print('Sum of odd values:',se)

'''
10 WAP that accepts two lists and print if they are separated
or overlapped lists.
'''
# l1  = eval(input('Enter 1st list:'))
# l2  = eval(input('Enter 2nd list:'))
# for v in l1:
#     if v in l2:
#         print('\nLists are overlapped.')
#         break
# else:
#     print('\nLists are separated.')

'''
11 WAP that accepts a list and swap each odd positioned element
with the next element(if available)
'''
# lst = eval(input('Enter a list: '))
# print('\n\nList before swapping:',lst)
# for i in range(1,len(lst),2):
#     lst[i],lst[i-1] = lst[i-1], lst[i]
# print('List after swapping:',lst)



'''
12 Create a function GCD_LCM() that accepts two integer arguments
and return GCD & LCM of given numbers.
using above function, make a program that accepts two numbers from
a user and prints GCD & LCM of given numbers.
'''
# def GCD_LCM(x,y):
#     if x<y:
#         small = x
#     else:
#         small = y
#     for i in range(small,0,-1):
#         if x%i == 0 and y%i == 0:
#             return i, ((x*y)//i)
        
# x = int(input('Enter 1st no.: '))
# y = int(input('Enter 2nd no.: '))
# g, l = GCD_LCM(x,y)
# print('GCD:',g)
# print('LCM:',l)

'''
13 Create a function isprime() that accepts an integer as argument
and return True if supplied number is a prime number; otherwise 
return False.
Using above function, make a program that prints prime numbers
between 2 & N (N is supplied by user)
'''
# def isprime(n):
#     for i in range(2,(n//2)+1):
#         if n % i == 0:
#             return False
#     else:
#         return True
    
# num = int(input('Enter a number: '))
# print('Prime no.s between 2 &',num,'are :')
# for i in range(2,num+1):
#     if isprime(i):
#         print(i,end = ' ')


'''
14 Create a function median() that accepts a list as arguments and
return median of supplied list.
Using above function, make a program that prints median of 
entered list (list is supplied by user)
'''
# def median(lst):
#     lst.sort()
#     n = len(lst)
#     if n%2 != 0:
#         return lst[n//2]
#     else:
#         return (lst[(n//2)-1] + lst[n//2])/2

# lst_main = eval(input('Enter a list: '))
# print('Original List:',lst_main)
# med = median(lst_main)
# print('Sorted List:',lst_main)
# print('Median:',med)


'''
15 Create a function rotate() that accepts a list and an integer
s arguments and rotates the list with roatation factor as supplied
argument.
Using above function, make a program that accepts a list and
rotation factor from user and rotate the list accordingly.
'''
# def rotate(rl,r):
#     l = len(rl)
#     n_lst = []
#     n_lst += rl[l-r:]
#     n_lst += rl[:l-r]
#     rl = list(n_lst)
#     return rl

# lst = eval(input('Enter a list: '))
# r = int(input('Enter rotation factor: '))
# print('\nEntered list:',lst)
# lst = rotate(lst, r)
# print('New list:',lst)

'''
16 Write a menu driven program that prints string statistics; a
string is palindrome or not; printing string in reverse case;
and print capitalized string using different functions.
'''
# def str_stat(s):
#     l = len(s)

#     up = low = dig = space = sp = 0

#     for i in range(0,l):
#         if s[i].isupper():
#             up += 1
#         elif s[i].islower():
#             low += 1
#         elif s[i].isdigit():
#             dig += 1
#         elif s[i].isspace():
#             space += 1
#         else:
#             sp += 1

#     print('\nString:',s)    
#     print("Upper: ",up)
#     print("Lower: ",low)
#     print("Digits: ",dig)
#     print("Space: ",space)
#     print("Special char.: ",sp)
    
# def str_palin(st):
#     if st.upper() == st[::-1].upper():
#         return True
#     else:
#         return False

# def str_rev_case(st):
#     l = len(st)
#     r_st = ''
#     for i in range(0,l):
#         if st[i].isupper():
#             r_st += st[i].lower()
#         else:
#             r_st += st[i].upper()
#     return r_st

# def str_cap(st):
#     n_st = ''
#     n_st += st[0].upper()
    
#     i =1
#     while (i < len(st)):
#         if (st[i] != ' '):
#             n_st += st[i].lower()
#             i += 1
#         elif (st[i] == ' ' and st[i+1] != ' '):
#             n_st += ' '
#             n_st += st[i+1].upper()
#             i +=2
#         else:
#             n_st += ' '
#             i += 1
#     return n_st



# strn = input('Enter a string: ')

# while True:
#     print('\n1: String Statistics:')
#     print('2: Print if string is palin or not:')
#     print('3: Print reversed case string:')
#     print('4: Print Capitalized string:')
#     print('0: Exit:')
#     ch = int(input('Enter your choice [1/2/3/4/0]: '))
    
#     if ch == 1:
#         str_stat(strn)
#     elif ch ==2:
#         if str_palin(strn):
#             print('\'',strn,'\'','is palin.',sep='')
#         else:
#             print('\'',strn,'\'',' is not palin.',sep='')
#     elif ch == 3:
#         print('Reversed case string:',str_rev_case(strn))
#     elif ch == 4:
#         print('Capitalized String:',str_cap(strn))
#     elif ch == 0:
#         break
#     else:
#         print('Invalid input.')
#     input('Press enter to continue...')

'''
17
WAP that reads a file and prints all of its odd paragraphs
in uppercase and print all of its even paragraphs in lower case.
'''
# f = open(r'c:\dfh\temp.txt','r')
# ls = f.readlines()
# for i in range(len(ls)):
#     if i % 2 == 0:
#         print(ls[i].upper())
#     else:
#         print(ls[i].lower())
# f.close()

'''
18
WAP that reads a file and diplay 'I' instead of 'E' and vice-versa
while printing on screen.
'''
# f = open(r'c:\dfh\temp.txt','r')
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
19
WAP that reads a file and diplay character statistics of file
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
20
WAP that reads a file and count and display the occurence of the
words 'IS', 'TO' and 'YOU'.
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
21
WAP that reads a file and display the words which are either
starting with 'C' or ending with 'R'.
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
22
WAP that reads a file and display the lines which are starting
with 'T' or 'W'.
'''
# f = open(r'C:\dfh\temp.txt','r')
# s= f.read()
# s = s.split('.')
# print(s)

# for l in s:
#     l = l.strip()
#     l = l.strip('\n')
#     if len(l) != 0:
#         if l[0] in 'TW':
#             print(l+'.')
# f.close()

'''
23
WAP that reads a file and create another file storing text in
camel case.
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
24
WAP that reads and write numbers from NUM.txt to two different
files named EVEN.txt and ODD.txt containing even and odd numbers
respectively. Program should display contents of all files on screen
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
25
WAP that performs menu driven reading and writing operaions on CSV
file containing students record (Roll No., Name, Marks).
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
#             obj_string = '{:<8} {:^25} {:>8}'
#             print(obj_string.format(i[0],i[1],i[2]))
#             print('='*43)
            
#         else:
#             obj_string = '{:<8} {:^25} {:>8}'
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
26
WAP that performs menu driven operations on binary file containing
students record (Roll No., Name, Marks)
1. Write records in a new file.
2. Appends records in an existing file
3. Read records from a file.
4. Search record by Roll No.
5. Display recordsw having marks >= 60.
6. Update record by Roll No.
7. Delete record by Roll No.
8. Display sorted records by marks in descending order.
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
#         if ch.upper() in 'NO':
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
#             print(rec,'records found. (0.00 sec)')
            
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
#                 print('0 records found. (0.00 sec)')
#             elif rec == 1:
#                 print('1 record found. (0.01 sec)')
#             else:
#                 print(rec,'record(s) found. (0.03 sec)')
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
#                     print('0 records found. (0.00 sec)')
#                 elif rec == 1:
#                     print('1 record found. (0.01 sec)')
#                 else:
#                     print(rec,'record(s) found. (0.02 sec)')
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
#             print(rec,'record(s) updated. (0.03 sec)')
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
#                 if ch.upper() in 'YES':
#                     rec+= 1
#                 else:
#                     pickle.dump(data,tp)             
#             else:
#                 pickle.dump(data,tp)
#         except EOFError:
#             print(rec,'record(s) deleted. (0.02 sec)')
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
#             rec = len(lst_rec)
#             print(rec,'record(s) found. (0.04 sec)')
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
    
'''
27
WAP that implemments linear search using function.
'''
# def insert(arr):
#     roll = int(input("Enter roll :"))
#     name = input("Enter name :")
    
#     ele = [roll, name]

#     arr.append(ele)
#     print("Element", ele, "is added at the end.")

# def display(arr):
#     if len(arr) == 0:
#         print("Array is empty.")
#     else:
#         print("Elements of the array :")
#         for i in range(0, len(arr)):
#             print("Element at position", i+1, ":", arr[i])

# def lsearch(arr,sname):
#     for i in range(0, len(arr)):
#         if arr[i][1] == sname:
#             return arr[i], i+1
    
#     return None, None

# ds = []

# while (True):
#     print("\n\n")
#     print("1 : Insert an element")
#     print("2 : Display elements")
#     print("3 : Search element")
#     print("0 : Exit")
#     ch = int(input("Enter your choice :"))
    
#     if ch == 1:
#         insert(ds)
        
#     elif ch == 2:
#         display(ds)
    
#     elif ch == 3:
#         sname = input("Enter name to search:")
#         r, p = lsearch(ds,sname)
#         if p == None:
#             print("Name", sname, "is not found.")
#         else:
#             print("Record", r, "is found at position", p) 
        
#     elif ch == 0:
#         break
    
#     else:
#         print("Invalid Input.")
        
'''
28
WAP that implements binary search using function.
'''
# def insert(arr):
#     ele = eval(input("Enter element :"))
#     arr.append(ele)
#     print("Element", ele, "is added at the end.")

# def display(arr):
#     if len(arr) == 0:
#         print("Array is empty.")
#     else:
#         print("Elements of the array :")
#         for i in range(0, len(arr)):
#             print("Element at position", i+1, ":", arr[i])

# def bsearch(arr,s):
#     arr.sort()
#     first = 0
#     last = len(arr)-1
#     while(first <= last):
#         mid = int((first + last) / 2)
#         if arr[mid] == s:
#             return mid+1
#         elif s > arr[mid]:
#             first = mid + 1
#         else:
#             last = mid - 1
#     else:
#         return None

# ds = []

# while (True):
#     print()
#     print("1 : Insert an element")
#     print("2 : Display elements")
#     print("3 : Search element")
#     print("0 : Exit")
#     ch = int(input("Enter your choice :"))
    
#     if ch == 1:
#         insert(ds)
        
#     elif ch == 2:
#         display(ds)
    
#     elif ch == 3:
#         s = eval(input("Enter element to search:"))
#         r = bsearch(ds,s)
#         if r == None:
#             print("Element", s, "is not found.")
#         else:
#             print("Element", s, "is found at position", r) 
        
#     elif ch == 0:
#         break
    
#     else:
#         print("Invalid Input.")
        
'''
29
WAP that implements a stack of books using a list.
'''
# def Push(stk,item):
#     stk.append(item)
#     top = len(stk) - 1
    
# def Pop(stk):
#     if stk == []:
#         return 'Underflow'
#     else:
#         item = stk.pop()
#         if len(stk) == 0:
#             top = None
#         else:
#             top = len(stk) - 1
#         return item

# def Peek(stk):
#     if stk == []:
#         return 'Underflow'
#     else:
#         top = len(stk) - 1
#         return stk[top]

# def Display(stk):
#     if stk == []:
#         print('Stack is empty.')
#     else:
#         top = len(stk) -1
#         print('\n',stk[top],'<-- Top')
#         for a in range(top-1, -1, -1):
#             print(stk[a])

# #___main___

# stk = []
# top = None

# while True:
#     print('\nStack Opeartions:')
#     print('1: Push')
#     print('2: Pop')
#     print('3: Peek')
#     print('4: Display')
#     print('0: Exit')
#     ch = int(input('Enter your choice: '))
    
#     if ch == 1:
#         book_id = int(input('Enter book ID: '))
#         book_title = input('Enter Book Name: ')
#         book_author = input('Enter the Author: ')
#         item = [book_id, book_title, book_author]
#         Push(stk, item)
    
#     elif ch == 2:
#         item = Pop(stk)
#         if item == 'Underflow':
#             print('Underflow! Stack is empty.')
#         else:
#             print('Top most item is',item)
            
#     elif ch == 3:
#         item = Peek(stk)
#         if item == 'Underflow':
#             print('Underflow! Stack is empty.')
#         else:
#             print('Top most item is',item)
        
#     elif ch == 4:
#         Display(stk)
        
#     elif ch == 0:
#         break
    
#     else: 
#         print('Invalid Input.')

'''
30
WAP that implements a queue of players using a list.
'''
# def clear():
#     print('\n\n\n')
    
# def isEmpty(Qu):
#     if Qu == []:
#         return True
#     else:
#         return False
    
# def Enqueue(Qu,item):
#     Qu.append(item)
#     # global front, rear
#     if len(Qu) == 1:
#         front = rear = 0
#     else:
#         ren = len(Qu) -1
    
# def Dequeue(Qu):
#     if isEmpty(Qu):
#         return 'Underflow'
#     else:
#         item = Qu.pop(0)
        
#     # global front,rear
#     if len(Qu) == 0:
#         front = rear = None
#     # else:
#         # rear = len(Qu) -1
#     return item

# def Peek(Qu):
#     if isEmpty(Qu):
#         return 'Underflow'
#     else:
#         front = 0
#     return Qu[front]

# def Display(Qu):
#     if isEmpty(Qu):
#         print('Queue is empty!')
#     elif len(Qu) == 1:
#         print(Qu[0],'<-- Front, Rear')
#     else:
#         front = 0
#         rear = len(Qu) -1
#         print(Qu[front],'<--Front')
#         for a in range(1,rear):
#             print(Qu[a])
#         print(Qu[rear],'<--Rear')
        
# #___main___
# queue = []
# front, rear = None, None

# while True:
#     clear()
#     print('\nQUEUE OPERAIONS:')
#     print('1: Enqueue')
#     print('2: Dequeue')
#     print('3: Peek')
#     print('4: Display')
#     print('0: Exit')
#     ch = int(input('Enter your choice: '))
    
#     if ch == 1:
#         pno = int(input('Enter player number: '))
#         pname = input('Enter player name: ')
#         item = [pno, pname]
#         Enqueue(queue, item)
#         input('Press enter to continue...')
    
#     elif ch == 2:
#         item = Dequeue(queue)
#         if item == 'Underflow':
#             print('Underflow! Queue is empty.')
#         else:
#             print('Dequeued item is',item)
#         input('Press enter to continue...')
    
#     elif ch == 3:
#         item = Peek(queue)
#         if item == 'Underflow':
#             print('Underflow! Queue is empty.')
#         else:
#             print('Frontmost item is',item)
#         input('Press enter to continue...')
    
#     elif ch == 4:
#         Display(queue)
#         input('Press enter to continue...')
    
#     elif ch == 0:
#         break
    
#     else:
#         print('Invalid input.')
#         print('Press enter to continue...')
        
'''
34
WAP that intrefaces python with MySQL to read data from 'DRESS' table
of 'EXAM' database.
'''
# import mysql.connector as mysql
# import datetime
# db = mysql.connect(host = 'localhost', user = 'root', \
#                     passwd = 'root', database = 'exam')
# cur = db.cursor()
# qry = 'select * from dress'
# cur.execute(qry)

# s = cur.fetchall()
# print('+-------+----------------+-------+-------+------------+')
# ostr = '|{:^7}|{:^16}|{:^7}|{:^7}|{:^12}|'.format(cur.column_names[0],\
#                                             cur.column_names[1],\
#                                             cur.column_names[2],\
#                                             cur.column_names[3],\
#                                             cur.column_names[4])
# print(ostr)
# print('+-------+----------------+-------+-------+------------+')
# for rec in s:
#     obj = datetime.datetime.strptime(str(rec[4]), '%Y-%m-%d')
#     df = obj.strftime('%Y-%m-%d')
#     ostr = '|{:^7}|{:^16}|{:^7}|{:^7}|{:^12}|'.format(rec[0],\
#                                                         rec[1],\
#                                                         rec[2],
#                                                         rec[3],\
#                                                         df)
#     print(ostr)
# print('+-------+----------------+-------+-------+------------+')
# print(cur.rowcount,'records found.')

'''
35
'''
# import mysql.connector as mysql
# import datetime
# db = mysql.connect(host = 'localhost', user = 'root', \
#                     passwd = 'root', database = 'exam')
# cur = db.cursor()

# qry = 'show tables'
# cur.execute(qry)
# tbl = cur.fetchall()
# print('Available Tables are:')
# for i in range(cur.rowcount):
#     print(i+1, ':', tbl[i][0])
# ch = int(input('Enter your choice: '))
# qry = 'select * from '+tbl[ch-1][0]
# cur.execute(qry)
# noc = len(cur.column_names)
# data = cur.fetchall()
# for rec in data:
#     for c in range(noc):
#         print(cur.column_names[c],':',rec[c])
#     print()
# print(cur.rowcount,'records found.')
# db.close()



'''
36
Write a program that interfaces python with MySQL to execute delete query.
'''

# import mysql.connector as mysql
# #import datetime
# db = mysql.connect(host = 'localhost', user = 'root', \
#                    passwd = 'root', database = 'exam')
# cur = db.cursor()

# try:
#     code = input('Enter mcode to delete: ')
#     qry = f"delete from dress where mcode = '{code}'"
#     cur = db.cursor()
#     cur.execute(qry)
# except Exception as e:
#     print(e)
#     pass
# db.commit()
# db.close()


'''
37
Write a program that interfaces python with MySQL to execute update query.
'''

# import mysql.connector as mysql
# #import datetime
# db = mysql.connect(host = 'localhost', user = 'root', \
#                    passwd = 'root', database = 'exam')
# cur = db.cursor()

# try:
#         dcode = input('Enter Dress code to update: ')
#         qry = 'select * from Dress where dcode = \''+ dcode + '\''
#         cur = db.cursor()
#         cur.execute(qry)
#         data = cur.fetchone()
#         print('Dress code:',data[0])
#         print('Description :',data[1])
#         print('Price:',data[2])
#         print('mcode:',data[3])
#         print('Launchdate:',data[4])
        
#         ncode = input('Enter new Dress Code (press ENTER to keep same: )')
#         if ncode == '':
#             ncode = data[0]
        
#         desc = input('Enter new Description (press ENTER to keep same: )')
#         if desc == '':
#             desc = data[1]
        
#         price = input('Enter new price (press ENTER to keep same: )')
#         if price == '':
#             price = data[2]

#         mcode = input('Enter new mcode (press ENTER to keep same: )')
#         if mcode == '':
#             mcode = data[3]

#         date = input('Enter new launchdate (press ENTER to keep same: )')
#         if date == '':
#             date = data[4]
        
#         qry = f"update dress set dcode = {ncode}, desc = '{desc}',\
#                 price = {price}, mcode = {mcode}, launchdate = {date} where \
#                 dcode = {dcode}"
        
#         cur = db.cursor()
#         cur.execute(qry)
#         print(cur.rowcount, 'records updated.')
# except Exception as e:
#     print(e)
#     pass
# db.commit()
# db.close()



'''
38
Write a menu driven program that performs Create, Insert, Select, Update
and Delete Operations on the table of TCOACH having columns
PCODE(Coach Code), NAME(Coach Name) and ACODE(Activity Code).
'''
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
        
        qry = 'insert into tcoach values({},\'{}\',{})'
        cur = db.cursor()
        cur.execute(qry.format(pcode,name,acode))
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
        ostr = '| {:^6} | {:^15} | {:^5} |'.format(cur.column_names[0],\
                                                    cur.column_names[1],\
                                                    cur.column_names[2])
        print(ostr)
        print('+--------+-----------------+-------+')
        for rec in data:
            ostr = '| {:^6} | {:^15} | {:^5} |'.format(rec[0],\
                                                        rec[1],\
                                                        rec[2])
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
        
        qry = 'update tcoach set pcode = {}, name = \'{}\', acode = {} where \
            pcode = {]'.format(ncode, cname, acode, ccode)
        
        cur = db.cursor()
        cur.execute(qry)
        print(cur.rowcount, 'records updated.')
    except Exception as e:
        # print(e)
        pass
    
def t_del():
    try:
        code = input('Enter Coach code to delete: ')
        qry = 'delete from tcoach where pcode = ' + code
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
