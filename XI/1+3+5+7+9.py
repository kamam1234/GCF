# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:50:05 2022
1+3+5+7+9
@author: AMD Ryzen
"""
print("Sum of ",end=" ")
tot = 0
for i in range(1,11,2):
    print(i, end=" ")
    tot += i
print("=",tot)