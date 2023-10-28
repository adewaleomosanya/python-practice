import random
print("Welcome to NGgame")
lowest_attempts = float('inf')
highest_attempts = 0

while True:
        
        number = random.randint(1, 10)
        
        
        attempts = 0

        while True:
            try:
                
                usernum = int(input("Guess a number between 1 and 10: "))
                attempts += 1

                if usernum < number:
                    print("It's lower, try again.")
                elif usernum > number:
                    print("It's higher, try again.")
                else:
                    print(f"Nice! You got it! It took you {attempts} attempts.")
                    
                    lowest_attempts = min(lowest_attempts, attempts)
                    highest_attempts = max(highest_attempts, attempts)
                    break

            except :
                print("Invalid input. Please enter a valid number between 1 and 10.")

        play_again = input("Would you like to play again?Yes/No: ")
        if play_again != 'yes':
            print("It was nice playing with you.")
            print(f"Your Lowest attempt(s) is {lowest_attempts}")
            print(f"Your Highest attempt(s) is {highest_attempts}")
            break


        
