from random import randint

randomNumber = randint(1, 100)
guessNumber = 0
numberOfChances = 10
print("You have " + str(numberOfChances) + " chances to pick a number  between 1 and 100: ")

for guessNumber in range(1, int(numberOfChances ) + 1):
    print("Enter a number between 1 and 100: ")
    userGuess = int( input())
    guessNumber += 1
    
    if(userGuess > randomNumber):
        print("Too high")
        print("Your last guess: " + str(userGuess))
        print(str(numberOfChances - guessNumber) + " guesses left")
    elif(userGuess < randomNumber):
            print("Too low")
            print("Your last guess: " + str(userGuess))
            print(str(numberOfChances - guessNumber) + " guesses left")
    else:
        print("Congrats, you picked the right number.")
        
print(randomNumber)
