# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:07:01 2022
Total, Avg, Status of 3 sub (out of 100)
@author: AMD Ryzen
"""

s1 = int(input("Enter the marks of 1st subject: "))
s2 = int(input("Enter the marks of 2nd subject: "))
s3 = int(input("Enter the marks of 3rd subject: "))

tot = s1 + s2 + s3
avg = tot/3

if (s1 >=33) and (s2 >=33) and (s3 >=33):
    st = "Pass"
else:
    st  = "Fail"

if st == "Fail":
    gr = "***"
elif avg >= 75:
    gr ="A"
elif avg >= 60:
    gr = "B"
elif avg >= 40:
    gr  = "C"
else:
    gr = "D"


print("Total Marks: ", tot)
print("Avg Marks: ",avg)
print("Status: ",st)
print("Grade: ",gr)