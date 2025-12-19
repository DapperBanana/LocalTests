using System;

class Program
{
    // Function to check if a year is a leap year
    static bool IsLeapYear(int year)
    {
        // A year is a leap year if it is divisible by 4
        // but not divisible by 100, unless it is divisible by 400
        return (year % 4 == 0) && (year % 100 != 0 || year % 400 == 0);
    }
    
    static void Main()
    {
        Console.WriteLine("Enter a year:");
        int year;
        if (int.TryParse(Console.ReadLine(), out year))
        {
            if (IsLeapYear(year))
                Console.WriteLine($"{year} is a leap year.");
            else
                Console.WriteLine($"{year} is not a leap year.");
        }
        else
        {
            Console.WriteLine("Invalid input.");
        }
    }
}