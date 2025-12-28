using System;

public class PalindromeYearChecker
{
    public static void Main()
    {
        Console.WriteLine("Enter a year:");
        string input = Console.ReadLine();
        if (int.TryParse(input, out int year))
        {
            if (IsPalindromeYear(year))
                Console.WriteLine($"{year} is a palindrome year.");
            else
                Console.WriteLine($"{year} is not a palindrome year.");
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a valid year.");
        }
    }

    public static bool IsPalindromeYear(int year)
    {
        string yearStr = year.ToString();
        char[] charArray = yearStr.ToCharArray();
        Array.Reverse(charArray);
        string reversedYear = new string(charArray);
        return yearStr == reversedYear;
    }
}