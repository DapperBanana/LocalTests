
import random

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or (player == 'scissors' and computer == 'paper') or (player == 'paper' and computer == 'rock'):
        return "Player wins!"
    else:
        return "Computer wins!"

def main():
    choices = ['rock', 'paper', 'scissors']

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ")
        
        if player_choice == 'q':
            print("Thanks for playing!")
            break
        
        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = random.choice(choices)
        
        print(f"Player choice: {player_choice}")
        print(f"Computer choice: {computer_choice}")
        
        print(get_winner(player_choice, computer_choice))

if __name__ == "__main__":
    main()
