import random
print ("Welcome to number guessing game!!!")
number = random.randint(1,100)

while True:
    try:
        guess = int(input("Guess the number between 1 and 100 "))
        if guess > number:
            print("Too High!")
        elif guess < number:
            print("Too Low!")
        else:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid input")
        

        
