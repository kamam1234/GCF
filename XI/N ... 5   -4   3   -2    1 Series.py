n = int(input("Enter N:"))
for i in range(n,0,-1):
    if i%2==0:
        print(-i,end="    ")
    else:
        print(i,end="   ")