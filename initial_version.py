using System;
using System.Text;

public class Program
{
    public static void Main()
    {
        string input = "Hello, world! How are you today?";
        string result = RemovePunctuation(input);
        Console.WriteLine(result);
    }

    public static string RemovePunctuation(string str)
    {
        StringBuilder sb = new StringBuilder();
        foreach (char c in str)
        {
            if (!char.IsPunctuation(c))
            {
                sb.Append(c);
            }
        }
        return sb.ToString();
    }
}