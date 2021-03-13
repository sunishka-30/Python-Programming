n = int(input("Enter the no.\n"))
if n%3==0:
    if n%5==0:
        print("Tic Tac")
    else:
        print("Tic")
elif n%5==0:
    print("Tac")

