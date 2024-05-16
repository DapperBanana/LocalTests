letion(id='chatcmpl-9Pe4PpLYa70CxqKdFZ7e7cS7wgTsh', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    if user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        play_game()
    else:
        computer_choice = random.choice(choices)
        
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")
            
        play_again = input("Do you want to play again? (yes/no): ").lower()
        
        if play_again == 'yes':
            play_game()
        else:
            print("Thanks for playing!")
        
play_game()', role='assistant', function_call=None, tool_calls=None))], created=1715899257, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=220, prompt_tokens=25, total_tokens=245)