
import random

def choose_word():
    word_list = ["apple", "banana", "cherry", "grape", "kiwi", "orange", "peach", "pear", "strawberry", "watermelon"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Guesses remaining:", attempts)
        
        guess = input("Enter a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.append(guess)
            if set(word) == set(guessed_letters):
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            guessed_letters.append(guess)
            attempts -= 1
            if attempts == 0:
                print("\nGame over! The word was:", word)
                break

hangman()
