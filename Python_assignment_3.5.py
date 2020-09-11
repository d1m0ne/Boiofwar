Numberguess = 8

print("guess the number!")

guess = input()

while int(Numberguess) != int(guess):
    print("guess again!")
    guess = input()

print("You guessed the number!")