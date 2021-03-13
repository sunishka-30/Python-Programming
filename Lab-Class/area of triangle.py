import math
a=int(input("Enter side.\n"))
b=int(input("Enter side.\n"))
c=int(input("Enter side.\n"))
sp = (a+b+c)/2
area = math.sqrt(sp*(sp-a)*(sp-b)*(sp-c))
print("Area = {:.2f}".format(area))


