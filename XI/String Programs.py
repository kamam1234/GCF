# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 18:49:25 2022
String Programs
@author: AMD Ryzen
"""
# -*- coding: ascii -*-
'''
String Traversal through forward and backward index by
forwardand backward index:
'''
# s = input("Enter a string: ")
# print("\nForward traversal with forward index:")
# for i in range(len(s)):
#     print(s[i], end=" ")
# print("\nForward traversal with backward index:")
# for i in range(-len(s),0):
#     print(s[i], end=" ")
# print("\nBackward traversal with forward index:")
# for i in range(len(s)-1,-1,-1):
#     print(s[i], end=" ")
# print("\nBackward traversal with backward index:")
# for i in range(-1,-len(s)-1,-1):
#     print(s[i], end=" ")


'''
String Stats.
'''
# s = input("Enter a string: ")
# up = low = dig = spa = sp = 0
# for i in range(len(s)):
#     if s[i].isupper():
#         up +=1
#     elif s[i].islower():
#         low += 1
#     elif s[i].isspace():
#         spa += 1
#     elif s[i].isdigit():
#         dig +=1 
#     else:
#         sp +=1

# print("String: ",s)
# print("upper: ",up)
# print("Lower: ",low)
# print("Alphabets: ",up+low)
# print("Spaces: ",spa-1,-len(s)-1,-1)
# print("Digits: ",dig)
# print("Sp. char: ",sp)
# print("Total Char.: ",len(s))

'''
Accept string and print total no of vowels and consonants
'''
# s = input("Enter a String: ")
# alpha = vow = 0
# for ch in s:
#     if ch.isalpha():
#         alpha +=1
#     if ch in "aeiouAEIOU":
#         vow +=1
# print("Vowels: ",vow)
# print("Consonants: ",alpha-vow)
# print("Alphabets: ",alpha)
    
'''
Enter String and check occurence of char in string along
 with position
'''
# s = input("Enter a String: ")
# ch = input("Enter a character: ")
# f = 0
# for i in range(len(s)):
#     if s[i].upper() == ch.upper():
#         f+=1
#         print(i,end=" ")
# print("\nCharacter '",ch,"' is found ",f," times.",sep="")

'''
String is palin or not
'''
s = input("Enter String: ")            #slicing method
if s.upper() == s[::-1].upper():
    print("String is palin.")
else:
    print("String is not palin.")

'''
Accept string and print in reverse order and reverse case
'''



'''
Strong password
8 char, upper, lower, digit, sp char
'''


'''
Accept string and print every alternate char in upper and
lower case
'''