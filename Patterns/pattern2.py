n = int(input("Enter a no.\n"))
for i in range (n):
   for j in range (n):
       if j==0 or j==n-1 or i==0 or i==n-1:
        print("0",end='')
       else:
        print(" ",end='')
       j=j+1
   i=i+1
   print()
