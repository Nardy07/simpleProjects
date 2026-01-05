import random

userName= input("Welcome to the Word Guessing Game. What is your name? ")
print(f"Good luck, {userName}!!")
print("🎉🎉🎉")
#list of words
words = ['Carry', 'Pants', 'Honey', 'Empty', 'Apple', 'Brief', 'Rhythm', 'Fable', 'Syrup', 'Knife', 'Boxer', 'Human', 'Pride']

#select a random word and store in word
word = random.choice(words)
word = word.lower()
print("Guess the characters!!")

yourGuesses = ''
turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in yourGuesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You win!!")
        print(f"The word was {word}. Thanks for playing!")
        break
    print()
    guess = input("Enter a word: ")
    yourGuesses += guess
    if guess not in word:
        print("WRONG!")
        turns -=1
        print(f"You now have {turns} left.")

        if turns == 0:
            print("You lost brate!")