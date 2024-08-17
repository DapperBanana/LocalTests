
import random

def choose_word():
    words = ['apple', 'banana', 'cherry', 'orange', 'grape', 'kiwi', 'melon', 'peach']
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
    num_wrong_guesses = 0

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while num_wrong_guesses < 6:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            print(display_word(word, guessed_letters))
        else:
            num_wrong_guesses += 1
            print("Wrong guess! You have {} guesses remaining.".format(6 - num_wrong_guesses))
            print(display_word(word, guessed_letters))

        if '_' not in display_word(word, guessed_letters):
            print("Congratulations, you guessed the word!")
            break

    if num_wrong_guesses == 6:
        print("Sorry, you ran out of guesses. The word was {}.".format(word))

hangman()
