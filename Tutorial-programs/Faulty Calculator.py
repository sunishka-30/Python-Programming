n1 = int(input("Enter first number."))
n2 = int(input("Enter second number."))
ch = input("Enter operation to be performed.")
if n1==45 and n2==3 and ch=="*":
    print("555")
elif n1==56 and n2==9 and ch=="+":
    print("77")
elif n1==56 and n2==6 and ch=="/":
    print("4")
elif ch=="+":
    print(n1 + n2)
elif ch == "-":
    print(n1 - n2)
elif ch=="*":
    print(n1 * n2)
elif ch=="/":
    print(n1 / n2)
else:
    print("Invalid operator.")