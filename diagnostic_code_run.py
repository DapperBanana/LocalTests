using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a string:");
        string input = Console.ReadLine();
        string titleCase = ToTitleCase(input);
        Console.WriteLine("Title Case: " + titleCase);
    }

    static string ToTitleCase(string str)
    {
        if (string.IsNullOrEmpty(str))
            return str;

        string[] words = str.Split(' ');
        for (int i = 0; i < words.Length; i++)
        {
            if (words[i].Length > 0)
            {
                string firstChar = Char.ToUpper(words[i][0]).ToString();
                string rest = words[i].Substring(1).ToLower();
                words[i] = firstChar + rest;
            }
        }
        return String.Join(" ", words);
    }
}