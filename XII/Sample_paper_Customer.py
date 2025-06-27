# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 08:50:03 2023

@author: Ankur (Admin)
"""

'''
A list contains following record of a customer:
[Customer_name, Phone_number, City]
Write the following user defined functions to perform the given operations
on the stack named status:
    i) Push_element(): To push an object containing name and phone number
                       of customers who live in Goa to the stack.
    ii) Pop_element(): To Pop the objects from the stack and display them.
                       Also, display 'Stack Empty' when there are no elements
                       in the stack.
'''

status = []

def Push_element(cust):
    for d in cust:
        if d[2] == 'Goa':
            status.append([d[0],d[1]])
            
def Pop_element():
    while len(status):
        print(status.pop())
    else:
        print('Stack Empty.')
Push_element([])
Pop_element()