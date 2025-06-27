# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 09:52:10 2023

@author: ANKUR MACWAN(ADMIN)

"""

'''
Q1 WAP that accepts two strings & check if it is a
prefix of another or not.
'''
s1 = input('Enter 1st string: ')
s2 = input('Enter 2nd String: ')
l1 = len(s1)
l2 = len(s2)
if (s1.upper() == s2.upper()) or (s1 == s2):
    print('\nBoth the strings are same.')
elif l1 < l2:
    if s1.lower() == s2[:l1].lower():
        print("\n\'",s1,"\' is a prefix of \'",s2,
              "\'",sep='')
elif l1 > l2:
    if s2.lower() == s1[:l2].lower():
        print("\n\'",s2,"\' is a prefix of \'",s1,
              "\'",sep='')
else:
    print('\nNeither string is a prefix of other.')
        
'''
Q2 WAP that accepts a list containing several 0's and shift all
the 0's to the left side of the list
'''
lst = eval(input('Enter a list containing several 0\'s: '))
cnt = lst.count(0)
print('\n\n\nEntered list:',lst)
for i in range(cnt):
    lst.remove(0)
lst = ([0]*cnt)+lst
print('Updated list:',lst)