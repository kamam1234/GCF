# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 09:38:04 2023


____________________________________SORTING____________________________________


@author: Ankur (Admin)
"""

'''
Bubble Sorting
'''
# lst = eval(input('Enter a list: '))
# print('\nOrg.List: ',lst)
# n = len(lst)

# for i in range(n):
#     print(i)
#     for j in range(0,n-i-1):
#         if lst[j] > lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
#             print(lst)
# print()
# print()

# print('Sorted list:',lst)


'''
Insertion Sort
'''
# lst = eval(input('Enter a list: '))
# print('\nOrg.List:',lst)
# n = len(lst)
# for i in range(1,n):
#     v = lst[i]
#     j = i - 1
#     while j >= 0 and v < lst[j]:
#         lst[j+1] = lst[j]
#         j -= 1
#     else:
#         lst[j+1] = v
# print('Sorted List:',lst)