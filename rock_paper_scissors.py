import random

user_wins = 0
computer_wins = 0
draws = 0

options = ["rock", "paper", "scissors"]

play = input("Would you like to play Rock Paper & Scissors against Computer? ")
if play.lower() == "yes":
        print("Yay Let's Go!")

else:
    print("Goodbye")
    quit()

while True:

    user_pick = input("Pick Rock/Paper/Scissors or press Q to exit ").lower()
    if user_pick == "q":
        break

    elif user_pick not in options:
        print("Your input is Invalid!")
        continue

    choice = random.randint(0,2)
    computer_pick = options[choice]
    print("Computer picked ", computer_pick + ".")
    
    if user_pick == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1

    elif user_pick == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1

    elif user_pick == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1

    elif user_pick == "rock" and computer_pick == "rock":
        print("It's a Draw!")
        print("Pick Again")
        draws += 1
        continue

    elif user_pick == "paper" and computer_pick == "paper":
        print("It's a Draw!")
        print("Pick Again")
        draws += 1
        continue

    elif user_pick == "scissors" and computer_pick == "scissors":
        print("It's a Draw!")
        print("Pick Again")
        draws += 1
        continue

    else:
        print("You Lost!")
        computer_wins += 1

    
print("Thanks for playing!")
print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("There were", draws, "Draws.")
print("Goodbye!")




