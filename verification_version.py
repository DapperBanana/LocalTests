
import random

def choose_word():
    words = ["python", "hangman", "coding", "computer", "program"]
    return random.choice(words)

def display_word(word, guesses):
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guesses = []
    lives = 6

    print("Welcome to Hangman!")
    while lives > 0:
        print("\nWord:", display_word(word, guesses))
        print("Lives:", lives)

        letter = input("Guess a letter: ").lower()

        if letter in guesses:
            print("You already guessed that letter!")
        elif letter in word:
            guesses.append(letter)
            if set(word) == set(guesses):
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            print("Incorrect guess!")
            lives -= 1

    if lives == 0:
        print("\nGame over! The word was:", word)

hangman()
