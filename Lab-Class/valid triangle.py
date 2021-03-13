a=int(input("Enter side.\n"))
b=int(input("Enter side.\n"))
c=int(input("Enter side.\n"))
if (a+b)>c and (b+c)>a and (c+a)>b:
    print("Triangle is valid.")
else:
    print("Triangle is not valid.")