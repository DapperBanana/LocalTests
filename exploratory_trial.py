// C# code for generating a random sentence using Markov chains

using System;
using System.Collections.Generic;
using System.Text;
using System.Text.RegularExpressions;

public class MarkovChainGenerator
{
    private Dictionary<string, List<string>> markovChain = new Dictionary<string, List<string>>();
    private Random random = new Random();

    // Train the model with input text
    public void Train(string inputText)
    {
        var words = Tokenize(inputText);
        for (int i = 0; i < words.Length - 1; i++)
        {
            string currentWord = words[i];
            string nextWord = words[i + 1];

            if (!markovChain.ContainsKey(currentWord))
            {
                markovChain[currentWord] = new List<string>();
            }
            markovChain[currentWord].Add(nextWord);
        }
    }

    // Generate a sentence with optional maximum length
    public string GenerateSentence(int maxWords = 20)
    {
        // Choose a starting word randomly
        var keys = new List<string>(markovChain.Keys);
        string currentWord = keys[random.Next(keys.Count)];

        StringBuilder result = new StringBuilder();
        result.Append(Capitalize(currentWord));

        for (int i = 0; i < maxWords - 1; i++)
        {
            if (markovChain.ContainsKey(currentWord))
            {
                var nextWords = markovChain[currentWord];
                currentWord = nextWords[random.Next(nextWords.Count)];
                result.Append(" ").Append(currentWord);
                if (IsSentenceEnd(currentWord))
                {
                    break;
                }
            }
            else
            {
                break;
            }
        }

        return result.ToString() + ".";
    }

    // Helper: Tokenize input text into words
    private string[] Tokenize(string text)
    {
        var matches = Regex.Matches(text, @"\b\w+\b");
        List<string> tokens = new List<string>();
        foreach (Match match in matches)
        {
            tokens.Add(match.Value.ToLower());
        }
        return tokens.ToArray();
    }

    // Helper: Capitalize first letter
    private string Capitalize(string word)
    {
        if (string.IsNullOrEmpty(word))
            return word;
        return char.ToUpper(word[0]) + word.Substring(1);
    }

    // Helper: Decide if the word ends a sentence
    private bool IsSentenceEnd(string word)
    {
        // For simplicity, assume words like 'end' or 'stop' could signify sentence end
        // You can customize this as needed
        return false;
    }
}

class Program
{
    static void Main()
    {
        string sampleText = @"The quick brown fox jumps over the lazy dog. 
                               The fox is quick and the dog is lazy. 
                               Dogs and foxes are animals.";

        MarkovChainGenerator generator = new MarkovChainGenerator();
        generator.Train(sampleText);

        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine(generator.GenerateSentence());
        }
    }
}