import random
print ("Welcome to Dice Game!!!")

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print("Your respective rolls are " f'({die1}, {die2})')
    elif choice == "n":
        print("Thanks for playing. See ya again!")
        break
    else:
        print("Invalid Input!")