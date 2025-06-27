a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
print(a)
print(b)
c = a + b
print(c)
i = 1
while i <=1000:
    a, b = b, c
    c = a + b
    print(c)
    i += 1