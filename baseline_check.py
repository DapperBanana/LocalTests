
import random

def choose_word():
    words = ['python', 'hangman', 'program', 'computer', 'coding']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    while True:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess. {} attempts remaining.".format(attempts))
            if attempts == 0:
                print("You ran out of attempts. The word was '{}'.".format(word))
                break

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word '{}'. You win!".format(word))
            break

if __name__ == "__main__":
    hangman()
