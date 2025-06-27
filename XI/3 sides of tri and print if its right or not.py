s1 = int(input("Enter the 1st side: "))
s2 = int(input("Enter the 2nd side: "))
s3 = int(input("Enter the 3rd side: "))

ss1 = s1 ** 2
ss2 = s2 ** 2
ss3 = s3 ** 2


if (ss1 + ss2 == ss3) or (ss1 + ss3 == ss2) or (ss2 + ss3 == ss1):
    print("It is a Right Triangle")
else:
    print("It is not a Right Triangle")