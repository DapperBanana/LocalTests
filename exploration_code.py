
import random

def choose_word():
    words = ["apple", "banana", "cherry", "grape", "orange", "kiwi", "melon"]
    return random.choice(words)

def display_word(word, guesses):
    displayed_word = ""
    for letter in word:
        if letter in guesses:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def hangman():
    word = choose_word()
    guesses = []
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while True:
        displayed = display_word(word, guesses)
        print(displayed)
        
        if "_" not in displayed:
            print("Congratulations! You've guessed the word:")
            print(word)
            break
        
        if attempts == 0:
            print("Sorry, you've run out of attempts.")
            print("The word was:", word)
            break
            
        print("Attempts left:", attempts)
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guesses:
            print("You've already guessed that letter.")
            continue
        
        guesses.append(guess)
        
        if guess not in word:
            attempts -= 1
            print("Incorrect guess!")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing!")

hangman()
