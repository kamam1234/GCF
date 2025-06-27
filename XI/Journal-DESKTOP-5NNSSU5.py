# -*- coding: utf-8 -*-
'''
Created on Sat Sep 24 13:30:51 2022
Journal
@author: Ankur Macwan.
'''


'''
1 WAP to calculate BMI.
'''
# w = float(input('Enter your weight(in kg): '))
# h = float(input('Enter your height(in m): '))
# bmi = w / (h * h)
# print('\nWeight: ',w)
# print('Height: ',h)
# print('BMI: ',bmi)


"""
2 Vol and area of cylinder
"""
# r =float(input('Enter the radius: '))
# h = float(input('Enter the height: '))
# pi = 3.1415926
# vol = pi * r * r * h
# area = 2 * pi * r * (r+h)
# print('\nRadius: ',r)
# print('Height: ',h)
# print('Volume: ',vol)
# print('Area:',area)


"""
3 Swap values
"""
# a = int(input('Enter 1st number: '))
# b = int(input('Enter 2ndd number: '))
# print('Original numbers: ', a , 'and',b)
# c = a
# a = b
# b = c
# print('Swapped numbers:', a ,'and' , b)


"""
4 WAP to convert dist of m and cm to feet and inches.
"""
# m = int(input('Enter dist. in m: '))
# cm = int(input('Enter dist. in cm: '))
# tm = (m*100)+cm
# f = int(tm // 2.54)
# i = int(tm % 2.54)
# print('\nDist. in m: ',m)
# print('Dist. in cm: ',cm)
# print('Dist. in feet: ',f)
# print('Dist. in inches: ',i)


"""
5 Sum of two durations:
"""
# h1 = int(input('Enter Hour 1: '))
# m1 = int(input('Enter Min. 1: '))
# h2 = int(input('Enter Hour 2: '))
# m2 = int(input('Enter Min. 2: '))
# tm = (h1*60)+(h2 *60)+ m1 + m2

# sh = tm // 60
# sm = tm % 60
# print('\nDuration 1 -->',h1,':',m1)
# print('Duration 2 -->',h2,':',m2)
# print('\nSum of Durations -->',sh,':',sm)


"""
6 Accept three no.s and Find smallest Number:
"""
# n1 = int(input('Enter No. 1: '))
# n2 = int(input('Enter No. 2: '))
# n3 = int(input('Enter No. 3: '))
# m = n1
# if n2 < n1:
#     m = n2
# elif n3 < n1:
#     m = n3
# print(m,'is smallest number.')


"""
7 EvEN OR ODD
"""
# n = int(input('Enter a no.: '))
# if n%2==0:
#     print(n,'is even.')
# else:
#     print(n,'is odd.')

"""
8 +ve, -ve or zero
"""
# n = float(input('Enter a no.: '))
# if n>0:
#     print(n,'is +ve.')
# elif n<0:
#     print(n,'is -ve.')
# else:
#     print(n,'is 0.')


"""
9 Accepts marks of three sub and print if pass or fail.
Also print total and percentage
"""
# s1 = int(input('Enter marks of 1st Sub.: '))
# s2 = int(input('Enter marks of 2nd Sub.: '))
# s3 = int(input('Enter marks of 3rd Sub.: '))
# st = ''
# if (s1 >= 33) and (s2 >= 33) and (s3 >= 33):
#     st = 'Pass'
# else:
#     st = 'Fail'
# tot = s1 + s2 + s3
# per = tot / 3
# print('\n1st Sub. Marks(Out of 100):',s1)
# print('2nd Sub. Marks(Out of 100):',s2)
# print('3rd Sub. Marks(Out of 100):',s3)
# print('Status:',st)
# print('Total:',tot)
# print('Percentage:',per)

"""
10 right triangle or not
"""
# s1 = int(input('Enter side 1: '))
# s2 = int(input('Enter side 2: '))
# s3 = int(input('Enter side 3: '))
# ss1 = s1 ** 2
# ss2 = s2 ** 2
# ss3 = s3 ** 2
# if (ss1 + ss2 == ss3) or (ss1 + ss3 == ss2) or (ss2 + ss3 == ss1):
#     print('It\'s a right triangle.')
# else:
#     print('It\'s not a right triangle.')

"""
11 leap year or not
"""
# y = int(input('Enter a year: '))
# if (y%1000 == 0) or (y%100 != 0) and (y%4 == 0):
#     print(y,'is a leap year.')
# else:
#     print(y,'is not a leap year.')


"""
12 bill
first 50 calls 0.0 / call
next 100 calls 0.5 / call
next 100 calls 0.7 / call
next 100 calls 1.0 / call
min bill: 25
gst : 18% of bill
payable amt
"""
# n = int(input('Enter the no. calls: '))
# bill = 0
# if n <= 50:
#     bill = 25
# elif n <= 150:
#     bill += (n-50)*0.5
# elif n <= 250:
#     bill += (n-150)*0.7
# elif n <= 350:
#     bill = (n-250)*1 + (100*0.7) + (100*0.5)
# print(bill)


"""
13
a) 1 2 3 4 5 6 7 8 9 10
b) Ans = 1 + 3 + 5 + 7 + ....... + N
c) 1 -2 3 -4 5 -6 7 -8 ..... n
d) 1 4 9 16 25 ..... N*N
e) 0 1 1 2 3 5 8 13 ....... N
"""
# print('Series A:')
# for i in range(1,11):
#     print(i, end=' ')
    
# print('Series B:')
# n = int(input('Enter N: '))
# ans = 0
# for i in range(1,n+1,2):
#     ans += i
# print('Ans:',ans)

# print('Series C:')
# n = int(input('Enter N: '))
# for i in range(1,n+1):
#     if i%2==0:
#         print(-i,end='  ')
#     else:
#         print(i,end=' ')

# print('Series D:')
# n = int(input('Enter N: '))
# for i in range(1,n+1):
#     print(i**2,end=' ')

# print('Series E:')
# n = int(input('Enter N: '))
# i = 0
# j = 1
# while i <= n:
#     print(i,end=' ')
#     if j <= n:
#         print(j,end=' ')
#     i += j
#     j += i

""" Q 14
Multipilcation Table
"""
# n = int(input('Enter a no. to print its Table: '))
# i = 1
# while i <= 10:
#     print(n,"x",i,"=",n*i)
#     i += 1

"""
Q 15
factorial
"""
# n = int(input('Enter a no. to print its factorial: '))
# f = 1
# for i in range(1,n+1):
#     f *= i
# print(n,"! = ",f,sep ='')


"""
Q 16
factorial upto n
"""
# n = int(input('Enter no. to print factorials upto n: '))
# f = 1
# for i in range(1,n+1):
#     f *= i
#     print(i,"! = ",f,sep ='')


'''
Q 17
x raised to y
'''
# x = int(input('Enter base: '))
# y = int(input('Enter power: '))
# p = 1
# for i in range(1,y+1):
#     p *= x
# print(x,'^',y,' = ',p,sep='')


'''
Q 18
Accept a num, print NOD, SOD, REV and print if it"s palin or not
'''

# n = int(input('Enter a no.: '))
# nod = 0
# sod = 0
# rev = 0
# i = n
# while i > 0:
#     nod += 1
#     sod += i%10
#     rev = (rev*10) + (i%10)
#     i = i//10
# print('No. of Digits: ',nod)
# print('Sum of Digits: ',sod)
# print('Reverse: ',rev)
# if rev == n:
#     print(n,"is palin.")
# else:
#     print(n,"is not palin.")


"""
Q 19
Factors of number
"""
# n = int(input('Enter a no.: '))
# print('\nFactors of',n,"are :",end=" ")
# for i in range(1,(n//2)+1):
#     if n%i == 0:
#         print(i,end=" ")
# print(n)


"""
Q 20
Accepts 2 no.s and print GCD and LCM
"""
# x = int(input('Enter 1st no.: '))
# y = int(input('Enter 2nd no.: '))
# gcd = 0
# if x > y:
#     s = x
# else:
#     s = y
# for i in range(s,0,-1):
#     if (x%i)==0 and (y%i)==0:
#         gcd = i
#         break
# print("\n1st no.: ",x)
# print("2nd no.: ",y)
# print("GCD:",gcd)
# print("LCM:",(x*y)//gcd)


"""
Q 21
Write a program that accepts a number and prints if it"s
prime or not.
"""
# n = int(input('Enter N: '))
# for i in range(2,n):
#     if n % i == 0:
#         print(n,'is not prime.')
#         break
# else:
#     print(n,'is prime.')


'''
Q 22
Write a program that prints following alpha series:
a) A B C .... X Y Z
b) Aa Bb Cc Dd ..... Yy Zz
c) A b C d E f G h I j K l M n O p Q r S t U v W x Y z
d) ABc DEF GHi JKL MNo PQR STu VWX Y
e) AB cd EF gh IJ kl MN op QR st UV wx YZ
f) AbC Def GhI JkL MnO PqR StU VwX Yz
'''
# print("Series A:")
# for i in range(1,27):
#     print(chr(i+64),end=" ")

# print("Series B:")
# for i in range(1,27):
#     print(chr(i+64),chr(i+96),end=" ",sep="")

# print("Series C:")
# for i in range(1,27):
#     if i%2==0:
#         print(chr(i+96),end=" ")
#     else:
#         print(chr(i+64),end=" ")

# print("Series D:")
# for i in range(1,27):
#     if i%3==0:
#         print(chr(i+96),end=" ")
#     else:
#         print(chr(i+64),end="")

# print('Series E:')
# for i in range(1,27):
#     if i%4==1:
#         print(chr(i+64),end="")
#     elif i%4==2:
#         print(chr(i+64),end=" ")
#     elif i%4==3:
#         print(chr(i+96),end="")
#     else:
#         print(chr(i+96),end=" ")

# print("Series F:")
# for i in range(1,27):
#     if i%3==1:
#         print(chr(i+64),end="")
#     elif i%3==2:
#         print(chr(i+96),end="")
#     else:
#         print(chr(i+64),end=" ")


"""
Q23
Armstrong no. or not
"""
# n = int(input('Enter N: '))
# soc = 0
# i = n
# while i > 0:
#     soc += (i%10)**3
#     i = i//10
# if soc == n:
#     print('Armstrong No.')
# else:
#     print('Not Armstrong.')


"""
Q 24
Write a program that prints numbers upto N whose
squares are palin.
"""
# n = int(input('Enter a number: '))
# print('No.s whose squares are palin are:')
# for k in range(1, (n)+1):
#     j = k * k
#     i = k * k
#     rev = 0
#     while j>0:
#         rev = (rev*10) + (j%10)
#         j = j//10
#         if rev == i:
#             print('Square of ',k,' is ',i,'. Rev: ',rev,sep='')


"""
Q 25
Write a program that prints all prime numbers between 2 and N.
"""
# n = int(input("Enter N: "))
# print("Prime no.s between 2 and",n,"are :",end=' ')
# for i in range(2,n+1):
#     for j in range(2,(i//2)+1):
#         if i%j==0:
#             break
#     else:
#         print(i,end=" ")


"""
Q 26
WAP to print aemstrong numbers between 1 & 1000
"""
# print("Armstrong no.s between 1 and 1000: ")
# for i in range(1,1001):
#     soc = 0
#     j = i
#     while i > 0:
#         soc += (i%10)**3
#         i = i//10
#         if soc == j:
#             print(j,end=" ")


"""
Q 27
i) 1/n! + ........ + 1/3! + 1/2! + 1/1!
11) x^1/1! + x^2/2! + x^3/3! + ........ + x^n/n!
iii) 1 + x^1/1! - x^2/2! + ..... +- x^n/n!
iv) x + x^2/3! + x^3/5! + .... + x^n/n*2-1
"""
# print("Series 1: ")
# n = int(input('Enter N: '))
# ans = 0
# for j in range(n,0,-1):
#     f = 1
#     for i in range(1,j+1):
#         f *= i
#         ans += 1/f
# print("Answer:",ans)

# print("Series 2:")
# x = int(input('Enter x: '))
# n = int(input('enter the no of terms: '))
# ans = 0
# for j in range(1,n+1):
#     p = x ** j
#     f = 1
#     for i in range(1,j+1):
#         f *= i
#     ans += p/f
# print('Answer: ',ans)

# print("Series 3:")
# x = int(input('Enter x: '))
# n = int(input('enter the no of terms: '))
# ans = 1
# for j in range(1,n+1):
#     p = x ** j
#     f = 1
#     for i in range(1,j+1):
#         f *= i
#     if j%2 == 0:
#         ans -= p/f
#     else:
#         ans += p/f
# print('Answer: ',ans)

# print("Series 4: ")
# x = int(input('Enter X: '))
# n = int(input('Enter no. of terms: '))
# ans = 0
# for j in range(1,n+1):
#     p = x **j
#     f = 1
#     for i in range(1,j*2):
#         f *= i
#     ans += p/f
# print('Answer: ',ans)


"""
Q 28
Wap to print patterns:
"""
"""
a)
*
**
***
****
*****
"""
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
"""
b)
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()
"""c)
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""
# n=5
# for i in range(n,0,-1):
#     for j in range(n,i-1,-1):
#         print(j,end=' ')
#     print()
"""f)
A
A B
A B C
A B C D
A B C D E
"""
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(j+64),end=" ")
#     print()
"""g)
a b c d e
b c d e
c d e
d e
d
"""
# n = 5
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(chr(j+96),end=" ")
#     print()
"""h)
E d C b A
E d C b
E d C
E d
E
"""
# n = 5
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         if j%2==0:
#             print(chr(j+96),end=" ")
#         else:
#             print(chr(j+64),end=" ")
#     print()

"""i)
A
B b
C c C
D d D d
E e E e E
"""
# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j%2==0:
#             print(chr(i+96),end=" ")
#         else:
#             print(chr(i+64),end=" ")
#     print()
"""j)
e
DD
ccc
BBBB
aaaaa
"""
# n = 5
# for i in range(n,0,-1):
#     for j in range(i,n+1):
#         if i%2==0:
#             print(chr(i+64),end=" ")
#         else:
#             print(chr(i+96),end=" ")
#     print()
"""k)
    A
   A B
  A B C
 A B C D
A B C D E
"""
# n = 5
# for i in range(1,n+1):
#     for j in range(i,n):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(chr(i+64),end=" ")
#     print()
"""l)
    A
   B C
  D E F
 G H I J
K L M N O
"""
# n = 5
# c = 1
# for i in range(1,n+1):
#     for j in range(i,n):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(chr(c+64),end=" ")
#         c += 1
#     print()

"""m)
        E
      E D E
    E D C D E
  E D C B C D E
E D C B A B C D E
  E D C B C D E
    E D C D E
      E D E
        E
"""
# n = 5
# for i in range(n,1,-1):
#     for j in range(1,i):
#         print(end="  ")
#     for j in range(n,i,-1):
#         print(chr(j+64),end=" ")
#     for j in range(i,n+1):
#         print(chr(j+64),end=' ')
#     print()
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(end="  ")
#     for j in range(n,i,-1):
#         print(chr(j+64),end=" ")
#     for j in range(i,n+1):
#         print(chr(j+64),end=" ")
#     print()
'''
n)
A B C D E D C B A
A B C D   D C B A
A B C       C B A
A B           B A
A               A
A B           B A
A B C       C B A
A B C D   D C B A
A B C D E D C B A
'''
# print("Pattern 14:")
# n = 5
# for i in range(n,1,-1):
#     for j in range(1,i+1):
#         print(chr(j+64),end=" ")
#     for j in range (1,(n-i)*2):
#         print(end="  ")
#     for j in range (i,0,-1):
#         if j != n:
#             print(chr(j+64),end=" ")
#     print()
# for i in range (1,n+1):
#     for j in range(1,i+1):
#         print(chr(j+64),end=" ")
#     for j in range(1,(n-i)*2):
#         print(end="  ")
#     for j in range(i,0,-1):
#         if j != n:
#             print(chr(j+64),end=" ")
#     print()
'''
o)
        1
      1 0 1
    1 0 1 0 1
  1 0 1 0 1 0 1
1 0 1 0 1 0 1 0 1
  1 0 1 0 1 0 1
    1 0 1 0 1
      1 0 1
        1
'''
n = 5
for i in range(n,1,-1):
    for j in range(1,i):
        print(end='  ')
    for j in range(n,i,-1):
        print(j%2,end=' ')
    for j in range(i,n+1):
        print(j%2,end=' ')
    print()
for i in range(1,n+1):
    for j in range(1,i):
        print(end='  ')
    for j in range(n,i,-1):
        print(j%2,end=' ')
    for j in range(i,n+1):
        print(j%2,end=' ')
    print()

'''
Q 29
WAP that accepts a string and traverse through it by value and by
index in forward & backward direction using forward & backward index.
'''
# s = input('Enter a string: ')
# print('\nTraversal by value:')
# for i in s:
#     print(i,end=' ')
# print('\nForward Traversal using forward index:')
# for i in range(0,len(s)):
#     print('Character \'',s[i],'\' found at  ',i,sep='')
# print('\nBackward Traversal using backward index:')
# for i in range(len(s)-1,-1,-1):
#     print('Character \'',s[i],'\' found at  ',i,sep='')
# print('\nForward Traversal using backward index:')
# for i in range(-len(s),0):
#     print('Character \'',s[i],'\' found at ',i,sep='')
# print('\nBackward Traversal using backward index:')
# for i in range(-1,-len(s)-1,-1):
#     print('Character \'',s[i],'\' found at ',i,sep='')

'''
Q 30
WAP that reads a line and print its statistics
(Uppercase, lowercase and Alphabets)
'''
# s = input('Enter a string: ')
# up = low = dig = 0

# for i in range(1,len(s)):
#     if s[i].isupper():
#         up += 1
#     if s[i].islower():
#         low +=1
#     if s[i].isdigit():
#         dig += 1
# print('Upper:',up)
# print('Lower:',low)
# print('Digit:',dig)

'''
Q31
WAP that accepts a string and print total no of vowels and Alphabets
'''
# st = input('Enter a String: ')
# alpha = vow = 0
# for i in st:
#     if i.isalpha():
#         alpha += 1
#     if i in 'aeiouAEIOU':
#         vow += 1
# print('Alphabets:',len(st))
# print('Vowels:',vow)
# print('Consonants:',alpha-vow)

'''
Q 32
WAP that accepts a string and convert it into alphanumeric string
by removing other characters (except space)
'''
# st = input('Enter a string: ')
# ns = ''
# for i in st:
#     if i.isalnum():
#         ns += i
#     if i.isspace():
#         ns += i
# st = ns
# print(st)

'''
Q33
WAP that accepts a string and print it is palin or not
'''
# st = input('Enter a string: ')
# if st.upper() == st[::-1].upper():
#     print('Palin.')
# else:
#     print('Not Palin.')

'''
Q34
WAP that accepts a string and print it in reverse order and
reverse case.
'''
# st = input('Enter a string: ')
# print('\n\nReverse ordered and reverse cased string:')
# for i in st[::-1]:
#     if i.isupper():
#         print(i.lower(),end='')
#     else:
#         print(i.upper(),end='')

'''
Q 35
WAP that accepts a password string and check if it
is strong or not.
(A password must be atleast 8 characters long and must contain
 atleast one character of following: Uppercase, Lowercase, digit
 and special character.) 
'''
# st = input('Enter a password: ')
# up = low = dig = sp = 0
# for i in st:
#     if i.isupper():
#         up += 1
#     elif i.islower():
#         low += 1
#     elif i.isdigit():
#         dig += 1
#     else:
#         sp += 1
# if len(st)<8:
#     print('Not strong. Len < 8')
# elif up == 0:
#     print('Not strong. No uppercase char.')
# elif low == 0:
#     print('Not strong. No lowercase char.')
# elif dig == 0:
#     print('Not strong. No digit.')
# elif sp == 0:
#     print('Not strong. No special character.')
# else:
#     print('Strong Password.')

'''
Q36
WAP that accepts a string and print every alternate character in
uppercase and other character in lowercase.
'''
# s = input('Enter a string: ')
# print()
# for i in range(len(s)):
#     if i %2 == 0:
#         print(s[i].upper(),end='')
#     else:
#         print(s[i].lower(),end='')

'''
Q37
WAP that accepts a string and a character and check the
occurence of entered character along with its position
'''
s = input('ENter a string: ')
ch = input('Enter a character to check its occurence: ')
print('\nChar',ch,'found at position(s): ')
for i in range(len(s)):
    if ch.lower() == s[i].lower():
        print(i+1,end=' ')
        
'''
Q38
WAP that accepts a string and find largest and shortest word
'''

'''
Q39
WAP that accepts 2 strings and check if any string is prefix of
another or not.(without using startswith() function)
'''

'''
40WAP that accepts a lists from a user and print
sum of all even and odd values.
Also print sum of even and odd positioned values.
'''
# lst = eval(input("enter a list: "))
# se = so = sep = sop = 0
# for i in range(len(lst)):
#     if (lst[i] % 2) == 0:
#         se += lst[i]
#     else:
#         so += lst[i]
#     if i%2 == 0:
#         sop += lst[i]
#     else:
#         sep += lst[i]
# print('\nSum of even values: ',se)
# print('Sum of odd values: ',so)
# print('Sum of even positioned values: ',sep)
# print('Sum of odd positioned values: ',sop)

'''
41WAP that accepts 2 lists from user and print
if lists are overlapped or separated.
'''
# l1 = eval(input("enter 1st list: "))
# l2 = eval(input("enter 2nd list: "))
# for v in l1:
#     if v in l2:
#         print('Lists are overlapped.')
#         break
# else:
#     print('Lists are separated.')

'''
42WAP that accepts a list and swap each odd
positioned element with even positioned element
'''
# l = eval(input('enter a list: '))
# print('\n\nList before swapping: ', l)
# for i in range(1,len(l),2):
#     l[i],l[i-1] = l[i-1],l[i]
# print('List after swapping: ',l)

'''
43WAP that accepts a list from user and swap
the first half with the other half.
'''
# lst = eval(input('enter a list: '))
# print('List before Swapping:',lst)
# l = len(lst)
# if l % 2 == 0:
#     lst[:l//2],lst[l//2:]=lst[l//2:],lst[:l//2]
# else:
#     lst[:(l//2)], lst[(l//2)+1:] = lst[(l//2)+1:], lst[:(l//2)]
# print('Swapped list: ',lst)

'''
44WAP that accepts a list and rotation factor
and rotate the 
list considering the rotation factor.
'''
# lst = eval(input('enter a list: '))
# r = int(input('enter rotation factor: '))
# print('\nOriginal List: ',lst)
# if r>=0 and r<=len(lst):
#     r_lst = []
#     r_lst += lst[-r:]
#     r_lst += lst[:-r]
#     lst = r_lst
#     print('Rotated list: ',lst)
# else:
#     print('Invalid Rotation factor')

'''
45WAP that accepts a list and print unique &
repeated elements of list.
Also print the frequency of all elements.
'''
# lst = eval(input('enter a list: '))
# un = []
# du = []
# for ele in lst:
#     if ele not in du:
#         cnt = lst.count(ele)
#         print("Frequency of '",ele,"' is ",cnt,sep='')
#         if cnt == 1:
#             un.append(ele)
#         else:
#             du.append(ele)
# print('\nOriginal list:',lst)
# print('List of Unique elements:',un)
# print('List of Duplicate elements:',du)

'''
46WAP that accepts a list and print mean, median,
mode and range of the list.
'''
# lst = eval(input('enter a list: '))
# n = len(lst)
# mean = sum(lst)/n
# srt = sorted(lst)
# mid = n//2
# if n%2 == 0:
#     median = (srt[mid]+srt[mid-1])/2
# else:
#     median = srt[mid]
# mfreq = 0
# for ele in lst:
#     freq = lst.count(ele)
#     if freq > mfreq:
#         mfreq = freq
# mode = []
# for ele in lst:
#     if lst.count(ele) == mfreq and ele not in mode:
#         mode.append(ele)
# rng = max(lst) - min(lst)
# print('\nMean:',mean)
# print('Median:',median)
# print('Mode:',mode,'with frequency of',mfreq)
# print('Range:',rng)

'''
47WAP that accepts a list containing several 0s &
shift all 0 to the right side of the list:
'''
# l = eval(input('enter a list: '))
# print('\nentered List:',l)
# cnt = l.count(0)
# for i in range(cnt):
#     l.remove(0)
# l = l + ([0]*cnt)
# print('Updated list: ',l)

'''
48WAP that accepts a list and make it a non duplicated list
'''
# lst = eval(input('enter a list: '))
# print('\nOriginal List: ',lst)
# lstnd = []
# for v in lst:
#     if v not in lstnd:
#         lstnd.append(v)
# lst = lstnd
# print('Updated list: ',lst)

'''
49WAP that accepts a list of fibonacci series using
a list upto N
'''
# n = int(input('enter N: '))
# if n == 1:
#     print([0])
# else:
#     l = [0,1]
#     for i in range(2,n):
#         v = l[i-1] + l[i-2]
#         l.append(v)
#     print('\n',l)

'''
50WAP that accepts two lists and find the difference of
elements index
'''
# ls1 = eval(input('enter 1st list:'))
# ls2 = eval(input('enter 2nd list:'))
# if ls1 == ls2:
#     print('Both the lists are same.')
# else:
#     l1 = len(ls1)
#     l2 = len(ls2)
#     for i in range(min(l1,l2)):
#         if ls1[i] != ls2[i]:
#             print('Difference found at position',i+1)
#             break
#     else:
#         print('Difference found at position',i+2)

'''
51WAP that accepts 2 matrices and find the sum of those 2 matrices
'''
# r = int(input('enter no. of rows: '))
# c = int(input('enter no. of columns: '))
# print('\nEnter values for 1st Matrix.')
# m1 = []
# for i in range(r):
#     m1.append([])
#     for j in range(c):
#         m1[i].append(int(input('enter Value: ')))
# print('\nenter values for 2nd Matrix.')
# m2 = []
# for i in range(r):
#     m2.append([])
#     for j in range(c):
#         m2[i].append(int(input('enter Value: ')))
# sm = []
# for i in range(r):
#     sm.append([])
#     for j in range(c):
#         sm[i].append(m1[i][j] + m2[i][j])

# print('\nMatrix 1:')
# for i in range(r):
#     for j in range(c):
#         print(m1[i][j],end='\t')
#     print()
# # print()
# #     print()
# print('\nMatrix 2:')
# for i in range(r):
#     for j in range(c):
#         print(m2[i][j],end='\t')
#     print()
# print('\nSum of Matrices:')
# for i in range(r):
#     for j in range(c):
#         print(sm[i][j],end='\t')
#     print()

'''
52WAP that accepts 2 matrices & produces the product of
those matrices
Columns of 1st matrix must be equal to
the rows of the second matrix. (Neccessary Condition)
'''
m1 = []
m2 = []
mp = []
r1 = int(input('enter rows of 1st matrix: '))
c1 = int(input('enter columns of 1st matrix: '))
r2 = int(input('enter rows of 2nd matrix: '))
c2 = int(input('enter columns of 2nd matrix: '))
if c1 == r2:
    print('\nenter values in 1st matrix:')
    for i in range(r1):
        m1.append([])
        for j in range(c1):
            m1[i].append(int(input('enter Value: ')))
    print('\nenter values in 2nd matrix:')
    for i in range(r2):
        m2.append([])
        for j in range(c2):
            m2[i].append(int(input('enter Value: ')))
    mp = []
    rp = r1
    cp = c2
    for i in range(rp):
        mp.append([])
        for j in range(cp):
            mp[i].append(0)
            for k in range(c1):
                mp[i][j] += (m1[i][k] * m2[k][j])
    print('\nMatrix 1:')
    for i in range(r1):
        for j in range(c1):
            print(m1[i][j],end='\t')
        print()
    print('\nMatrix 2:')
    for i in range(r2):
        for j in range(c2):
            print(m2[i][j],end='\t')
        print()
    print('\nProduct of Matrices:')
    for i in range(rp):
        for j in range(cp):
            print(mp[i][j],end='\t')
        print()
else:
    print('Product is not possible.')