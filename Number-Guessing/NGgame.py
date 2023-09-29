import random

secret_number = random.randint(1, 10)

print("Welcome to the NGgame!")
attempts = 0

while True:
    try:
        user_guess = int(input("Guess the number between 1 and 10: "))
        attempts += 1

        if user_guess < secret_number:
            print("It's lower, try again.")
        elif user_guess > secret_number:
            print("It's higher, try again.")
        else:
            print(f"Nice! You got it!")
            print(f"It took you {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 10.")
