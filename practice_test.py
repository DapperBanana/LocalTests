
import random

# List of words for the game
word_list = ['python', 'hangman', 'programming', 'computer', 'game', 'coding']

def hangman():
    # Choose a random word from the word list
    word = random.choice(word_list)
    # Create a list to store the guessed letters
    guessed_letters = []
    # Set the number of incorrect guesses allowed
    max_attempts = 6
    attempts = 0

    # Create a masked word with underscores for unguessed letters
    masked_word = ['_'] * len(word)

    while True:
        print(' '.join(masked_word))
        guess = input('Guess a letter: ').lower()

        # Check if the guessed letter is already guessed
        if guess in guessed_letters:
            print('You already guessed that letter. Try again.')
            continue
        
        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    masked_word[i] = guess
                if '_' not in masked_word:
                    print('You guessed the word:', word)
                    break
        else:
            attempts += 1
            print('Incorrect guess. Attempts left:', max_attempts - attempts)
            if attempts == max_attempts:
                print('You ran out of attempts. The word was:', word)
                break
        
        print('Guessed letters:', guessed_letters)

        if '_' not in masked_word:
            print('Congratulations! You guessed the word:', word)
            break

if __name__ == '__main__':
    hangman()
