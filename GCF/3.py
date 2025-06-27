# class BankAccount:
#     def _init_(self, balance):
#         self.__balance = balance #Private attribute
#     def deposit(self, amount):
#         self.__balance += amount
#     def get_balance(self):
#         return self.__balance
# acct = BankAccount(1000)
# acct.deposit(500)
# print(acct.get_balance()) # Output: 1500

# # create a code for polymorphism in python
# class Animal:
#     def speak(self):
#         # remove raise NotImplementedError
#         return "Some sound"
    
# class Dog():
#     def speak(self):
#         return "Woof!"

# class Cat():
#     def speak(self):
#         return "Meow!"

# def animal_sound(animal):
#     print(animal.speak())
# dog = Dog()
# cat = Cat()
# animal_sound(dog)  # Output: Woof!
# animal_sound(cat)  # Output: Meow!


# # Bank Account Management System
# # Problem:
# # Create a class BankAccount with the following:
# # Account_number, account_holder, balance Attributes: account_nu
# # Methods:
# # deposit(amount)
# # withdraw(amount)
# # display_balance()
# # Follow-up:
# # Create multiple objects and simulate transactions.

# class BankAccount:
#     def __init__(self, account_number, account_holder, balance=0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited: {amount}. New balance: {self.balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew: {amount}. New balance: {self.balance}")
#         else:
#             print("Insufficient funds or invalid withdrawal amount.")

#     def display_balance(self):
#         print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")
        
# account1 = BankAccount("123456", "John Doe")
# account2 = BankAccount("789012", "Jane Smith", 500)

# print('Account 1:')
# account1.deposit(500)
# account1.withdraw(200)
# account1.display_balance()
# account1.withdraw(400)
# account1.display_balance()
# account1.deposit(-100)
# account1.display_balance()
# print('\nAccount 2:')
# account2.deposit(1000)
# account2.withdraw(300)
# account2.display_balance()
# account2.withdraw(1000)
# account2.display_balance()

# Artificial Intelligence (AI) is a field of study that focuses on creating intelligent machines 
# capable of performing tasks that typically require human intelligence, such as visual perception, 
# speech recognition, decision-making, and language translation. AI systems use algorithms and data 
# structures to analyze data, make decisions, and take actions, often in real-time and with minimal 
# human intervention. The primary goal of AI is to create machines that can learn from experience, 
# reason about the world, and interact with humans in a natural way.

# import numpy as np

# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.array([[7, 8, 9], [10, 11, 12]])
# print(a @ b)  # Matrix multiplication
# print(a * b)  # Element-wise multiplication

# # A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

# class Car:
#     # The __init__ method is a special method called a constructor. It initializes the attributes of the class.
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     # A method is a function that is defined inside a class and is associated with an object.
#     def description(self):
#         return f"{self.year} {self.make} {self.model}"

#     def start_engine(self):
#         return "Engine started"

# # Creating an object of the class Car
# my_car = Car("Toyota", "Corolla", 2020)

# # Calling the methods of the Car class
# print(my_car.description())  # Output: 2020 Toyota Corolla
# print(my_car.start_engine()) # Output: Engine started


# # PRACTICE TASKS
# # 1. Create an example showing encapsulation using private variables.
# # 2. Show method overriding with base and derived classes.

# # 1 Encapsulation Example
# # Encapsulation is the concept of hiding the implementation details 
# # from the user and only exposing the required information. In this 
# # example, the balance attribute is private and can only be accessed 
# # through the public methods deposit, get_balance, and withdraw.

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Deposit amount must be positive.")

#     def get_balance(self):
#         return self.__balance

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds or invalid withdrawal amount.")
# acct = BankAccount(1000)
# acct.deposit(500)
# print(acct.get_balance())  # Output: 1500
# acct.withdraw(200)
# print(acct.get_balance())  # Output: 1300

# # 2 Method Overriding Example
# # In this example, the Animal class has a method called speak. The Dog
# # and Cat classes override the speak method to provide their own 
# # implementation. The animal_sound function takes an Animal object as 
# # an argument and calls the speak method on it. The output depends on 
# # the type of Animal object passed to the function.

# class Animal:
#     def speak(self):
#         return "Some sound"

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
# def animal_sound(animal):
#     print(animal.speak())
# dog = Dog()
# cat = Cat()
# animal_sound(dog)  # Output: Woof!
# animal_sound(cat)  # Output: Meow!

# # 3 Method Overloading Example
# # In this example, the MathOperations class has two methods with the 
# # same name add. The first add method takes two arguments and returns 
# # their sum. The second add method takes three arguments and returns 
# # their sum. The output depends on the number of arguments passed to 
# # the add method.

# class MathOperations:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):
#         return a + b + c
# math_op = MathOperations()
# print(math_op.add(1, 2))        # Output: 3
# print(math_op.add(1, 2, 3))     # Output: 6
    
# # 4 Base and Derived Class Example
# # In this example, the Vehicle class has a start method. The Car and 
# # Bike classes are derived from the Vehicle class and override the 
# # start method to provide their own implementation. The vehicle_start
# # function takes a Vehicle object as an argument and calls the start 
# # method on it. The output depends on the type of Vehicle object 
# # passed to the function.

# class Vehicle:
#     def start(self):
#         return "Vehicle started"

# class Car(Vehicle):
#     def start(self):
#         return "Car started"
# class Bike(Vehicle):
#     def start(self):
#         return "Bike started"
# def vehicle_start(vehicle):
#     print(vehicle.start())
# car = Car()
# bike = Bike()
# vehicle_start(car)  # Output: Car started
# vehicle_start(bike) # Output: Bike started

# # 5 Abstract Class Example
# # In this example, the Shape class is an abstract class. It has an 
# # abstract method area. The Circle and Rectangle classes are derived 
# # from the Shape class and override the area method to provide their 
# # own implementation. The print_area function takes a Shape object as 
# # an argument and calls the area method on it. The output depends on 
# # the type of Shape object passed to the function.

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2  
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
# def print_area(shape):
#     print(f"Area: {shape.area()}")
# circle = Circle(5)
# rectangle = Rectangle(4, 6)
# print_area(circle)      # Output: Area: 78.5
# print_area(rectangle)   # Output: Area: 24


# try:
#     print(34/0)
# except:
#     print(f"Error: Cannot divide by zero.")
# finally:
#     print("\nExecution completed.")

# age = int(input("Enter your age: "))
# if age < 18:
#     raise ValueError("Age must be 18 or older.")
# else:
#     print("Access granted.")

# try:
#     print(10/"hello")
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     print("Execution completed.")
# try:
#     print('\r')
# finally:
#     print("This block always executes, regardless of exceptions.")

# # Raising exception
# balance = 1000
# withdrawal = int(input("Enter the money to be withdrawn: "))
# try:
#     if withdrawal < 0:
#         raise ValueError("Withdrawal amount cannot be negative.")
#     if balance < withdrawal:
#         raise ValueError("Insufficient balance for withdrawal.")
# except ValueError as e:
#     print(f"Error: {e}")
# else:
#     print("Money withdrawn successfully.")

file = open('1.txt', 'w')
file.write('''Yes
possible''')
file.close()

# file = open('1.txt', 'r')
# content = file.read()
# print(content) 
# file.close()


# Create a text file and write student names to it.
# Read and print the content of that file line by line.
# Append exam scores to the file.
# Copy the content of one file to another.
# Count the number of lines, words, and characters in a file.

# Create a text file and write student names to it.
file = open('students.txt', 'w')
students = ['Alice', 'Bob', 'Charlie', 'David']
for student in students:
    file.write(student + '\n')
file.close()

# Read and print the content of that file line by line.
file = open('students.txt', 'r')
print("Student Names:")
for line in file:   
    print(line.strip())  # Using strip() to remove the newline character
file.close()

# Append exam scores to the file.
file = open('students.txt', 'a')
scores = [90, 80, 85, 95]
for score in scores:
    file.write(f"{score}\n")
file.close()

# Copy the content of one file to another.  
file1 = open('students.txt', 'r')
file2 = open('copy.txt', 'w')
for line in file1:
    file2.write(line)
file1.close()
file2.close()

# Count the number of lines, words, and characters in a file.
file = open('students.txt', 'r')
line_count = 0
word_count = 0
char_count = 0
for line in file:
    line_count += 1
    words = line.split()
    word_count += len(words)
    char_count += len(line)
file.close()
print(f"Number of lines: {line_count}")
print(f"Number of words: {word_count}")
print(f"Number of characters: {char_count}")
