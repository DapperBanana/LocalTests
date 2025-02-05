
import random

# List of words to choose from
words = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "melon", "peach"]

# Function to choose a random word from the list
def choose_word(words):
    return random.choice(words)

# Function to display the current state of the word with hidden letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

# Function to check if the player has guessed the word
def check_win(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

# Main game function
def hangman():
    word = choose_word(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("Attempts left: ", attempts)
        print(display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess.")
        
        if check_win(word, guessed_letters):
            print("Congratulations! You've guessed the word:", word)
            break
    
    if attempts == 0:
        print("Sorry, you've run out of attempts. The word was:", word)

# Start the game
hangman()
