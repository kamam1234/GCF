gs = int(input("Enter your Salary: "))
ta = 5000
da = gs * 0.2
pf = gs * 0.12

if gs >= 0 and gs <= 500000:
    t = 0
elif gs > 500000 and gs <= 750000:
    t = 0.1
elif gs > 750000 and gs <= 1000000:
    t = 0.2
else:
    t = 0.3
    
tax = gs * t


ns  = gs + ta + da - pf - tax

print("\nGross Salary:       Rs.", gs)
print("Travel Allowance:   Rs.", ta)
print("Dearness Allowance: Rs.", da)
print("PF:                 Rs.", pf)
print("Tax:                Rs.", pf)
print("\t\tNet Salary: Rs.", ns)