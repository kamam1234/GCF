# students = {
# "101": {"name": "Tom", "grade": "A"},
# "102": {"name": "Jerry", "grade": "B"}
# }
# print(students["101"]["name"]) # Output: Tom


# string = """Hello\a
# This is a multiline string"""
# print(fr'{string[5]}')

# text = "Python  is my fav language"
# print(text[0])
# # Output: P
# print(text[-1])
# # Output: n
# print(text[4:9])
# # Output:

# s1 = "That was a game."
# s2 = "This was a game."
# print(s1.replace(s1, s2))

# email = input("Enter your email: ")
# if "@" in email and email.startswith("2403031260") and email.endswith(".in"):
#     print("Valid email")
# else:
#     print("Invalid email")

# email = input("Enter your email: ")
# if "@" in email and email.startswith("2403031260") and email.endswith(".in"):
#     print("Valid email")
# else:
#     print("Invalid email")

# # Concatenation
# greeting = "Hello" + " " + "World"
# print(greeting)
# # Repetition
# print("ha" * 3) # Output: hahaha
# # Membership
# print("Py" in "Python") # True

# check if entered number is prime or not
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

# marks = int(input("Enter your marks: "))
# if marks >= 35:
#   print("You passed!")
# else:
#   print("You failed.")

# grade = 85
# if grade >= 90:
#   print("A Grade")
# elif grade >= 80:
#   print("B Grade")
# elif grade >= 70:
#   print("C Grade")
# else:
#   print("Fail")

# for i in range(5):
#     print(" "*(4-i), end="")
#     print("* "*(i+1))

# for i in range(1,5):
#     print(" "*(i), end="")
#     print("* "*(5-i))

# # Write a program to check if a number is positive, negative or zero.
# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive number")
# elif num < 0:
#     print("Negative number")
# else:
#     print("Zero")

# # Create a loop that skips multiple of 3
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#   if i % 3 == 0:
#     continue
#   print(i, end=" ")
# print()

# # Create a loop to stop the loop if the user inputs a negative number
# while True:
#   n = int(input("Enter a number: "))
#   print("You entered",n)
#   if n < 0:
#     break

# Function
# def add(a, b):
#   """
#   Add two numbers.

#   Args:
#     a (int or float): The first number.
#     b (int or float): The second number.

#   Returns:
#     int or float: The sum of the two numbers.
#   """

#   return a + b
# a = 10
# b = 20
# print(add(a, b))

# # Lambda Function
# add = lambda a, b: [(a*i) + (b*i) for i in range(5)]
# print(add(10, 20))

# # Map Function
# numbers = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x**2, numbers))
# print(squares)

# def factorial(n):
#   if n == 0:
#     return 1

#   else:
#     fact = n
#     for i in range(n,1,-1):
#       fact *= (i-1)
#     return fact
# print(factorial(5))

# import math
# rad = int(input("Enter the radius of the circle: "))
# area = math.pi * rad**2
# print(f"The area of the circle is {area:.3f} units².")

# import calculator

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# print(f"Sum of {num1} and {num2} is {calculator.add(num1, num2)}")
# print(f"Difference of {num1} and {num2} is {calculator.subtract(num1, num2)}")
# print(f"Product of {num1} and {num2} is {calculator.multiply(num1, num2)}")
# print(f"Division of {num1} and {num2} is {calculator.divide(num1, num2)}")

# l = eval(input("Enter a list: "))
# reverse = l [::-1]
# print(f"The reverse of the list is {reverse}")

# l = eval(input("Enter a list: "))
# max = l[0]
# for i in l:
#     if i > max:
#         max = i
# print(f"The maximum number in the list is {max}.")

# min = int(input("Enter the minimum number: "))
# max = int(input("Enter the maximum number: "))
# sum = 0
# for i in range(min, max+1):
#     if i % 2 == 0:
#         sum += i
# print(f"The sum of even numbers between {min} and {max} is {sum}.")

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
  
#   def display(self):
#     print(f"Name: {self.name}")
#     print(f"Age: {self.age}")

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# person = Person(name, age)
# print()
# person.display()

# Write the code to create a calculator using oops concept

# class Calculator:
    
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def add(self):
#         return self.num1 + self.num2

#     def subtract(self):
#         return self.num1 - self.num2
    
#     def multiply(self):
#         return self.num1 * self.num2

#     def divide(self):
#         return self.num1 / self.num2
    
# x = int(input("Enter the 1st number: "))
# y = int(input("Enter the 2nd number: "))
# calc = Calculator(x, y)
# print(f"Sum of {x} and {y} is {calc.add()}")
# print(f"Difference of {x} and {y} is {calc.subtract()}")
# print(f"Product of {x} and {y} is {calc.multiply()}")
# print(f"Division of {x} and {y} is {calc.divide()}")

# find the second largest element in the list

l = eval(input("Enter a list: "))
l.sort()
max = l[-1]
for i in l[::-1]:
    if i < max:
        print(f"The second largest element in the list is {i}")
        break

# Sum of digits of a number

num = int(input("Enter a number: "))
n = num
sum = 0
while num > 0:
    rem = num % 10
    sum += rem
    num //= 10
print(f"The sum of digits of {n} is {sum}")

# First n prime numbers

n = int(input("Enter the value of n: "))
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")