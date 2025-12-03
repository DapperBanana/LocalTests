using System;
using System.Text;

public class Program
{
    public static string RemovePunctuation(string input)
    {
        StringBuilder result = new StringBuilder();
        foreach (char c in input)
        {
            if (!char.IsPunctuation(c))
            {
                result.Append(c);
            }
        }
        return result.ToString();
    }

    static void Main()
    {
        string testString = "Hello, world! How are you today?";
        Console.WriteLine(RemovePunctuation(testString));
    }
}