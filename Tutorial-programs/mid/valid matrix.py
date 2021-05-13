a=eval(input())
c=0
b=len(a[0])
for i in range(1,len(a)):
    if len(a[i])!=b:
        c=1;break
if c==1:
    print("invalid")
else:
    print("valid")