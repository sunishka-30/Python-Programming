c,r=map(int,(input("Enter row and column").split()))
m1=[[int(input("Element of matrix 1:")) for j in range(c)] for i in range (r)]
print("Original matrix :")
for i in range(r):
    for j in range(c):
        print('{:4}'.format(m1[i][j]),end=' ')
    print()


print("Transpose matrix:")
for i in range(r):
    for j in range(c):
        print('{:4}'.format(m1[j][i]),end=' ')
    print()

