
import random

words = ['apple', 'banana', 'cherry', 'dog', 'elephant', 'frog', 'grape', 'horse', 'igloo', 'jaguar']

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0 and '_' in display_word(word, guessed_letters):
        guess = input("Please enter a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print("Incorrect guess. You have {} attempts remaining.".format(attempts))

        print(display_word(word, guessed_letters))

    if '_' not in display_word(word, guessed_letters):
        print("Congratulations, you've won!")
    else:
        print("Sorry, you've run out of attempts. The word was '{}'.".format(word))

hangman()
