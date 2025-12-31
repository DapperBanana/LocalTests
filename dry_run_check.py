using System;

class Program
{
    static string IntToRoman(int num)
    {
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        string result = "";

        for (int i = 0; i < values.Length && num > 0; i++)
        {
            while (num >= values[i])
            {
                result += symbols[i];
                num -= values[i];
            }
        }
        return result;
    }

    static void Main()
    {
        Console.Write("Enter a number: ");
        int number;
        if (int.TryParse(Console.ReadLine(), out number))
        {
            Console.WriteLine("Roman numeral: " + IntToRoman(number));
        }
        else
        {
            Console.WriteLine("Invalid input.");
        }
    }
}