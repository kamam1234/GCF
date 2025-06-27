# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 14:54:22 2022

@author: ANKUR (AMD Ryzen)
"""

'''
WAP that accepts a tuple & create another tuple having
cummulative sum of numbers
'''
# tpl = eval(input('Enter a Tuple: '))
# c_tpl = ()
# s = 0
# for ele in tpl:
#     s += ele
#     c_tpl += (s,)
# print('Cummulative Sum Tuple:',c_tpl)

'''
WAP that multiple email addresses from a user and separate usernames
and domain in two different lists.
'''
# n = int(input('How many emails do you want to enter: '))
# e_tup = ()
# for i in range(1,n+1):
#     e = input('Enter email ' + str(i) + ':')
#     e_tup += (e,)
# un = ()
# dom = ()
# for e in e_tup:
#     un_dom = e.partition('@')
#     un += (un_dom[0],)
#     dom += (un_dom[2],)
# print('\nEmail Addresses:')
# for v in e_tup:
#     print(v)
# print('\nUsernames:')
# for v in un:
#     print(v)
# print('\nDomains:')
# for v in dom:
#     print(v)

'''
WAP that accepts a tuple of numbers and generate another 2 tuples
containing the armstrong numbers, prime numbers available in
first tuple.
'''
# t = eval(input('Enter tuples of number: '))
# p = ()
# a = ()
# for v in t:
#     if v != 1:
#         for j in range(2,(v//2)+1):
#             if v % j == 0:
#                 break
#         else:
#             if v not in p:
#                 p += (v,)
#     s = 0
#     i = v
#     while i>0:
#         s += (i%10)**3
#         i = i//10
#     if (v==s) and (v not in a):
#         a += (v,)
# print('Orig. Tuple:',t)
# print('Tuple of Prime no.s:',p)
# print('Tuple of Armstrong:',a)

'''
WAP that accepts a tuple & swap 1st half with 2nd.
'''
# tpl = eval(input('Enter a tuple: '))
# print('\nOrig. tuple:',tpl)
# n = len(tpl)//2
# s_tpl = ()
# if len(tpl)%2 == 0:
#     s_tpl += tpl[n:]
#     s_tpl += tpl[:n]
# else:
#     s_tpl += tpl[n+1:]
#     s_tpl += tpl[n:n+1]
#     s_tpl += tpl[:n+1]
# tpl = s_tpl
# print('New Tuple:',tpl)

'''
WAP that accepts a tuple and rotation factor
and rotate the tuple considering the rotation
factor.
'''
# tpl = eval(input('Enter a tuple: '))
# r = int(input('Enter rotation factor: '))
# l = len(tpl)
# print('\n\nOriginal Tuple:',tpl)
# if r<=l and r>=0:
#     r_tpl = ()
#     r_tpl += tpl[-r:]
#     r_tpl += tpl[:-r]
#     tpl = r_tpl
#     print('Rotated Tuple:',tpl)
# else:
#     print('Invalid rotation factor.')
'''
WAP that accepts a tuple of numbers and generate
another tuple containing the numbers and factorials
of other numbers.
'''
# t = eval(input('Enter a Tuple of numbers:'))
# ft = ()
# tcf = ()
# f = i = 1
# while (f <= max(t)):
#     f *= i
#     i += 1
#     if f in t:
#         ft += (f,)
# print('Tuple of factorials:',ft)

#
# 

# t = eval(input('Enter a Tuple of numbers:'))
# ft = ()
# tcf = ()
# f = i = 1
# while (f <= max(t)):
#     f *= i
#     i += 1
#     ft += (f,)
# for v in t:
#     if (v in ft) and (v not in tcf):
#         tcf += (v,)
# # print('Tuple of factorials:',ft)
# print('Tuple containing factorials:',tcf)

'''
WAP that accepts a number and prints if it is
a factorial of a number or not.
'''
# n = int(input('Enter a number: '))
# j = n
# f = i = 1
# l = []
# while i <= j:
#     f *= i
#     i+=1
#     l += [f]
# print(l)

'''
WAP that accepts matrix in tuples and print the following:
i) 1st & last row of matrix
ii) 1st & last column of matrix
iii)all non-border elements
iv)middle row & middle column
v)Upward Diagonal
vi)Downward diagonal
vii)upper of downward diagonal
viii)Lower of upward diagonal with upward diagonal
'''
# r = int(input('Enter no. of rows: '))
# c = int(input('Enter no. of columns: '))
# mat = ()
r = 6
c = 6
mat = ((11, 12, 13, 14, 15, 16),
       (16, 17, 18, 19, 20, 21),
       (21, 22, 23, 24, 25, 26),
       (26, 27, 28, 29, 30, 31),
       (31, 32, 33, 34, 35, 36),
       (36, 37, 38, 39, 40, 41))

#Transpose

# mat = ((11, 12, 13, 14),
#         (16, 17, 18, 19),
#         (21, 22, 23, 24))
# for i in range(r):
#     row = []
#     for j in range(c):
#         row.append(int(input('Enter Element: ')))
#     mat += tuple(row),
# print(mat)


#####################################################
print('Matrix: ')
for i in range(r):
    for j in range(c):
        print(mat[i][j],end='\t')
    print()

# 1st & last row of matrix

print('\n\n1st & Last row of matrix:')
for i in range(r):
    for j in range(c):
        if i == 0 or i == r-1:
            print(mat[i][j],end='\t')
        else:
            print('--',end='\t')
    print()

# 1st & last column of matrix
print('\n\n1st & Last column of matrix:')
for i in range(r):
    for j in range(c):
        if j == 0 or j == c-1:
            print(mat[i][j],end='\t')
        else:
            print('--',end='\t')
    print()
    
    
# all non-border elements
print('\n\nAll non-border elements:')
for i in range(r):
    for j in range(c):
        if not (j == 0 or j == c-1 or i == 0 or i == r-1):
            print(mat[i][j],end='\t')
        else:
            print('--',end='\t')
    print()



# middle row & middle column

print('\n\nMiddle row & middle column:')
if r % 2 == 0 or c % 2 == 0:
    for i in range(r):
        for j in range(c):
            if j == c/2 or i == r/2 or j == (c/2)-1 or i == (r/2)-1:
                print(mat[i][j],end='\t')
            else:
                print('--',end='\t')
        print()
else:
    for i in range(r):
        for j in range(c):
            if j == (c//2) or i == (r//2):
                print(mat[i][j],end='\t')
            else:
                print('--',end='\t')
        print()
        
# Upward Diagonal
print('\n\nUpward Diagonal:')
if r != c:
    print('Can\'t print upward diagonal.')
else:
    for i in range(r):
        for j in range(c):
            if (i + j) == r-1:
                print(mat[i][j],end='\t')
            else:
                print('--',end='\t')
        print()

# Downward diagonal
print('\n\nDownward Diagonal:')
if r != c:
    print('Can\'t print downward diagonal.')
else:
    for i in range(r):
        for j in range(c):
            if i == j:
                print(mat[i][j],end='\t')
            else:
                print('--',end='\t')
        print()
        
# Upper of downward diagonal
print('\n\nUpper of downward diagonal:')
if r != c:
    print('Can\'t print upward diagonal.')
else:
    for i in range(r):
        for j in range(c):
            if i < j:
                print(mat[i][j],end='\t')
            else:
                print('--',end='\t')
        print()
        
        
# Lower of upward diagonal with upward diagonal
print('\n\nLower of upward diagonal with upward diagonal:')
if r != c:
    print('Can\'t print upward diagonal.')
else:
    for i in range(r):
        for j in range(c):
            if (i + j) == (r-1) or (i + j) > (r-1):
                print(mat[i][j],end='\t')
            else:
                print('--',end='\t')
        print()
        
# Elements one by one
print('\n\nElements one by one:')
for i in range(r):
    for j in range(c):
        if (i+j) % 2 == 0:
            print(mat[i][j],end='\t')
        else:
            print('--',end='\t')
    print()

# Elements one by one of Transpose
print('\n\nElements one by one of Transpose:')
for i in range(r):
    for j in range(c):
        if (i+j) % 2 == 0:
            print(mat[j][i],end='\t')
        else:
            print('--',end='\t')
    print()

# print transpose
print('\n\nTranspose:')
for i in range(c):
    for j in range(r):
        print(mat[j][i],end='\t')
    print()

# print Border elements
print('\n\nBorder elements:')
for i in range(r):
    for j in range(c):
        if i in (0,r-1) or j in (0,c-1):
            print(mat[i][j],end='\t')
        else:
            print('--',end='\t')
    print()

# print Border elements of Transpose
print('\n\nBorder elements of Transpose:')
for i in range(r):
    for j in range(c):
        if i in (0,r-1) or j in (0,c-1):
            print(mat[j][i],end='\t')
        else:
            print('--',end='\t')
    print()