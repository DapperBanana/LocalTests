
import random

# List of words for the game
words = ['python', 'hangman', 'programming', 'computer', 'coding', 'software', 'algorithm']

def choose_word():
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
    attempts = 6
    game_over = False

    print("Welcome to Hangman!")
    
    while not game_over:
        print("\nAttempts left:", attempts)
        print("Word:", display_word(word, guessed_letters))
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word:
            print("Incorrect guess!")
            attempts -= 1
            if attempts == 0:
                print("\nSorry, you ran out of attempts. The word was:", word)
                game_over = True
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations, you guessed the word:", word)
            game_over = True

if __name__ == "__main__":
    hangman()
