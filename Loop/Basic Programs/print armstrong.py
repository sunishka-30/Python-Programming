m = int(input("Enter lower range.\n"))
n = int(input("Enter upper range.\n"))
print("Armstrong numbers between",m,"and",n,"are:-")
for i in range(m,n+1):
    c = 0
    a = i
    p = i
    r = 0
    while i > 0:
        i = i // 10
        c = c + 1
    while a > 0:
        rem = a % 10
        r = r + pow(rem, c)
        a = a // 10
    if r == p :
        print(r)