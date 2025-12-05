using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

class Program
{
    static void Main()
    {
        string text = "Here's a sample text with #hashtags like #CSharp, #Code, and #AI.";
        List<string> hashtags = ExtractHashtags(text);
        
        foreach (var hashtag in hashtags)
        {
            Console.WriteLine(hashtag);
        }
    }

    static List<string> ExtractHashtags(string input)
    {
        var hashtags = new List<string>();
        var pattern = @"#\w+";

        foreach (Match match in Regex.Matches(input, pattern))
        {
            hashtags.Add(match.Value);
        }

        return hashtags;
    }
}