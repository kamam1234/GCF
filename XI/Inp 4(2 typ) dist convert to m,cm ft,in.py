#input 4 dist in m, cm , ft , in 
#sum
#print in m, cm and ft, in

m = float(input("Enter distance in meters:"))
cm = float(input("Enter distance in centimeters:"))
f = float(input("Enter distance in feet:"))
i = float(input("Enter distance in inches:"))

tcm = (m * 100) + cm
tin = (f * 12) + i
tincm = tin * 2.54
tdist = tincm + tcm

print("Total Dist in Meters:", tdist // 100)
print("Total Dist in Centimeters:", tdist % 100)
print("Total Dist in Feet:", (tdist / 2.54) // 12)
print("Total Dist in Inches:", (tdist // 2.54))
