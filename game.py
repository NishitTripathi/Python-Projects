print('Welcome to the Quiz')
question = input("Would you like to take the Quiz? ")
if question.lower() != "yes":
    quit()
else:
    print("Yay Let's Go! :(")
    score = 0
answer = input("What's the full form of CPU? ")
if answer.lower() == "central processing unit":
    print("Corrrect Answer")
    score += 1
else:
    print("Incorrect")

answer = int(input("How many bits are there in x86 Architecture? "))
if answer == 32:
    print("Correct Answer")
    score += 1
else:
    print("Incorrect")

answer = input("What is the full form of RAM? ")
if answer.lower() == "random access memory":
    print("Correct Answer")
    score += 1
else:
    print("incorrect")

answer = input('What is the full form of GPU? ')
if answer.lower() == "graphics processing unit":
    print("Correct Answer")
    score += 1
else:
    print("Incorrect")

print("You answered " + str(score) + "questions correctly!")
print("You got " + str((score / 4) * 100) + "%.")







