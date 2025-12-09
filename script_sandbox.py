using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string input = "This is a test. This test is only a test.";
        Dictionary<string, int> wordCount = new Dictionary<string, int>(StringComparer.OrdinalIgnoreCase);

        string[] words = input.Split(new char[] { ' ', '.', ',', '!', '?' }, StringSplitOptions.RemoveEmptyEntries);

        foreach (string word in words)
        {
            if (wordCount.ContainsKey(word))
            {
                wordCount[word]++;
            }
            else
            {
                wordCount[word] = 1;
            }
        }

        foreach (var pair in wordCount)
        {
            Console.WriteLine($"'{pair.Key}': {pair.Value}");
        }
    }
}