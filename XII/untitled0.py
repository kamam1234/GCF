# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:12:26 2023

@author: ANKUR
"""
import pickle

def append():
    f = open(r'c:\dfh\stu_recl.dat','wb+')
    while True:
        roll = int(input('\nEnter Roll No.: '))
        name = input('Enter Name: ')
        marks = float(input('Enter Marks: '))        
        data = [roll,name,marks]
        pickle.dump(f,data)
        ch = input('\nDo you want to enter more records: ')
        if ch.upper() in 'N':
            break
    f.close()

def read():
    f = open(r'c:\dfh\stu_recl.dat','rb')
    o = '{:1}{:^8}{:1}{:^15}{:1}{:^7}{:1}'
    print('+--------+---------------+-------+')
    print(o.format('|','Roll No.','|','Name','|','Marks','|'))
    print('+--------+---------------+-------+')
    rec = 0
    while True:
        try:
            data = pickle.load(f)
            rec += 1
            o = '{:1}{:^8}{:1}{:^15}{:1}{:^7.2f}{:1}'
            print(o.format('|',data[0],'|',data[1],'|',data[2],'|'))
        except EOFError:
            o = '{:1}{:^8}{:1}{:^15}{:1}{:^8}{:1}'
            print('+--------+---------------+-------+')
            if rec == 1:
                print(1,'row in set.')
            else:
                print(rec,'rows in set.')
            break
    f.close()
read()