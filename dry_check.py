
import random

def get_word():
    word_list = ["python", "hangman", "computer", "programming", "code"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    word = get_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess. You have {} attempts left.".format(attempts))
        else:
            print("Good guess!")
        
        print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word: {}".format(word))
            break

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was: {}".format(word))

hangman()
