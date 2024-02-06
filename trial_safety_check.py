letion(id='chatcmpl-8p4ZAd1Ftnmdi3EW9B39YkBA5WV6m', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import random

def hangman():
    word_list = ['python', 'programming', 'hangman', 'computer', 'game']
    word = random.choice(word_list)
    guessed_letters = []
    remaining_attempts = 6
    correct_guesses = 0
    
    while remaining_attempts > 0 and correct_guesses < len(word):
        print("\n" + "-" * 20)
        print("Word:", end=" ")

        for letter in word:
            if letter in guessed_letters:
                print(letter, end=" ")
                correct_guesses += 1
            else:
                print("_", end=" ")
        
        print("\n")
        print("Guessed Letters:", guessed_letters)
        print("Remaining Attempts:", remaining_attempts)
        
        guess = input("Enter your guess: ").lower()
        
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You have already guessed that letter.")
            elif guess in word:
                print("Correct guess!")
                guessed_letters.append(guess)
            else:
                print("Wrong guess!")
                remaining_attempts -= 1
                guessed_letters.append(guess)
        else:
            print("Invalid guess. Please enter a single letter.")
    
    print("\n" + "-" * 20)
    
    if correct_guesses == len(word):
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game over! The word was:", word)

hangman()', role='assistant', function_call=None, tool_calls=None))], created=1707182972, model='gpt-3.5-turbo-0613', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=304, prompt_tokens=23, total_tokens=327)