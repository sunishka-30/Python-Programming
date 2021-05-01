r,c=map(int,(input("Enter row and column").split()))
m1=[[int(input("Element of matrix 1:")) for j in range(c)] for i in range (r)]
m2=[[int(input("Element of matrix 2:")) for j in range(c)] for i in range (r)]
m3=[[m1[i][j]+m2[i][j] for j in range(c)] for i in range(r)]
print("Matrix 1:")#just for visual representation in matrix form
for i in range(r):
    for j in range(c):
        print('{:4}'.format(m1[i][j]),end=' ')
    print()
print("Matrix 2:")#just for visual representation in matrix form
for i in range(r):
    for j in range(c):
        print('{:4}'.format(m2[i][j]),end=' ')
    print()


print("Addition matrix:")
for i in range(r):
    for j in range(c):
        print('{:4}'.format(m3[i][j]),end=' ')
    print()

