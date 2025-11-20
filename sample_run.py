
import random

def choose_word():
    words = ['apple', 'banana', 'cherry', 'orange', 'pear']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

def game():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts = 6
    
    while True:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ")
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.append(guess)
            if set(word) == set(guessed_letters):
                print(f"Congratulations! You guessed the word '{word}'. You win!")
                break
        else:
            attempts -= 1
            print(f"Incorrect guess. You have {attempts} attempts left.")
            if attempts == 0:
                print(f"Sorry, you're out of attempts. The word was '{word}'. Game over!")
                break
                
    play_again = input("Would you like to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        game()
    else:
        print("Thanks for playing!")

game()
