
import random

def get_user_choice():
    user_choice = input("Rock, paper, or scissors? ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid input. Please choose rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Welcome to Rock-Paper-Scissors!")
    
    play_again = "y"
    while play_again == "y":
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose {user_choice}.")
        print(f"The computer chose {computer_choice}.")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Play again? (y/n) ").lower()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
