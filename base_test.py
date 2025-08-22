
import random

# List of words to choose from
words = ["apple", "banana", "cherry", "grape", "kiwi", "orange", "peach", "pear"]

# Function to choose a random word
def choose_word():
    return random.choice(words)

# Function to display the current state of the word with blanks for unguessed letters
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

# Function to play the game
def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the fruit:")
    
    while True:
        print(display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.append(guess)
            if all(letter in guessed_letters for letter in word):
                print(display_word(word, guessed_letters))
                print("Congratulations! You guessed the word.")
                break
        else:
            attempts -= 1
            if attempts == 0:
                print("Out of attempts! The word was:", word)
                break
            else:
                print("Incorrect guess. You have", attempts, "attempts remaining.")
    
    play_again = input("Play again? (y/n): ")
    if play_again.lower() == 'y':
        hangman()
    else:
        print("Thanks for playing!")

hangman()
