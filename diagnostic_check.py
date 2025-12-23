// C# code to generate a random sentence using Markov chains
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class MarkovChainGenerator
{
    private Dictionary<string, List<string>> markovChain = new Dictionary<string, List<string>>();
    private Random rand = new Random();

    public void BuildChain(string[] words)
    {
        for (int i = 0; i < words.Length - 1; i++)
        {
            var currentWord = words[i];
            var nextWord = words[i + 1];

            if (!markovChain.ContainsKey(currentWord))
            {
                markovChain[currentWord] = new List<string>();
            }
            markovChain[currentWord].Add(nextWord);
        }
    }

    public string GenerateSentence(int maxWords = 20)
    {
        var keys = markovChain.Keys.ToList();
        // Start with a capitalized word if possible
        string currentWord = keys[rand.Next(keys.Count)];
        var sentence = new List<string> { currentWord };

        for (int i = 0; i < maxWords - 1; i++)
        {
            if (!markovChain.ContainsKey(currentWord))
                break;

            var nextWords = markovChain[currentWord];
            currentWord = nextWords[rand.Next(nextWords.Count)];
            sentence.Add(currentWord);

            if (currentWord.EndsWith(".") || currentWord.EndsWith("!") || currentWord.EndsWith("?"))
                break;
        }

        return string.Join(" ", sentence);
    }

    static void Main(string[] args)
    {
        var generator = new MarkovChainGenerator();

        // Read input text from a file or define a string
        string inputText = @"Your sample input text goes here. It can be multiple sentences. The generator builds a model based on this.";

        // Preprocess text: split into words
        var words = inputText
            .Split(new[] { ' ', '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries)
            .Select(w => w.Trim())
            .ToArray();

        generator.BuildChain(words);

        // Generate and print a random sentence
        Console.WriteLine(generator.GenerateSentence());
    }
}