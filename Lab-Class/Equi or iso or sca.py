a=int(input("Enter side.\n"))
b=int(input("Enter side.\n"))
c=int(input("Enter side.\n"))
if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or c == a:
    print("Isoceles Triangle")
else:
    print("Scalene Triangle")

