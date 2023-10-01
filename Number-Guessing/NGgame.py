import random

number = random.randint(1, 10)

print("Welcome to the NGgame!")
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
                print(f"Nice! You got it!")
                print(f"It took you {attempts} attempts.") 
            if usernum == number:
              play_again =input ("Would you like to play again Yes/No: ")
            if play_again != "Yes":
                 print("It was nice playing with you")
                 break
            else:
                usernum
        except :
            if usernum == ValueError:
               print("Invalid input. Please enter a valid number between 1 and 10.")
        
          


