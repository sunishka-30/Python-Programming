L=[ ]
while(True):
 n=int(input())

 if n==0:
    break
 L.append(n)

for n in L:
  c=0

  for i in range(1,n+1):
     d = n

     if d%i==0:
         c=c+1

  if c%2==0:
     print("no")
  else:
     print("yes")