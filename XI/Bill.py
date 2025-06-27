uc = int(input("Enter the units consumed: "))

if uc >= 0 and uc <201:
    b = 0
elif uc >200 and uc < 300:
    b = (uc%200) * 0.5
elif uc > 300 and uc <400:
    b = (uc * 0.5) + ((uc%100)*0.75)
else:
    b = ((uc * 0.5) + ((uc%100)*0.75)) + ((uc%200) * 0.5) + ((uc%100)*1)

    
if b == 0:
    tot = 50
else:
    tot = b + (b*0.2)



print("\n\tUnits Consumed: ", uc)
print("\n\tThe total bill is: Rs.", tot)