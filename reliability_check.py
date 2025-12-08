using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a string:");
        string input = Console.ReadLine();
        bool isIsogram = IsIsogram(input);
        Console.WriteLine($"Is the string an isogram? {isIsogram}");
    }

    static bool IsIsogram(string str)
    {
        if (string.IsNullOrEmpty(str))
            return true;

        str = str.ToLower();
        var seen = new HashSet<char>();

        foreach (char c in str)
        {
            if (char.IsLetter(c))
            {
                if (seen.Contains(c))
                    return false;
                seen.Add(c);
            }
        }
        return true;
    }
}