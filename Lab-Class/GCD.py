a=int(input("Enter first no.\n"))
b=int(input("Enter second no.\n"))
c=0
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
    c=c+1

print("GCD of",a,"and",b,"=",gcd)
print("No. of steps =",c)