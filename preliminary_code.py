
import random

# List of words to choose from
word_list = ["python", "hangman", "computer", "programming", "keyboard", "monitor"]

# Select a random word from the list
word = random.choice(word_list)

# Create a list to store the guessed letters
guessed_letters = []

# Create a string to store the guessed word
guessed_word = "_" * len(word)

# Number of incorrect guesses allowed
max_attempts = 6
attempts = 0

print("Welcome to Hangman!")
print("Try to guess the word:")

while attempts < max_attempts and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word = guessed_word[:i] + guess + guessed_word[i + 1:]
    else:
        attempts += 1
        print("Incorrect guess. Attempts left:", max_attempts - attempts)

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nSorry, you ran out of attempts. The word was:", word)
