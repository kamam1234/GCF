# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:20:50 2023

@author: Ankur (Admin)
"""

'''
WAP that implemments linear search using function.  #LINEAR
'''
def insert(arr):
    roll = int(input("Enter roll :"))
    name = input("Enter name :")
    
    ele = [roll, name]

    arr.append(ele)
    print("Element", ele, "is added at the end.")

def display(arr):
    if len(arr) == 0:
        print("Array is empty.")
    else:
        print("Elements of the array :")
        for i in range(0, len(arr)):
            print("Element at position", i+1, ":", arr[i])

def lsearch(arr,sname):
    for i in range(0, len(arr)):
        if arr[i][1] == sname:
            return arr[i], i+1
    
    return None, None

ds = []

while (True):
    print("\n\n")
    print("1 : Insert an element")
    print("2 : Display elements")
    print("3 : Search element")
    print("0 : Exit")
    ch = int(input("Enter your choice :"))
    
    if ch == 1:
        insert(ds)
        
    elif ch == 2:
        display(ds)
    
    elif ch == 3:
        sname = input("Enter name to search:")
        r, p = lsearch(ds,sname)
        if p == None:
            print("Name", sname, "is not found.")
        else:
            print("Record", r, "is found at position", p) 
        
    elif ch == 0:
        break
    
    else:
        print("Invalid Input.")

'''
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
#     input('Press ENTER to continue...')
    

'''
WAP that implements a queue of players using a list.
'''
def isEmpty(Qu):
    if Qu == []:
        return True
    else:
        return False
    
def Enqueue(Qu,item):
    Qu.append(item)
    # global front, rear
    if len(Qu) == 1:
        front = rear = 0
    else:
        ren = len(Qu) -1
    
def Dequeue(Qu):
    if isEmpty(Qu):
        return 'Underflow'
    else:
        item = Qu.pop(0)
        
    # global front,rear
    if len(Qu) == 0:
        front = rear = None
    # else:
        # rear = len(Qu) -1
    return item

def Peek(Qu):
    if isEmpty(Qu):
        return 'Underflow'
    else:
        front = 0
    return Qu[front]

def Display(Qu):
    if isEmpty(Qu):
        print('Queue is empty!')
    elif len(Qu) == 1:
        print(Qu[0],'<-- Front, Rear')
    else:
        front = 0
        rear = len(Qu) -1
        print(Qu[front],'<== Front')
        for a in range(1,rear):
            print(Qu[a])
        print(Qu[rear],'<== Rear')
        
#___main___
queue = [[1, 'sds'],
[2, 'sdsd'],
[3, 'dsw'],
[4, 'wdc'],
[5, 'wed'],
[6, 'wdwe']]
front, rear = None, None

while True:
    # %clear
    print('\nQUEUE OPERAIONS:')
    print('1: Enqueue')
    print('2: Dequeue')
    print('3: Peek')
    print('4: Display')
    print('0: Exit')
    ch = int(input('Enter your choice: '))
    
    if ch == 1:
        pno = int(input('Enter player number: '))
        pname = input('Enter player name: ')
        item = [pno, pname]
        Enqueue(queue, item)
    
    elif ch == 2:
        item = Dequeue(queue)
        if item == 'Underflow':
            print('Underflow! Queue is empty.')
        else:
            print('Dequeued item is',item)
    
    elif ch == 3:
        item = Peek(queue)
        if item == 'Underflow':
            print('Underflow! Queue is empty.')
        else:
            print('Frontmost item is',item)
    
    elif ch == 4:
        Display(queue)
    
    elif ch == 0:
        break
    
    else:
        print('Invalid input.')
    input('Press enter to continue...')
    
    