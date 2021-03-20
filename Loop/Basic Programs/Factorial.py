n = int(input("Enter a number.\n"))
a = n
i=1
f=1
while n>0:
    f=f*i
    i=i+1
    n=n-1
print("Factorial of",a,"is =",f)