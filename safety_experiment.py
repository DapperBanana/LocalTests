
import random

def choose_word():
    words = ['python', 'hangman', 'computer', 'program', 'algorithm']
    return random.choice(words)

def play_hangman():
    word = choose_word()
    guessed = '_' * len(word)
    guessed_letters = []
    tries = 6
    
    print("Welcome to Hangman!")
    print(guessed)
    
    while tries > 0 and '_' in guessed:
        letter = input("Guess a letter: ").lower()
        
        if letter in guessed_letters:
            print("You've already guessed that letter")
        elif len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter")
        elif letter in word:
            new_guessed = ''
            for i in range(len(word)):
                if word[i] == letter:
                    new_guessed += letter
                else:
                    new_guessed += guessed[i]
            guessed = new_guessed
            guessed_letters.append(letter)
            print(guessed)
        else:
            tries -= 1
            guessed_letters.append(letter)
            print(f"Incorrect guess! You have {tries} tries left")
            print(guessed)
    
    if '_' not in guessed:
        print("Congratulations, you've guessed the word!")
    else:
        print(f"Sorry, you've run out of tries. The word was {word}")

play_hangman()
