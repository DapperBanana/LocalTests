using System;
using System.IO;

class WordCount
{
    static void Main(string[] args)
    {
        Console.WriteLine("Enter the path to the text file:");
        string filePath = Console.ReadLine();

        try
        {
            string content = File.ReadAllText(filePath);
            // Split on whitespace characters to count words
            int wordCount = 0;
            if (!string.IsNullOrWhiteSpace(content))
            {
                string[] words = content.Split(new char[] { ' ', '\t', '\n', '\r' }, StringSplitOptions.RemoveEmptyEntries);
                wordCount = words.Length;
            }
            Console.WriteLine($"Number of words: {wordCount}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error reading file: {ex.Message}");
        }
    }
}