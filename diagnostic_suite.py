using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // List of questions and answers
        List<(string question, string answer)> quiz = new List<(string, string)>
        {
            ("What is the capital of France?", "Paris"),
            ("What is 2 + 2?", "4"),
            ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee")
        };

        int score = 0;

        Console.WriteLine("Welcome to the Educational Quiz!");
        Console.WriteLine("Type your answer and press Enter.\n");

        foreach (var (question, answer) in quiz)
        {
            Console.WriteLine(question);
            string userInput = Console.ReadLine();

            if (userInput != null && userInput.Trim().Equals(answer, StringComparison.OrdinalIgnoreCase))
            {
                Console.WriteLine("Correct!\n");
                score++;
            }
            else
            {
                Console.WriteLine($"Incorrect. The correct answer is: {answer}\n");
            }
        }

        Console.WriteLine($"Quiz complete! Your score: {score}/{quiz.Count}");
    }
}