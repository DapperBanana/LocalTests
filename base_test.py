
import random

def choose_word():
    words = ["python", "hangman", "computer", "programming", "game", "hello", "world"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman! Try to guess the word.")
    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            if word == display_word(word, guessed_letters):
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            attempts -= 1
            print("Incorrect guess. You have", attempts, "attempts left.")
    
    if attempts == 0:
        print("\nGame over! The word was:", word)

hangman()
