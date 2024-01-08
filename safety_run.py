
import random

def hangman():
    word_list = ["python", "hangman", "game", "programming", "computer"]
    word = random.choice(word_list)
    lives = 6
    guessed_letters = []
    guessed_word = "_" * len(word)
    
    while lives > 0:
        print(f"\n{' '.join(guessed_word)}")
        letter = input("Guess a letter: ").lower()
        
        if len(letter) != 1 or not letter.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if letter in guessed_letters:
            print("You have already guessed that letter.")
            continue
            
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed_word = guessed_word[:i] + letter + guessed_word[i+1:]
        else:
            lives -= 1
            print(f"Incorrect! You have {lives} lives remaining.")
        
        guessed_letters.append(letter)
        
        if "_" not in guessed_word:
            print(f"\nCongratulations! You won! The word was '{word}'.")
            return
    
    print(f"\nGame over! You ran out of lives. The word was '{word}'.")
    

print("Welcome to Hangman!")
hangman()
