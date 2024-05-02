
import random

def choose_word():
    words = ["apple", "banana", "cherry", "orange", "pear"]
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
    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            if set(guessed_letters) == set(word):
                print("Congratulations, you guessed the word:", word)
                break
        else:
            attempts -= 1
            if attempts == 0:
                print("Sorry, you're out of attempts. The word was:", word)
            else:
                print("Incorrect guess. You have", attempts, "attempts remaining.")
    
    play_again = input("Play again? (yes/no): ")
    if play_again.lower() == "yes":
        hangman()
    else:
        print("Thanks for playing!")

hangman()
