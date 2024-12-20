
import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "coding"]
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
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word:
            attempts -= 1
            print("Incorrect guess!")
        
        if display_word(word, guessed_letters) == word:
            print("\nCongratulations! You guessed the word:", word)
            break
        
        if attempts == 0:
            print("\nGame over! The word was:", word)
            break

if __name__ == "__main__":
    hangman()
