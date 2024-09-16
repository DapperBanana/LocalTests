
import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif player_choice == 'rock' and computer_choice == 'scissors':
        return "Player wins!"
    elif player_choice == 'paper' and computer_choice == 'rock':
        return "Player wins!"
    elif player_choice == 'scissors' and computer_choice == 'paper':
        return "Player wins!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock-Paper-Scissors game!")
    
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        return
    
    computer_choice = get_computer_choice()
    
    print(f"Player choice: {player_choice}")
    print(f"Computer choice: {computer_choice}")
    
    winner = determine_winner(player_choice, computer_choice)
    print(winner)

if __name__ == "__main__":
    main()
