# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 12:15:05 2023
XII : CH - 3 -- Functions
@author: Ankur (Admin)
"""

'''
Q1
Create a function cube() that accepts two arguments as integers and
returns cube of these numbers and even or odd if the sum is even or odd
respectively.
WAP that finds the sum of cube of any two numbers and also print if the
sum is even or odd.
'''

# def cube(v1,v2):
#     ans = (v1**3) + (v2**3)
#     if ans%2 == 0:
#         return v1**3, v2**3, 'even'
#     else:
#         return v1**3, v2**3, 'odd'

# n1 = int(input('Enter 1st number: '))
# n2 = int(input('Enter 2nd number: '))
# c = cube(n1,n2)
# print(c[0]+c[1],' is the sum of cube of ',n1,':',c[0],\
#       ' and ',n2,':',c[1],' which is ',c[2],sep='')


'''
Q2
Create a function isprime() that accepts an integer as argument and
return if supplied number is prime; otherwise false.
Using above function, make a program that prints prime no.s between
2 & N (given by user)
'''

def isprime(n):
    for i in range(2,(n//2)+1):
        if n % i == 0:
            return False
    else:
        return True
    
num = int(input('Enter a number: '))
print('Prime no.s between 2 &',num,'are :')
for i in range(2,num+1):
    if isprime(i):
        print(i,end = ' ')

'''
Q3
Create a function isarm() that accepts an integer as argument and return
True if supplied argument is Armstrong no; otherwise false.
Using above function,make a program that prints Armstrong no.s between
1 & N(given by user)
'''

# def isarm(num):
#     s = 0 
#     i = num
#     while i >0:
#         s += (i%10)**3
#         i //= 10
#     if num == s:
#         return True
#     else:
#         return False
    
# n = int(input('Enter a number: '))
# print('Armstrong numbers between 1 &',n, 'are :')
# for i in range(1,n+1):
#     if isarm(i):
#         print(i,end= ' ')


'''
Q4
Create a function isperfect(n) that accepts an integer as an argument
& return list of perfect numbers between 1 & N.
Using above function, make a program that prints perfect numbers
between 1 & N(given by user).
'''

# def isperfect(n):
#     lst = []
#     for num in range(1,n+1):
#         s = 0
#         for i in range(1,(num//2)+1):
#             if num%i == 0:
#                 s += i
#         if num == s:
#             lst.append(num)
#     return lst

# n = int(input('Enter a number: '))
# print('\nPerfect numbers between 1 &',n,'are: ')
# l = isperfect(n)
# print(l)

'''
Q5
Create a function ispalin() that accepts an integer as argument
& return true if supplied number is painn; otherwise return False.
'''

# def ispalin(n):
#     i = n
#     rev = 0
#     while i > 0:
#         rev = (rev*10) + (i%10)
#         i //= 10
#     if n == rev:
#         return True
#     else:
#         return False
    
# un = int(input('Enter N: '))
# for n in range(1,un+1):
#     if ispalin(n*n):
#         print('Square of ',n,':',n*n,' is palin.',sep='')

'''
Q6
Create a function GCD_LCM() that accepts two integer arguments & return
GCD & LCM of given numbers.
Using above function, Make a program that accepts 2 numbers from user
and print GCD & LCM of given numbers.
'''

# def GCD_LCM(n1,n2):
#     if x<y:
#         small = x
#     else:
#         small = y
#     for i in range(small,0,-1):
#         if x%i == 0 and y%i == 0:
#             return i, ((n1*n2)//i)
        
# x = int(input('Enter 1st no.: '))
# y = int(input('Enter 2nd no.: '))
# g, l = GCD_LCM(x,y)
# print('GCD:',g)
# print('LCM:',l)

'''
Q7
Create a function median() that accepts a list as argument & return
median of supplied list.
Using above function, make a program that prints median of entered
list (given by user).
'''

# def median(lst):
#     lst.sort()
#     n = len(lst)
#     if n%2 == 0:
#         return lst[n//2]
#     else:
#         return (lst[(n//2)-1] + lst[n//2])/2

# lst_main = eval(input('Enter a list: '))
# print('Original List:',lst_main)
# med = median(lst_main)
# print('Sorted List:',lst_main)
# print('Median:',med)

'''
Q8
Create a function rotate() that accepts a list and integer as
argument & rotates the elements of supplied list with rotation
factor as supplied argument.
Using above function, make a program that accepts a list and
rotation factor from user and rotate the list accordingly.
'''

# def rotate(rl,r):
#     l = len(rl)
#     n_lst = []
#     n_lst += rl[l-r:]
#     n_lst += rl[:l-r]
#     rl = list(n_lst)
#     return rl

# lst = eval(input('Enter a list: '))
# r = int(input('Enter rotation factor: '))
# print('\nEntered list:',lst)
# lst = rotate(lst, r)
# print('New list:',lst)

'''
Q9
Create a function fact() that receives a number as argument and
returns factorial of number.
Create a function power() that accepts two arguments and return
power of 1st number raised to the 2nd number.
Using above function, make a program to print answers of
harmonic series.
1) n!/n + ..... + 3!/3 + 2!/2 + 1!/1
2) x/1! + x^2/2! + x^3/3! + .... + x^n/n!
3) 1 + x^1/1! - x^2/2! + x^3/3! - ..... +- x^n/n!
4) x + x^2/3! + x^3/5! + x^4/7! + .....
'''

# def fact(n):
#     f = 1
#     for i in range(1,n+1):
#         f *= i
#     return f

# def power(x,n):
#     return x**n


# x = float(input('Enter x: '))
# n = float(input('Enter n: '))

# ##Series 1:
    
# ans = 0.0
# for t in range(int(n),0,-1):
#     f = fact(t)
#     ans += f/t
#     print(f,'/',t,':',f/t,'Ans=',ans)
# print('\nAnswer of Series 1:',ans)

# ## Series 2:
    
# ans = 0.0
# for t in range(1,int(n+1)):
#     p = power(x,t)
#     f = fact(t)
#     ans += p/f
#     print(f,"/",t,":",f/t,'ans=',ans)
# print('\nAnswer of Series 2:',ans)

# ## Series 3:
    
# ans = 1.0
# for t in range(1,int(n+1)):
#     p = power(x,t)
#     f = fact(t)
#     if t % 2 == 0:
#         ans -= p/f
#     else:
#         ans += p/f
#     print(p,'/',f,':',p/f,'Ans:',ans)
# print('\nAnswer of Series 3:',ans)

# ## Series 4:
    
# ans = 0.0
# for t in range(1,int(n+1)):
#     p = power(x,t)
#     f = fact((t*2)-1)
#     ans += p/f
#     print(p,'/',f,':',p/f,'Ans:',ans)
# print('\nAnswer of Series 4:',ans)

'''
Q 10
Create a function str_stat() that accepts a string and print string
statistics.
Create function str_palin that accepts a string & return True if
string is palindrome; otherwise False.
Create a function str_rev_case() that accepts a string and return
reversed case string.
Create a function str_cap() that accepts a string & return 
capitalized string.
Using above functions, make a menu driven program to perform option
chosen by user.
'''

# def str_stat(s):
#     l = len(s)

#     up = low = dig = space = sp = 0

#     for i in range(0,l):
#         if s[i].isupper():
#             up += 1
#         elif s[i].islower():
#             low += 1
#         elif s[i].isdigit():
#             dig += 1
#         elif s[i].isspace():
#             space += 1
#         else:
#             sp += 1

#     print('\nString:',s)    
#     print("Upper: ",up)
#     print("Lower: ",low)
#     print("Digits: ",dig)
#     print("Space: ",space)
#     print("Special char.: ",sp)
    
# def str_palin(st):
#     if st.upper() == st[::-1].upper():
#         return True
#     else:
#         return False

# def str_rev_case(st):
#     l = len(st)
#     r_st = ''
#     for i in range(0,l):
#         if st[i].isupper():
#             r_st += st[i].lower()
#         else:
#             r_st += st[i].upper()
#     return r_st

# def str_cap(st):
#     n_st = ''
#     n_st += st[0].upper()
    
#     i =1
#     while (i < len(st)):
#         if (st[i] != ' '):
#             n_st += st[i].lower()
#             i += 1
#         elif (st[i] == ' ' and st[i+1] != ' '):
#             n_st += ' '
#             n_st += st[i+1].upper()
#             i +=2
#         else:
#             n_st += ' '
#             i += 1
#     return n_st


# ## ___MAIN___

# strn = input('Enter a string: ')

# while True:
#     print('\n1: String Statistics:')
#     print('2: Print if string is palin or not:')
#     print('3: Print reversed case string:')
#     print('4: Print Capitalized string:')
#     print('0: Exit:')
#     ch = int(input('Enter your choice [1/2/3/4/0]: '))
    
#     if ch == 1:
#         str_stat(strn)
#     elif ch ==2:
#         if str_palin(strn):
#             print(strn,'is palin.')
#         else:
#             print(strn,'is not palin.')
#     elif ch == 3:
#         print('Reversed case string:',str_rev_case(strn))
#     elif ch == 4:
#         print('Capitalized String:',str_cap(strn))
#     elif ch == 0:
#         break
#     else:
#         print('Invalid input.')
#     input('Press enter to continue...')