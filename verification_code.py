using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string input = "This is a test. This test is only a test.";
        Dictionary<string, int> wordCounts = CountWordOccurrences(input);
        
        foreach (var pair in wordCounts)
        {
            Console.WriteLine($"'{pair.Key}': {pair.Value}");
        }
    }

    static Dictionary<string, int> CountWordOccurrences(string input)
    {
        // Convert to lowercase and split by non-word characters
        string[] words = System.Text.RegularExpressions.Regex.Split(input.ToLower(), @"\W+");
        var counts = new Dictionary<string, int>();

        foreach (string word in words)
        {
            if (string.IsNullOrWhiteSpace(word))
                continue;

            if (counts.ContainsKey(word))
            {
                counts[word]++;
            }
            else
            {
                counts[word] = 1;
            }
        }
        return counts;
    }
}