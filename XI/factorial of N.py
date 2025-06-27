# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:03:47 2022
factorial of N
@author: AMD Ryzen
"""

n = int(input("Enter n to print its factorial: "))
f = 1
for i in range(n,0,-1):
    f *= i
print("Factorial of", n, "is" ,f)