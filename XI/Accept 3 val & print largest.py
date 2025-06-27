n1 = int(input("Enter 1st Number: "))
n2 = int(input("Enter 2nd Number: "))
n3 = int(input("Enter 3rd Number: "))

# if n1 > n2:
#     if n1 > n3:
#         m = n1
#     else:
#         m = n3
# else:
#     if n2 > n3:
#         m = n2
#     else:
#         m =n3
      
m = n1

if n2 > m:
    m = n2
if n3 > m:
    m = n3
print("\tLargest Value is:",m)