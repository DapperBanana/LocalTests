using System;
using System.IO;

class Program
{
    static void Main()
    {
        string filePath = "yourfile.csv";

        try
        {
            // Read all lines from the CSV file
            string[] lines = File.ReadAllLines(filePath);

            // Print each line
            foreach (var line in lines)
            {
                Console.WriteLine(line);
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}