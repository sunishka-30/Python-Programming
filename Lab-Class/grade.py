a = int(input("Enter the marks of 1st subject.\n"))
b = int(input("Enter the marks of 2nd subject.\n"))
c = int(input("Enter the marks of 3rd subject.\n"))
per = ((a+b+c)/300)*100
print("{:.2f}".format(per))
if per>=90:
    print("A+")
elif per>=80:
    print("A")
elif per>=70:
    print("B+")
else:
    print("Average")


