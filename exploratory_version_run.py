
import random

def choose_word():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grapefruit", "honeydew", "jackfruit", "kiwi", "lemon", "mango", "nectarine"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters= []
    turns = 6

    print("Welcome to Hangman!")
    while turns > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You have already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You guessed the word: " + word)
                break
        else:
            print("Incorrect!")
            turns -= 1
            print("You have {} turns left.".format(turns))
    else:
        print("\nGame over! The word was: " + word)

hangman()
