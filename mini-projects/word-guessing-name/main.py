import random

words = ["mandarin", "python", "badminton", "mahjong", "japanese"]

word = random.choice(words)

print("Guess the characters")

guesses = ""  # Empty string that holds all the characters guessed by the user
turns = 12  # The number of attempts the user has to guess the word. Initially set to 3

while turns > 0:  # while loop runs as long as the user has remaining turns

    failed = 0  # A counter for the number of characters that have not been correctly guessed

    for char in word:

        if char in guesses:
            print(char, end=" ")

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You win")
        print("The word is: ", word)
        break

    print()
    guess = input("Guess a character: ")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("Wrong")
        print("You have", + turns, "more guesses")

        if turns == 0:
            print("You lose")