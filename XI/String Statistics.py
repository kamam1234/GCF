# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 19:25:18 2022
String statistics
@author: AMD Ryzen
"""

s = input("Enter a string: ")
l = len(s)

up = low = dig = space = sp = 0

for i in range(0,l):
    if s[i].isupper():
        up += 1
    elif s[i].islower():
        low += 1
    elif s[i].isdigit():
        dig += 1
    elif s[i].isspace():
        space += 1
    else:
        sp += 1

print("Upper: ",up)
print("Lower: ",low)
print("Alphabets: ",up+low)
print("Digits: ",dig)
print("Space: ",space)
print("Special char.: ",sp)
print("Total char.: ",l)

# upper
# lower
# total alpha
# digits
# space
# special
# total