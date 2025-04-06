
import random

def main():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")
        
        play_again = input("Do you want to play again? (yes/no)").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
