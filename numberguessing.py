import random
print ("Welcome to number guessing game!!!")
number = random.randint(1,100)

while True:
    guess = int(input("Enter a number between 1 to 100: "))
    if guess == number:
        print("Congratulations! You guessed the number!")
        break
    elif guess > number:
        print("Too High!")
    elif guess < number:
        print("Too Low!")
    else:
        print("Please enter a valid number")
