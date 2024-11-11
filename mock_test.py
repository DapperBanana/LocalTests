
import random

def get_user_choice():
    """
    Function to get the user's choice for rock, paper, or scissors
    """
    user_choice = input("Enter your choice (rock, paper, or scissors): ")
    return user_choice.lower()

def get_computer_choice():
    """
    Function to generate the computer's choice for rock, paper, or scissors
    """
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    """
    Function to determine the winner of the game
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    """
    Main function to run the rock-paper-scissors game
    """
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"Computer's choice: {computer_choice}")
    
    winner = determine_winner(user_choice, computer_choice)
    print(winner)

if __name__ == "__main__":
    main()
