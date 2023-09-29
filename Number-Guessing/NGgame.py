import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    play_again = "yes"
    
    while play_again.lower() == "yes":
        secret_number = random.randint(1, 10)
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
        
        play_again = input("Would you like to play again? (Enter Yes/No): ")
    
    print("Thanks for playing!")

#if __name__ == "__main__":
    #number_guessing_game()
