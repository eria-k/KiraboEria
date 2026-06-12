secret_number = 42
count = 0
while count < 3:
    guess = int(input("Guess the secret number: "))
    if guess == secret_number:
        print("Congratulations! You've guessed the number!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    count += 1
if count == 3:
    print("Sorry, you've used all your guesses. The secret number was:", secret_number)
