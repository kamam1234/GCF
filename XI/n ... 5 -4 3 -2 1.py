# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:55:48 2022
n ... 5 -4 3 -2 1 
@author: AMD Ryzen
"""

n = int(input("Enter N: "))
for i in range(n,0,-1):
    if i%2 == 0:
        print(-i,end="  ")
    else:
        print(i,end=" ")
