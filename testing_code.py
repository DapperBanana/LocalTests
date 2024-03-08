
import random

def choose_word():
    words = ['python', 'hangman', 'computer', 'programming', 'code', 'developer']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    lives = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            lives -= 1
            print("Incorrect guess. You have {} lives remaining.".format(lives))
        
        if '_' not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word: {}".format(word))
            break
        
        if lives == 0:
            print("You ran out of lives. The word was: {}".format(word))
            break

        print(display_word(word, guessed_letters))

hangman()
