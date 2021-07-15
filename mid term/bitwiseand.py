m=list(map(int,input().split()))
n=list(map(int,input().split()))
ls=[m[i] & n[i] for i in range(len(m))]
print(ls)