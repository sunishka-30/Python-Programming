import math
L=[ ]
while(True):
 n=int(input())

 if n==0:
    break
 L.append(n)

for n in L:
  p=math.sqrt(n)

  if p==int(p):
     print("yes")
  else:
     print("no")
