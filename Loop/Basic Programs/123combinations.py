print("Six Combinations of 123 with distinct numbers are :-")
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            if i==j or j==k or k==i:
                continue
            print(i, j, k, sep='')