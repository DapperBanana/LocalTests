
import random

def hangman():
  word_list = ["python", "hangman", "game", "computer", "programming"]
  word = random.choice(word_list)
  guess = "_" * len(word)
  guessed_letters = []
  attempts = 6

  print("Let's play Hangman!")
  print(guess)

  while attempts > 0 and "_" in guess:
    letter = input("Guess a letter: ").lower()

    if letter in guessed_letters:
      print("You already guessed that letter.")

    elif len(letter) != 1 or not letter.isalpha():
        print("Please enter a single alphabetical character.")

    elif letter in word:
      for i in range(len(word)):
        if word[i] == letter:
          guess = guess[:i] + letter + guess[i+1:]
      guessed_letters.append(letter)
      print(guess)

    else:
      attempts -= 1
      guessed_letters.append(letter)
      print(f"Incorrect. You have {attempts} attempts remaining.")

  if "_" not in guess:
    print("Congratulations, you won!")

  else:
    print(f"Sorry, you lost! The word was {word}.")

hangman()
