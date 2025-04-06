
import random

# List of words for the player to guess
words = ['python', 'hangman', 'programming', 'computer', 'keyboard', 'internet']

def hangman():
    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    tries = 6

    print("Welcome to Hangman!")
    print("The word has {} letters".format(len(word)))

    while True:
        # Display current progress
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(display_word)

        # Ask the player for a letter
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            print("Correct!")
            guessed_letters.append(guess)
        else:
            print("Incorrect guess!")
            incorrect_guesses += 1

        # Check if player has won
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word: {}".format(word))
            break

        # Check if player has lost
        if incorrect_guesses >= tries:
            print("You are out of tries! The word was: {}".format(word))
            break

hangman()
