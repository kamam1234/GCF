# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:39:14 2023

@author: Ankur (Admin)
"""

'''
An nlist is containnihg data of employees in following format:
    [EmpNo, EName, Job, Sal]
Using records of employee, Create following functions:
    1) AddEmp : This should insert Employee Name and Job of
       Such employees of clerks and managers who are having
       sal >= 1500 to a stack named 'StkEmp'
    2) Pop : This should pop and display the elements of stack
       and when stack becomes empty should display message
       'Stack is Empty.'
'''
nlist = [[101,'AAA','Manager',2500],
         [102,'BBB','Salesman',2000],
         [103,'CCC','Clerk',1200],
         [104,'DDD','Manager',1250],
         [105,'EEE','Clerk',1800]]

stkemp = []

def AddEmp(nlist):
    for i in nlist:
        if (i[2].upper() in ['CLERK','MANAGER']) and i[3] >= 1500:
            stkemp.append([i[1],i[2]])
            
def pop():
    while len(stkemp):
        print(stkemp.pop())
        
    else:
        print('Stack is Empty.')
        
AddEmp(nlist)
print(stkemp)
print('\n\n\n')
pop()