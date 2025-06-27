"""
Created on Wed Sep 21 15:30:14 2022

@author: -AMD Ryzen
"""

'''
factorial of number
'''
 n  = int(input("Enter a no.: "))
 fact = 1
 for i in range(1,n+1):
     fact *= i
 print("Factorial of",i,"is",fact)

'''
Factorial upto N
'''

# n  = int(input("Enter a no.: "))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
#     print("Factorial of",i,"is",fact)

'''
print  x raised to y
'''
# x = int(input("Enter Base: "))
# y = int(input("Enter power: "))
# p = 1
# for i in range(1,y+1):
#     p *= x
# print(x, "raised to",y,"is",p)
    
'''
no and print NOD, SOD, reverse, Palin or not
'''
# n = int(input("Enter a Number: "))
# nod = 0
# sod = 0
# rev = 0
# while n > 0:
#     nod +=1
#     sod += (n%10)
#     rev = (rev*10) + (n%10)
#     n = n//10
# print("NOD: ",nod)
# print("SOD: ",sod)
# print("Reverse: ",rev)
# if n== rev:
#     print("Palin.")
# else:
#     print("Not palin.")

'''
factors of number
'''

n = int(input("Enter a Number: "))
print("Factors of",n,"are ",end="")
for i in range(1,(n//2)+1):
    if (n%i)==0:
        print(i,end=" ")
print(n)