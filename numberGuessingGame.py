import random

print("Hello, welcome to the Guessing game!!!")

#asking the user for the high and low bounds
upperBound = int(input("Please enter the upper bound: "))
lowerBound = int(input("Please enter the lower bound: "))

#generating a random number
randomNumber = random.randint(lowerBound,upperBound)

print("You have 7 guesses to correctly guess the number!!")

guessCount = 0
chances = 7

while guessCount < chances: 
    guessCount += 1
    guess = int(input("Enter your guess: "))

    #if/else now
    if guess == randomNumber:
        print(f"Congratulations, you correctly guessed the number in {guessCount} chances!!")
        break
    elif guessCount >= chances and guess != randomNumber:
        print(f"Sorry the number was {randomNumber}. Better luck next time.")
    elif guess > randomNumber:
        print("Your guess is too high!!")
    elif guess < randomNumber:
        print("Your guess is too low!!") 