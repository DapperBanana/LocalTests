using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a sentence:");
        string sentence = Console.ReadLine();

        string[] words = sentence.Split(new char[] {' '}, StringSplitOptions.RemoveEmptyEntries);
        int maxLength = 0;

        foreach (string word in words)
        {
            int length = word.Length;
            if (length > maxLength)
            {
                maxLength = length;
            }
        }
        Console.WriteLine("Length of the longest word: " + maxLength);
    }
}