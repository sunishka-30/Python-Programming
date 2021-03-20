m = int(input("Enter lower range.\n"))
n = int(input("Enter upper range.\n"))
print("Palindrome numbers between",m,"and",n,"are:-")
for i in range(m,n+1):
    p = i
    r = 0
    while i > 0:
        rem = i % 10
        r = r * 10 + rem
        i = i // 10
    if p == r:
        print(p)