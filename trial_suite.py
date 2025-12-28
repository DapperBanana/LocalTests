using System;

class Program
{
    static void Main()
    {
        string[] options = { "rock", "paper", "scissors" };
        Random rand = new Random();

        Console.WriteLine("Welcome to Rock-Paper-Scissors!");

        while (true)
        {
            Console.Write("Enter your choice (rock, paper, scissors) or 'exit' to quit: ");
            string playerChoice = Console.ReadLine().ToLower();

            if (playerChoice == "exit")
            {
                break;
            }

            if (Array.IndexOf(options, playerChoice) == -1)
            {
                Console.WriteLine("Invalid choice. Please try again.");
                continue;
            }

            string computerChoice = options[rand.Next(options.Length)];
            Console.WriteLine($"Computer chose: {computerChoice}");

            if (playerChoice == computerChoice)
            {
                Console.WriteLine("It's a tie!");
            }
            else if (
                (playerChoice == "rock" && computerChoice == "scissors") ||
                (playerChoice == "scissors" && computerChoice == "paper") ||
                (playerChoice == "paper" && computerChoice == "rock")
            )
            {
                Console.WriteLine("You win!");
            }
            else
            {
                Console.WriteLine("You lose!");
            }
        }

        Console.WriteLine("Thanks for playing!");
    }
}