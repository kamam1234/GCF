# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 09:41:41 2022
Accepts string and print vowels and consonants
@author: AMD Ryzen
"""

s = input("Enter a String: ")
print("\nString: ",s)
alpha = vow = 0
for ch in s:
    if ch.isalpha():
        alpha += 1
    if ch.upper() in "AEIOU":
        vow += 1
print("No. of vowels: ",vow)
print("No. of consonants: ",alpha-vow)
print("No. of alphabets: ",alpha)
