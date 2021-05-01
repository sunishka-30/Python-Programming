m=int(input())
n=int(input())
p=int(input())
q=int(input())
l1=[[int(input("enter element of matrix 1 ")) for i in range(n)] for j in range(m)]
l2=[[int(input("enter element of matrix 2 ")) for i in range(q)] for j in range(p)]
l3=[]
if n==p:
	for i in range (m):
		l=[]
		for j in range(q):
			s=0
			for k in range(n):
				s=s+l1[i][k]*l2[k][j]
			l.append(s)
		l3.append(l)

	for i in range (m):
		for j in range (q):
			print(l3[i][j],end="  ")
		print()
else:
	print("cant multiply")