a=int(input("Enter first no.\n"))
b=int(input("Enter second no.\n"))
m = max(a,b)
while(True):
    if m%a==0 and m%b==0:
        lcm = m
        break
        m=m+1
print(lcm)