using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a number:");
        int number = int.Parse(Console.ReadLine());

        while (number >= 10)
        {
            int sum = 0;
            while (number > 0)
            {
                sum += number % 10;
                number /= 10;
            }
            number = sum;
        }

        Console.WriteLine($"The single-digit sum is: {number}");
    }
}