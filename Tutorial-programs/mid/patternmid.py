n = int(input("Enter no. of rows.\n"))
for i in range(1,n//2+1):
    print(('*'*i).ljust(n//2+1),'*'*i,sep=' ')
for i in range(1,n//2+1):
    print(('*' * i).ljust(n // 2 + 1), '*' * i, sep=' ')