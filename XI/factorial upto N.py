# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 18:40:21 2022
Factorial upto n
@author: AMD Ryzen
"""

n = int(input("Enter n to print factorial upto n: "))
fact = 1
for i in range(1,n+1):
    fact *= i
    print("Fact. of",i,"is",fact)