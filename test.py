
import random

def choose_word():
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while True:
        print("Attempts left: ", attempts)
        print(display_word(word, guessed_letters))

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations, you guessed the word!")
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess.")

            if attempts == 0:
                print("Out of attempts! The word was:", word)
                break

hangman()
