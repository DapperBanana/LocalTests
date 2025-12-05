using System;

public class RomanNumerals
{
    public static string ToRoman(int num)
    {
        if (num <= 0 || num > 3999)
            throw new ArgumentOutOfRangeException("Input must be between 1 and 3999");

        string[] thousands = { "", "M", "MM", "MMM" };
        string[] hundreds = { "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" };
        string[] tens = { "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" };
        string[] ones = { "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" };

        return thousands[num / 1000] +
               hundreds[(num % 1000) / 100] +
               tens[(num % 100) / 10] +
               ones[num % 10];
    }

    public static void Main()
    {
        Console.WriteLine("Enter a number between 1 and 3999:");
        int number;
        if (int.TryParse(Console.ReadLine(), out number))
        {
            try
            {
                string roman = ToRoman(number);
                Console.WriteLine($"Roman numeral: {roman}");
            }
            catch (ArgumentOutOfRangeException e)
            {
                Console.WriteLine(e.Message);
            }
        }
        else
        {
            Console.WriteLine("Invalid input");
        }
    }
}