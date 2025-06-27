# # -*- coding: utf-8 -*-
# """
# Created on Sat Sep  3 18:44:20 2022
# 1
# 12
# 123
# 1234
# 12345
# @author: AMD Ryzen
# """
# Pattern 1
n = int(input("Enter no. of lines: "))
for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        print(j,end="")
print()


# '''
# *
# **
# ***
# ****
# *****
# '''
# # Pattern 2
# n = int(input("Enter no. of lines: "))
# for i in range(1,n+1):
#     print()
#     for j in range(1,i+1):
#         print("*",end="")
        

# '''
# 1)ABC de FGh ij KLM no PQR st UVW xy Z

# 3)A B c D E
#    f G H i
#     J K l
#      M N
#       o
# '''
# print()
# for i in range(1,27):
#     if i % 5 == 0:
#         print(chr(i+96),end=" ")
#     if i % 5 == 1:
#         print(chr(i+64),end="")
#     if i % 5 == 2:
#         print(chr(i+64),end="")
#     if i % 5 == 3:
#         print(chr(i+64),end=" ")
#     if i % 5 == 4:
#         print(chr(i+96),end="")

'''
2)a B c D e
  B c D e
  c D e
  D e
  e
'''
print()
n = int(input("Enter n: "))
for i in range(n,0,-1):
    print()
    for j in range(i,0,-1):
        if i%2==0:
            print(chr(j+64),end=" ")
        else:
                print(chr(j+96),end=" ")
