items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for i in items:
    if str(i).isnumeric() and i>=6:
        print(i)
