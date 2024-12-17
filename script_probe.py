
import random

def choose_word():
    words = ['hangman', 'python', 'programming', 'challenge', 'computer']
    return random.choice(words)

def display_word(word, guesses):
    displayed_word = ''
    for letter in word:
        if letter in guesses:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    word = choose_word()
    guesses = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word: " + display_word(word, guesses))

    while True:
        guess = input("Enter a letter: ").lower()

        if guess in guesses:
            print("You've already guessed that letter. Try again.")
        else:
            guesses.append(guess)
            if guess in word:
                print("Correct!")
            else:
                attempts -= 1
                print("Incorrect! You have", attempts, "attempts left.")

        print(display_word(word, guesses))

        if '_' not in display_word(word, guesses):
            print("Congratulations! You've guessed the word:", word)
            break

        if attempts == 0:
            print("You've run out of attempts. The word was:", word)
            break

if __name__ == '__main__':
    hangman()
