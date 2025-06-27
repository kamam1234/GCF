# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:53:54 2022

@author: AMD Ryzen
"""

# '''
# WAP that prints first N numbers whose squares are palin.
# '''
# n = int(input("Enter a number: "))
# print("No.s whose squares are palin are:")

# for k in range(1, (n)+1):
#     j = k * k
#     i = k * k
#     rev = 0
#     while j>0:
#         rev = (rev*10) + (j%10)
#         j = j//10
#     if rev == i:
#         print("Square of ",k," is ",i,". Rev: ",rev,sep="")


# '''
# A B C D E
#  F G H I
#   J K L
#    M N
#     O
# '''
# print()
# n = 5
# c = 1
# k = 1
# for i in range(n,0,-1):
#     for j in range(n,i,-1):
#         print(end="")
#     for j in range(1,i+1):
#         print(chr(c+64),end=" ")
#         c+=1
#     print()


# '''
# WAP that accepts a string and a char. and check the 
# occurences of enterd char along with positions (ignore case).
# '''
# s = input("\nEnter a string: ")
# ch = input("Enter a char. to check its occurence: ")
# k = ch
# print("Character found at positon(s):",end="")
# for i in range(len(s)):
#     if k.upper() == s[i].upper():
#         print(i + 1,end=" ")
# print()


