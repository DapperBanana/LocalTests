
import random

def choose_random_word():
    words = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    word = choose_random_word()
    guessed_letters = []
    lives = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            print(display_word(word, guessed_letters))
            if '_' not in display_word(word, guessed_letters):
                print("Congratulations, you've guessed the word!")
                break
        else:
            lives -= 1
            print("Incorrect guess. You have {} lives remaining.".format(lives))
            if lives == 0:
                print("Game over. The word was '{}'.".format(word))
                break

hangman()
