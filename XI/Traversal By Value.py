"""
Created on Fri Aug 26 18:41:15 2022
Traversal By Value

@author: AMD Ryzen
"""

s = "India"
print("Traversal By Value")
print()
for ch in s:
    print(ch,end='')

print("\n\nForward traversal with forward index:")
for i in range(len(s)):
    print("Character",s[i],"is at",i)

print("\n\nForward traversal with backward index:")
for i in range(-len(s),0):
    print("Character",s[i],"is at",i)
    
print("\n\nBackward traversal with forward index:")
for i in range(-1,-len(s)-1,-1):
    print("Character",s[i],"is at",i)
    
print("\n\nBackward traversal with Forward index:")
for i in range(len(s)-1,-1,-1):
    print("Character",s[i],"is at",i)