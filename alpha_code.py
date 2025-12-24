using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a number:");
        string input = Console.ReadLine();

        if (int.TryParse(input, out int number))
        {
            bool isInvariant = IsPerfectDigitalInvariant(number);
            Console.WriteLine($"Number {number} is {(isInvariant ? "" : "not ")}a perfect digital invariant.");
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter an integer.");
        }
    }

    static bool IsPerfectDigitalInvariant(int number)
    {
        if (number == 0)
            return true;

        int originalNumber = number;
        int sumOfPoweredDigits = 0;
        int digitCount = number == 0 ? 1 : (int)Math.Log10(Math.Abs(number)) + 1;

        while (number != 0)
        {
            int digit = Math.Abs(number % 10);
            sumOfPoweredDigits += (int)Math.Pow(digit, digitCount);
            number /= 10;
        }

        return sumOfPoweredDigits == originalNumber;
    }
}