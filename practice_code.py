
import random

# List of words for the game
words = ["hangman", "python", "programming", "computer", "code", "keyboard"]

# Select a random word from the list
word = random.choice(words)

# Create a list to store the letters guessed by the player
guessed_letters = []

# Create a variable to keep track of the number of incorrect guesses
incorrect_guesses = 0

# Main game loop
while True:
    # Display the current state of the word with underscores for missing letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print(display_word)

    # Ask the player to guess a letter
    letter = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if letter in guessed_letters:
        print("You have already guessed that letter. Try again.")
        continue

    # Add the letter to the list of guessed letters
    guessed_letters.append(letter)

    # Check if the letter is in the word
    if letter in word:
        print("Correct!")
    else:
        print("Incorrect.")
        incorrect_guesses += 1

    # Check if the player has won or lost
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You have won.")
        break
    elif incorrect_guesses >= 6:
        print("You have run out of guesses. The word was:", word)
        break
