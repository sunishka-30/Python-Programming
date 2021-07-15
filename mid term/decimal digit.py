n=(input())
for i in range (0,len(n)):
  if n[i]==".":
     c=i+1
     x=len(n)-c
     print(x)
     break
else:
  print("0")