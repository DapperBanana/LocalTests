
import random

def choose_random_word():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    word = choose_random_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess! You have {} attempts left.".format(attempts))

        print(display_word(word, guessed_letters))

        if set(word) == set(guessed_letters):
            print("Congratulations! You guessed the word.")
            break

        if attempts == 0:
            print("Game over! The word was: {}".format(word))
            break

if __name__ == "__main__":
    hangman()
