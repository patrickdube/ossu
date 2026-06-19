# Bisection
square = int(input("Enter your square: "))
lowerBound = 0
higherBound = square
guess = (lowerBound + higherBound) / 2
epsilon = 0.01
numGuesses = 0

while abs(guess**2 - square) >= epsilon:
    if guess**2 < square:
        lowerBound = guess
    elif guess**2 > square:
        higherBound = guess
    guess = (lowerBound + higherBound) / 2
    numGuesses += 1
    print(numGuesses)
    print(guess)
