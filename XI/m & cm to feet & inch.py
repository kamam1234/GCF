m = float(input("Enter distance in meters:"))
cm = float(input("Enter distance in centimeters:"))

tcm  = (m *100) + cm
tin = tcm / 2.54

f = tin // 12
i = tin % 12

print()
print("Dist in Meters: ", m)
print("Dist in Centimeters: ", cm)
print("\tDist in Feet: ", f)
print("\tDist in Inches: ", i)
