# # -*- coding: utf-8 -*-
# """
# Created on Mon Sep 11 15:30:58 2023

# @author: Ankur (Admin)
# """

# '''
# Structure:
#     Product ID, Product Name, Quantity, Rate
# Functions:
#     1 Add records along with title
#     2 count & display products having order amt more than 1000
#       (order amt = quantity * rate)
# '''

# import csv

# def write():
#     f = open('Pro_Details.csv','a',newline='')
#     s = csv.writer(f)
#     p = f.tell()
#     if p == 0:
#         s.writerow(['Product ID','Name','Quantity','Rate'])
#     while True:
#         pid = int(input('\nEnter Product ID: '))
#         name = input('Enter Product Name: ')
#         qua = int(input('Enter the Quantity: '))
#         rate = float(input('Enter Rate: '))
#         d = [pid, name, qua, rate]
#         s.writerow(d)
#         ch = input('Do you want to enter more records: ')
#         if ch.upper() in 'N':
#             break
        
        
#     f.close()

# def read():
#     f = open('Pro_Details.csv','r')

#     rec = 0
#     print('+----------+----------+--------+--------+')
#     d = csv.reader(f)
#     o = '{:1}{:^10}{:1}{:^10}{:1}{:^8}{:1}{:^8}{:1}'
#     cnt = 0
#     for i in d:
#         cnt += 1
#         if cnt == 1:
#             # print(i)
#             print(o.format('|',i[0],'|',i[1],'|',i[2],'|',i[3],'|'))
#             print('+----------+----------+--------+--------+')
#         else:
#             # print(i)
#             rec += 1
#             print(o.format('|',i[0],'|',i[1],'|',i[2],'|',i[3],'|'))
#     print('+----------+----------+--------+--------+')
#     print(rec,'records found.')
        
#     f.close()

# def src():
#     f = open('Pro_Details.csv','r')

#     rec = 0
#     print('+----------+----------+--------+--------+----------+')
#     d = csv.reader(f)
#     o = '{:1}{:^10}{:1}{:^10}{:1}{:^8}{:1}{:^8}{:1}{:^10}{:1}'
#     cnt = 0
#     for i in d:
#         cnt += 1
#         if cnt == 1:
#             # print(i)
#             print(o.format('|',i[0],'|',i[1],'|',i[2],'|',i[3],\
#                            '|','Order Amt.','|'))
#             print('+----------+----------+--------+--------+----------+')
#         else:
#             # print(i)
#             if (float(i[2])*float(i[3])) >= 1000:
#                 rec += 1
#                 print(o.format('|',i[0],'|',i[1],'|',i[2],'|',i[3],'|',\
#                                float(i[2])*float(i[3]),'|'))
#     print('+----------+----------+--------+--------+----------+')
#     print(rec,'records found.')
        
#     f.close()
    
# while True:
#     print('\n\nChoose from the following options:')
#     print('1: Write records in a file.')
#     print('2: Read records from file')
#     print('3: Display records where Order Amt >= 1000.')
#     print('0: Exit.')
#     ch = int(input('\nEnter your choice: '))
    
#     if ch == 1:
#         write()
        
#     elif ch == 2:
#         read()
        
#     elif ch == 3:
#         src()
        
#     elif ch == 0:
#         break
    
#     else:
#         print('Invalid input!')
#     input('Press ENTER to continue...')






