using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a non-negative integer:");
        if (int.TryParse(Console.ReadLine(), out int number) && number >= 0)
        {
            long factorial = CalculateFactorial(number);
            Console.WriteLine($"Factorial of {number} is {factorial}");
        }
        else
        {
            Console.WriteLine("Please enter a valid non-negative integer.");
        }
    }

    static long CalculateFactorial(int n)
    {
        long result = 1;
        for (int i = 1; i <= n; i++)
        {
            result *= i;
        }
        return result;
    }
}