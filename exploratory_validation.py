using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a string:");
        string input = Console.ReadLine();

        if (IsPalindrome(input))
        {
            Console.WriteLine("The string is a palindrome.");
        }
        else
        {
            Console.WriteLine("The string is not a palindrome.");
        }
    }

    static bool IsPalindrome(string str)
    {
        if (str == null) return false;

        int left = 0;
        int right = str.Length - 1;

        while (left < right)
        {
            // Skip non-alphanumeric characters if needed
            while (left < right && !Char.IsLetterOrDigit(str[left])) left++;
            while (left < right && !Char.IsLetterOrDigit(str[right])) right--;

            if (Char.ToLower(str[left]) != Char.ToLower(str[right]))
                return false;

            left++;
            right--;
        }
        return true;
    }
}