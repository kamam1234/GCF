# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:30:25 2023

@author: HP
"""
n = int(input('Enter a number to print fibonacci series upto: '))
a= 0
b = 1
print(a)
print(b)
while True:
    c = a + b
    a , b = b , c
    if c < n:
        print(c)
    else:
        break

# import line_profiler
# c = '''
# n = int(input('ENter n: '))

# def fib(n):
#     ans = [0,1]
#     for i in range(2,n+1):
#         ans.append(ans[i-1]+ ans[i-2])
    
#     print (ans)
# fib(n)'''

# pro = line_profiler.LineProfiler()
# pro.run(c)
# pro.print_stats()
