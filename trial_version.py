
import random

def choose_word():
    words = ['python', 'hangman', 'computer', 'programming', 'player']
    return random.choice(words)

def display_word(word, guesses):
    displayed_word = ''
    for letter in word:
        if letter in guesses:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    return displayed_word

def hangman():
    word = choose_word()
    guesses = []
    attempts = 5

    while attempts > 0:
        print(display_word(word, guesses))
        guess = input('Guess a letter: ')

        if guess in guesses:
            print('You already guessed that letter!')
        elif guess in word:
            guesses.append(guess)
            if '_' not in display_word(word, guesses):
                print('Congratulations! You guessed the word:', word)
                break
        else:
            attempts -= 1
            print('Incorrect guess. You have', attempts, 'attempts left.')

    if attempts == 0:
        print('Sorry, you ran out of attempts. The word was:', word)

hangman()
