n = int(input("Enter a number.\n"))
c=0
if (n>0):
    while(n!=1):
     if n%2==0:
        n=n//2
        c=c+1
        print(n)
     else:
        n=n*3+1
        c=c+1
        print(n)
    print("No. of Steps =",c)
else:
  print("Invalid Input.")
