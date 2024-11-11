name = input("Enter your name ")
print("Welcome", name, "to the Adventure Game")
answer = input("You are on a dirt road and slowly you are approaching a dead end. You have two directions to move ahead in the game either left or right. Which one do you choose (left/right)? ").lower()
if answer == "left":
    left1 = input("Hmm, so you have chosen the left turn. Now you walk ahead and you see a river. You have two options to cross this river either swim through the river or walk across the river. Which option will you choose (swim/walk)? ").lower()
    if left1 == "swim":
        print("You started swimming in the water and an alligator appeared and you lost the game!")

    elif left1 == "walk":
        print("You walked many miles and eventually ran out of water and lost the game!")

    else:
        print("Not a valid input. You Lose!")

elif answer == "right":
    right1 = input("Hmm, so you have chosen the right turn. Now you see an old bridge which is wobbling. You have two options either to cross the bridge or to go back to the main road. Which option will you choose (cross/back)? ").lower()
    if right1 == "cross":
        print("You crossed the bridge and reached the endpoint.")
        print ("Congratulations you won this Adventure!")
    
    elif right1 == "back":
        print("You started walking back to the main road but a truck hit you in the middle and you lost the game!")

    else:
        print("Not a valid input. You Lose!")

else:
    print("Not a valid input. You Lose!")

print("Thanks for trying", name + ".")



