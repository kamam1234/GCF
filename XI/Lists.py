# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 18:39:54 2022

====================='''''''LISTS''''''========================================

@author: AMD Ryzen Ankur
"""

'''
40WAP that accepts a lists from a user and print
sum of all even and odd values.
Also print sum of even and odd positioned values.
'''
# lst = eval(input("enter a list: "))
# se = so = sep = sop = 0
# for i in range(len(lst)):
#     if (lst[i] % 2) == 0:
#         se += lst[i]
#     else:
#         so += lst[i]
#     if i%2 == 0:
#         sop += lst[i]
#     else:
#         sep += lst[i]
# print('\nSum of even values: ',se)
# print('Sum of odd values: ',so)
# print('Sum of even positioned values: ',sep)
# print('Sum of odd positioned values: ',sop)

'''
41WAP that accepts 2 lists from user and print
if lists are overlapped or separated.
'''
# l1 = eval(input("enter 1st list: "))
# l2 = eval(input("enter 2nd list: "))
# for v in l1:
#     if v in l2:
#         print('Lists are overlapped.')
#         break
# else:
#     print('Lists are separated.')

'''
42WAP that accepts a list and swap each odd
positioned element with even positioned element
'''
# l = eval(input('enter a list: '))
# print('\n\nList before swapping: ', l)
# for i in range(1,len(l),2):
#     l[i],l[i-1] = l[i-1],l[i]
# print('List after swapping: ',l)

'''
43WAP that accepts a list from user and swap
the first half with the other half.
'''
# lst = eval(input('enter a list: '))
# print('List before Swapping:',lst)
# l = len(lst)
# if l % 2 == 0:
#     lst[:l//2],lst[l//2:]=lst[l//2:],lst[:l//2]
# else:
#     lst[:(l//2)], lst[(l//2)+1:] = lst[(l//2)+1:], lst[:(l//2)]
# print('Swapped list: ',lst)

'''
44WAP that accepts a list and rotation factor
and rotate the 
list considering the rotation factor.
'''
# lst = eval(input('enter a list: '))
# r = int(input('enter rotation factor: '))
# print('\nOriginal List: ',lst)
# if r>=0 and r<=len(lst):
#     r_lst = []
#     r_lst += lst[-r:]
#     r_lst += lst[:-r]
#     lst = r_lst
#     print('Rotated list: ',lst)
# else:
#     print('Invalid Rotation factor')

'''
45WAP that accepts a list and print unique &
repeated elements of list.
Also print the frequency of all elements.
'''
# lst = eval(input('enter a list: '))
# un = []
# du = []
# for ele in lst:
#     if ele not in du:
#         cnt = lst.count(ele)
#         print("Frequency of '",ele,"' is ",cnt,sep='')
#         if cnt == 1:
#             un.append(ele)
#         else:
#             du.append(ele)
# print('\nOriginal list:',lst)
# print('List of Unique elements:',un)
# print('List of Duplicate elements:',du)

'''
46WAP that accepts a list and print mean, median,
mode and range of the list.
'''
# lst = eval(input('enter a list: '))
# n = len(lst)
# mean = sum(lst)/n
# srt = sorted(lst)
# mid = n//2
# if n%2 == 0:
#     median = (srt[mid]+srt[mid-1])/2
# else:
#     median = srt[mid]
# mfreq = 0
# for ele in lst:
#     freq = lst.count(ele)
#     if freq > mfreq:
#         mfreq = freq
# mode = []
# for ele in lst:
#     if lst.count(ele) == mfreq and ele not in mode:
#         mode.append(ele)
# rng = max(lst) - min(lst)
# print('\nMean:',mean)
# print('Median:',median)
# print('Mode:',mode,'with frequency of',mfreq)
# print('Range:',rng)

'''
WAP that accepts a list & sort list in ascending and
descending order.
'''
# x = eval(input('enter a list: '))
# ax = list(x)
# ax.sort()
# dx = sorted(x,reverse = True)
# print('\nOriginal list:',x)
# print('Sorted list in asc order: ',ax)
# print('Sorted list in desc order: ',dx)

'''
WAP that performs following menu driven operations on list
1: Insert @ beginning
2: Insert between
3: Insert @ end
4: Delete from beginning
5: Delete from between
6: Delete from end
7: Delete by value
8: Clear list
9: View list
'''
# lst = []
# ch = 1
# while ch != 0:
#     print('\n\n')
#     print('1:Insert @ beginning')
#     print('2:Insert between')
#     print('3:Insert @ end')
#     print('4:Delete from beginning')
#     print('5:Delete from between')
#     print('6:Delete from end')
#     print('7:Delete by value')
#     print('8:Clear list')
#     print('9:View list')
#     print('0:exit')
#     ch = int(input('\nenter your Choice: '))
#     if ch == 1:
#         v = int(input('enter a Value: '))
#         lst.insert(0,v)
#         print('Value inserted.')
#     elif ch == 2:
#         p = int(input('enter Position: '))
#         if p>0 and p<= len(lst)+1:
#             v = int(input('enter value: '))
#             lst.insert(p-1, v)
#             print('Value inserted.')
#         else:
#             print('Invalid position.')
#     elif ch == 3:
#         v = int(input('enter a value: '))
#         lst.append(v)
#         print('Value inserted.')
#     elif ch == 4:
#         if len(lst) == 0:
#             print('List is empty.')
#         else:
#             print('Value',lst[0],'deleted')
#             lst.pop(0)
#     elif ch == 5:
#         if len(lst) == 0:
#             print('List is empty.')
#         else:
#             p = int(input('enter Position: '))
#             if p>0 and p<=len(lst):
#                 print('Value',lst[p-1],'deleted.')
#                 lst.pop(p-1)
#             else:
#                 print('Invalid Postion')
#     elif ch == 6:
#         if len(lst) == 0:
#             print('List is empty.')
#         else:
#             print('Value',lst[-1],'deleted.')
#             lst.pop()
#     elif ch == 7:
#         if len(lst) == 0:
#             print('List is empty.')
#         else:
#             v = int(input('enter Value: '))
#             i = d = f = 0
#             while i<len(lst):
#                 if lst[i] == v:
#                     print(v,'is found at',i+1)
#                     f += 1
#                     ch = int(input('Are you sure [Yes / No]?'))
#                     if ch in 'YyYesYeSyes':
#                         lst.pop(i)
#                         i -= 1
#                         d += 1
#                     i += 1
#                 if f == 0:
#                     print('Value not found in list.')
#                 print(d,'values deleted.')
#     elif ch == 8:
#         lst.clear()
#         print('List is cleared.')
#     elif ch == 9:
#         print('List:',lst)
#     elif ch == 0:
#         print('Thank You.')
#     else:
#         print('Invalid Input.')
#     input('Press "enter" to continue...')

'''
WAP that accepts two lists and merge them element by element
'''
# lst1 = eval(input('enter 1st list: '))
# lst2 = eval(input('enter 2nd list: '))
# l1 = len(lst1)
# l2 = len(lst2)
# ml = []

# for i in range(min(l1,l2)):
#     ml.append(lst1[i])
#     ml.append(lst2[i])
# if l1<l2:
#     ml += lst2[l1:]
# else:
#     ml += lst1[l2:]
# print(ml)

'''
47WAP that accepts a list containing several 0s &
shift all 0 to the right side of the list:
'''
# l = eval(input('enter a list: '))
# print('\nentered List:',l)
# cnt = l.count(0)
# for i in range(cnt):
#     l.remove(0)
# l = l + ([0]*cnt)
# print('Updated list: ',l)

'''
48WAP that accepts a list and make it a non duplicated list
'''
# lst = eval(input('enter a list: '))
# print('\nOriginal List: ',lst)
# lstnd = []
# for v in lst:
#     if v not in lstnd:
#         lstnd.append(v)
# lst = lstnd
# print('Updated list: ',lst)

'''
49WAP that accepts a list of fibonacci series using
a list upto N
'''
# n = int(input('enter N: '))
# if n == 1:
#     print([0])
# else:
#     l = [0,1]
#     for i in range(2,n):
#         v = l[i-1] + l[i-2]
#         l.append(v)
#     print('\n',l)

'''
50WAP that accepts two lists and find the difference of
elements index
'''
# ls1 = eval(input('enter 1st list:'))
# ls2 = eval(input('enter 2nd list:'))
# if ls1 == ls2:
#     print('Both the lists are same.')
# else:
#     l1 = len(ls1)
#     l2 = len(ls2)
#     for i in range(min(l1,l2)):
#         if ls1[i] != ls2[i]:
#             print('Difference found at position',i+1)
#             break
#     else:
#         print('Difference found at position',i+2)

'''
51WAP that accepts 2 matrices and find the sum of those 2 matrices
'''
# r = int(input('enter no. of rows: '))
# c = int(input('enter no. of columns: '))
# print('\nEnter values for 1st Matrix.')
# m1 = []
# for i in range(r):
#     m1.append([])
#     for j in range(c):
#         m1[i].append(int(input('enter Value: ')))
# print('\nenter values for 2nd Matrix.')
# m2 = []
# for i in range(r):
#     m2.append([])
#     for j in range(c):
#         m2[i].append(int(input('enter Value: ')))
# sm = []
# for i in range(r):
#     sm.append([])
#     for j in range(c):
#         sm[i].append(m1[i][j] + m2[i][j])

# print('\nMatrix 1:')
# for i in range(r):
#     for j in range(c):
#         print(m1[i][j],end='\t')
#     print()

# print('\nMatrix 2:')
# for i in range(r):
#     for j in range(c):
#         print(m2[i][j],end='\t')
#     print()
# print('\nSum of Matrices:')
# for i in range(r):
#     for j in range(c):
#         print(sm[i][j],end='\t')
#     print()

'''
52WAP that accepts 2 matrices & produces the product of
those matrices
Columns of 1st matrix must be equal to
the rows of the second matrix. (Neccessary Condition)
'''
# m1 = []
# m2 = []
# mp = []
# r1 = int(input('enter rows of 1st matrix: '))
# c1 = int(input('enter columns of 1st matrix: '))
# r2 = int(input('enter rows of 2nd matrix: '))
# c2 = int(input('enter columns of 2nd matrix: '))
# if c1 == r2:
#     print('\nEnter values in 1st matrix:')
#     for i in range(r1):
#         m1.append([])
#         for j in range(c1):
#             m1[i].append(int(input('Enter Value: ')))
#     print('\nEnter values in 2nd matrix:')
#     for i in range(r2):
#         m2.append([])
#         for j in range(c2):
#             m2[i].append(int(input('Enter Value: ')))
#     mp = []
#     rp = r1
#     cp = c2
#     for i in range(rp):
#         mp.append([])
#         for j in range(cp):
# mp[i].append(0)
# for k in range(c1):
#                 mp[i][j] += (m1[i][k] * m2[k][j])
#     print('\nMatrix 1:')
#     for i in range(r1):
#         for j in range(c1):
#             print(m1[i][j],end='\t')
#         print()
#     print('\nMatrix 2:')
#     for i in range(r2):
#         for j in range(c2):
#             print(m2[i][j],end='\t')
#         print()
#     print('\nProduct of Matrices:')
#     for i in range(rp):
#         for j in range(cp):
#             print(mp[i][j],end='\t')
#         print()
# else:
#     print('Product is not possible.')


# =============================================================================
# #############################################################################
# =============================================================================
'''
Practice
'''


'''sep or overlapped'''

# l1 = eval(input('enter 1st list: '))
# l2 = eval(input('enter 2nd list: '))
# for v in l1:
#     if v in l2:
#         print('Lists are overlapped.')
#         break
# else:
#     print('List are separated.')

'''print sov, sev, sopv, sepv of list'''
# lst = eval(input('enter a list: '))
# so = se = sop = sep = 0
# for i in range(len(lst)):
#     if i % 2 == 0:
#         sop += lst[i]
#     else:
#         sep += lst[i]
#     if lst[i] % 2 == 0:
#         se += lst[i]
#     else:
#         so += lst[i]
# print('SO:',so)
# print('Se:',se)
# print('SOP:',sop)
# print('SeP:',sep)

'''WAP that accepts a list and make it a non duplicated list'''
# lst = eval(input('enter a list: '))
# nd = []
# for v in lst:
#     if v not in nd:
#         nd.append(v)
# lst = nd
# print('Non-duplicated list:',nd)

'''Accept a list and rotate the list considering the rotation factor'''
# lst = eval(input('enter a list: '))
# r = int(input('enter Rotation Factor: '))
# if (r>0) and (r < len(lst)):
#     nl = []
#     nl += lst[-r:]
#     nl += lst[:-r]
#     lst = nl
#     print(nl)
# else:
#     print('Invalid rotation factor.')

'''Accept n & Print fibonacci series upto n'''
# n = int(input('Enter n: '))
# if n == 1:
#     print([0])
# else:
#     l = [0,1]
#     for i in range(2,n):
#         v = l[i-1] + l[i-2]
#         l.append(v)
#     print(l)

'''Shift 0's to right'''
# lst = eval(input('Enter a list containing 0\'s: '))
# cnt = lst.count(0)
# for i in range(cnt):
#     lst.remove(0)
#     lst += [0]
# print(lst)

'''WAP that accepts a list and print unique &
repeated elements of list.
Also print the frequency of all elements.'''
# lst = eval(input('Enter a list: '))
# nd = un = du = []
# for v in lst:
#     if v not in nd:
#         cnt =lst.count(v)
#         print('Frequency of',v,'is:',cnt)
#         if cnt == 1:
#             un.append(v)
#         else:
#             du.append(v)
# print(un)
# print(du)

'''WAP that accepts a list & sort list in ascending and
descending order'''
x = eval(input('Enter a list:'))
ax = list(x)
ax.sort()
dx = sorted(x,reverse = True)     #"""it's reverse not reversed"""
print(ax)
print(dx)