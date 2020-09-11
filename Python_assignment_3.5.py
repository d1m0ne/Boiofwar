Numberguess = 8

print("guess the number!")

guess = input()

while int(Numberguess) != int(guess):
    if int(Numberguess) > int(guess):
        print("Your number is too low, guess again!")
    elif int(Numberguess) < int(guess):
        print("Your number is too high, guess again!")
    guess = input()

print("You guessed the number!")