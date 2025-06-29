# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 12:59:44 2022

@author: AMD Ryzen
"""

def is_palindrome(s: str) -> bool:

    s = "".join([character for character in s.lower() if character.isalnum()])
    return s == s[::-1]


if __name__ == "__main__":
    s = input("Enter string to determine whether its palindrome or not: ").strip()
    if is_palindrome(s):
        print("Given string is palindrome")
    else:
        print("Given string is not palindrome")