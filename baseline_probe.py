
import random

def choose_word():
    words = ['python', 'java', 'ruby', 'javascript', 'html', 'css']
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
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("The word has {} letters.".format(len(word)))

    while attempts > 0:
        print("\nAttempts left: {}".format(attempts))
        print(display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You have already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            if word == display_word(word, guessed_letters):
                print("\nCongratulations! You guessed the word: {}".format(word))
                break
        else:
            attempts -= 1
            print("Incorrect guess!")

    if attempts == 0:
        print("\nOut of attempts! The word was: {}".format(word))

hangman()
