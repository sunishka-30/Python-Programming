a = int(input("Enter 1st no.\n"))
b = int(input("Enter 2nd no.\n"))
c = int(input("Enter 3rd no.\n"))
print(max(a,b,c),"is largest.")
if a>=b and a>=c:
    print(a,"is largest.")
elif b>=a and b>=c:
    print(b, "is largest.")
elif c >= a and c >= b:
    print(c, "is largest.")
if a>=b:
    if a>=c:
        print(a,"is largest.")
    else:
        print(c, "is largest.")
else:
    if b>=c:
        print(b, "is largest.")
    else:
        print(c, "is largest.")
