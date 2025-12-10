using System;
using System.IO;

class Program
{
    static void Main()
    {
        // Specify the path to your text file
        string filePath = "path/to/your/file.txt";
        // Word to find and replace
        string wordToReplace = "oldWord";
        string replacementWord = "newWord";

        // Read all text from the file
        string content = File.ReadAllText(filePath);

        // Replace the specified word
        string updatedContent = content.Replace(wordToReplace, replacementWord);

        // Write the updated content back to the file
        File.WriteAllText(filePath, updatedContent);

        Console.WriteLine("Replacement complete.");
    }
}