using System;

class PalindromeYearChecker
{
    static void Main()
    {
        Console.Write("Enter a year: ");
        string yearInput = Console.ReadLine();

        if (int.TryParse(yearInput, out int year))
        {
            string yearStr = year.ToString();
            string reversedYear = ReverseString(yearStr);
            if (yearStr == reversedYear)
            {
                Console.WriteLine($"{year} is a palindrome year.");
            }
            else
            {
                Console.WriteLine($"{year} is not a palindrome year.");
            }
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a valid year.");
        }
    }

    static string ReverseString(string s)
    {
        char[] charArray = s.ToCharArray();
        Array.Reverse(charArray);
        return new string(charArray);
    }
}