h1 = int(input("Enter Hours of 1st Duration:"))
m1 = int(input("Enter Minutes of 1st Duration:"))
h2 = int(input("Enter Hours of 2nd Duration:"))
m2 = int(input("Enter Minutes of 2nd Duration:"))

sh = h1 + h2
sm = m1 + m2


sh += (sm //60)
sm = sm % 60

print("First Duration is: ", h1, ":", m1, sep = "")
print("Second Duration is: ", h2, ":", m2, sep = "")
print("Total Duration is: ", sh, ":", sm, sep = "")