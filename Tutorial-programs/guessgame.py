n = 20
g = 10
while(g>0):
    a = int(input("Guess the no.\n"))
    if a<n:
        print("Your guess is lesser than the actual no.")
        print("Guesses left =",g-1)
    elif a>n:
        print("Your guess is greater than the actual no.")
        print("Guesses left =", g-1)
    else:
        print("You guessed right.")
        print("You guessed in ",10-g+1,"guesses")
        break
    g = g-1
