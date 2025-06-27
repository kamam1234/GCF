# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:05:54 2023

@author: HP
"""
import pickle as p
def srcmarks():
    try:
        f = open(r'c:\dfh\stu_recl.dat','rb')
    except IOError:
        print('File not found.')
        return
    src = []
    
    print('+--------+---------------+-------+')
    try:
        obj = '{:1}{:^8}{:1}{:^15}{:1}{:^7}{:1}'
        print(obj.format('|','Roll No.','|','Name','|','Marks','|'))
        print('+--------+---------------+-------+')
        rec = 0
        while True:
            data = p.load(f)
            rec += 1
            src.append([data[2],data[1],data[0]])
            src.sort()
        # for i in src:
        #     obj = '{:1}{:^8}{:1}{:^15}{:1}{:^7.2f}{:1}'
        #     print(obj.format('|',src[i][2],'|',src[i][1],'|',src[i][0],'|'))
        print(src)
    except EOFError:
        print('+--------+---------------+-------+')
        print(rec,'record(s) found')
    f.close()


def read():
    try:
        f = open(r'c:\dfh\stu_recl.dat','rb')
    except IOError:
        print('\nFile not found.')
        return
    
    print('\n+--------+---------------+-------+')
    try:
        obj = '{:1}{:^8}{:1}{:^15}{:1}{:^7}{:1}'
        print(obj.format('|','Roll No.','|','Name','|','Marks','|'))
        print('+--------+---------------+-------+')
        rec = 0
        while True:
            data = p.load(f)
            rec += 1
            obj = '{:1}{:^8}{:1}{:^15}{:1}{:^7.2f}{:1}'
            print(obj.format('|',data[0],'|',data[1],'|',data[2],'|'))
    except EOFError:
        print('+--------+---------------+-------+')
        print(rec,'record(s) found.')
    f.close()
read()
# srcmarks()