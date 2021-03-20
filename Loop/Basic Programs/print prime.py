m = int(input("Enter lower range.\n"))
n = int(input("Enter upper range.\n"))
print("Prime numbers between",m,"and",n,"are:-")
for i in range(m,n+1):
    f = 0
    for j in range(2, (i//2)+1):
        if i % j == 0:
            f = 1
            break
    if f==0:
        print(i)