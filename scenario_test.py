
import random

def choose_word():
    words = ['python', 'hangman', 'programming', 'computer', 'algorithm', 'code']
    return random.choice(words)

def play_hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0

    while True:
        display_word = ''
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += '_ '
        
        print(display_word)
        guess = input('Guess a letter: ').lower()

        if guess in guessed_letters:
            print('You already guessed that letter.')
        elif guess in word:
            guessed_letters.append(guess)
            if all(letter in guessed_letters for letter in word):
                print('Congratulations! You guessed the word:', word)
                break
        else:
            incorrect_guesses += 1
            print('Incorrect guess. You have', 6 - incorrect_guesses, 'tries left.')
            if incorrect_guesses == 6:
                print('You ran out of tries. The word was:', word)
                break

    play_again = input('Play again? (y/n): ')
    if play_again.lower() == 'y':
        play_hangman()
    else:
        print('Thanks for playing!')

play_hangman()
