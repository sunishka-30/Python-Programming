n = int(input("Enter a number.\n"))
c=0
a=n
m=n
r=0
while n>0:
    n=n//10
    c=c+1
while a>0:
    rem=a%10
    r = r+pow(rem,c)
    a=a//10
if r==m:
    print(m,"is a armstrong no.")
else:
    print(m,"is not a armstrong no.")