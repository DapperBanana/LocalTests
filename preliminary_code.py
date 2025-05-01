
import random

def get_user_choice():
    print("Rock, Paper, or Scissors?")
    user_choice = input().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chooses {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    main()
