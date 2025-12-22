using System;

class Program
{
    static void Main()
    {
        string sentence = "This is a sample sentence";
        string[] words = sentence.Split(' ');
        Array.Reverse(words);
        string reversedSentence = string.Join(" ", words);
        Console.WriteLine(reversedSentence);
    }
}