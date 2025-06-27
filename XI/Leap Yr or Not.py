"""
Created on Thu Aug 25 14:55:34 2022
Leap Year or Not
@author: AMD Ryzen
"""
yr = int(input("Enter a Year:"))
if (yr % 1000 == 0) or (yr % 100 != 0) and (yr % 4 == 0):
    print(yr, "is a leap year.")
else:
    print(yr, "is not a leap year.")