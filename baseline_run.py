
import random

def get_word():
    words = ['python', 'hangman', 'program', 'computer', 'coding']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def main():
    word = get_word()
    guesses = 6
    guessed_letters = []
    
    print("Welcome to Hangman!")
    
    while True:
        print("\nWord: ", display_word(word, guessed_letters))
        print("Guesses left: ", guesses)
        guess = input("Enter a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.append(guess)
            if '_' not in display_word(word, guessed_letters):
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            guesses -= 1
            guessed_letters.append(guess)
            if guesses == 0:
                print("Sorry, you've run out of guesses. The word was:", word)
                break
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
