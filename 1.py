#Write a program to add two integers without + operator
# a = 10
# b = 20

# c = a - (-b)
# print(c)

# list

# # Accessing List Items
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0:2]) # apple
# print(fruits[-1])
# #Modifying List Items
# fruits[1] = "orange"
# print (fruits) # ['apple', 'orange', 'cherry']
# fruits.append("mango")
# print(fruits)
# fruits.insert(1, "kiwi")
# print(fruits)
# fruits.extend(["grapes", "melon"])
# print(fruits)
# fruits.remove("orange")
# print(fruits)
# fruits.pop(1)

# print(fruits)

# fruits.sort()
# print(fruits)

# # Using curly braces
# my_set = {1, 2, 3, 4}
# # Using set() function
# another_set = set([4, 5, 6])
# # Empty set (use set(), not {})
# empty_set = set()
# #Note {} is an empty dictionary not a set

# A = {1,2,3,4}
# B = {3,2,1,6}
# print(A-B)
# print(A^B)
# print(A|B)
# print(A&B)
# sq = {x**2 for x in range(1,11)}
# print(sq)
# sq1 = frozenset(sq)
# try:
#   sq1.add(10)
# except Exception as e:
#   print(e)

# Basic dictionary
student = {
  "name": "Alice",
  "age": 20,
  "course": "Python"
}
# Using dict() constructor
person = dict(name="John", age = 25)
# Empty dictionary
empty_dict={}

print(student)
print(person)
print(empty_dict)

# Accessing values
print(student["name"])
print(student.get("age"))

# Adding or updating values
student["age"] = 21
student["city"] = "New York"
print(student)

# Removing vlaues
del student["city"]
student.clear()
print(student)
