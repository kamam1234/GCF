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

