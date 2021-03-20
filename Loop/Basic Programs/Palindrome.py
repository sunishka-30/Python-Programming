n = int(input("Enter a number.\n"))
p=n
r=0
while n>0:
    rem = n%10
    r = r*10+rem
    n=n//10
if p==r:
    print(p,"is a palindrome no.")
else:
    print(p,"is not a palindrome no.")