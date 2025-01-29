
import random

def choose_word():
    words = ["apple", "banana", "cherry", "peach", "grape", "orange"]
    return random.choice(words)

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
    strikes = 0
    max_strikes = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while "_" in display_word(word, guessed_letters) and strikes < max_strikes:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print(display_word(word, guessed_letters))
        else:
            strikes += 1
            print("Incorrect guess. You have {} strikes left.".format(max_strikes - strikes))
            print(display_word(word, guessed_letters))

    if "_" not in display_word(word, guessed_letters):
        print("Congratulations! You guessed the word: {}".format(word))
    else:
        print("You ran out of strikes. The word was: {}".format(word))

hangman()
