import random
print("Welcome to Rock,Paper,Scissors game")
def play_game():
  userinput = input("Choose rock (r), paper (p), or scissors (s): ").lower()
    
  if userinput not in ('r', 'p', 's'):
        print("Invalid choice. Please choose 'r', 'p', or 's'.")
        return
    
  choices = ['r', 'p', 's']
  mychoice = random.choice(choices)

  print(f"I chose {mychoice}")
  print(f"You chose {userinput}")
  if userinput == mychoice:
      print(f"It's a tie")
  elif (userinput == 'r' and mychoice == 's') or (userinput == 'p' and mychoice == 'r') or (userinput == 's' and mychoice == 'p'):
      print(f"You won")
  else :
      print(f"I won!, You lost")
while True:
   play_game()
   play_again = input("Play again? (Enter 'yes' or 'no'): ")
   if play_again != 'yes':
      print("Thanks for playing!It was nice playing with you")
      break


