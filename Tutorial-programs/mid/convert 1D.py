l = eval(input())
c=input()
r=int(c[0])
c=int(c[2])
if r*c==len(l):
    k=0
    for i in range(r):
        for j in range(c):
            print(l[k],end=" ")
            k=k+1
        print()
else:
    print("Invalid")