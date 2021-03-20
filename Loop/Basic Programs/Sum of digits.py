n = int(input("Enter a number.\n"))
s=0
a=n
while n>0:
    rem = n%10
    s = s+rem
    n=n//10
print("Sum of digits of",a,"is =",s)