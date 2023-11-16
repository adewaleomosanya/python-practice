import random
import os

def roll_dice(num_of_dice):
    results = []
    for i in range(num_of_dice):
        results.append(random.randint(1, 6))
    return results

while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print("Dice Roll Generator")
        user_choice = input("Choose between rolling 1 or 2 dice (Enter '1' or '2'): ")
        
        if user_choice in ['1', 'one']:
            num_of_dice = 1
        elif user_choice in ['2', 'two']:
            num_of_dice = 2
        else:
            print("Invalid choice. Please choose '1' or '2'.")
            continue

        results = roll_dice(num_of_dice)
        print(f"Result of rolling {num_of_dice} dice: {results}")

        play_again = input("Roll again? (Enter 'yes' or 'no'): ").lower()
        if play_again != 'yes':
            print("Thanks for rolling the dice!")
            break

