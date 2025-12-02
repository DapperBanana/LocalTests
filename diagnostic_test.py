// This language is C#, not Python. Here's the equivalent code in Python to read a JSON file and print key-value pairs:
using System;
using System.IO;
using Newtonsoft.Json.Linq;  // Make sure to install Newtonsoft.Json via NuGet

class Program
{
    static void Main()
    {
        string jsonFilePath = "path/to/your/file.json"; // Replace with your JSON file path
        
        string jsonContent = File.ReadAllText(jsonFilePath);
        JObject jsonObject = JObject.Parse(jsonContent);
        
        foreach (var property in jsonObject.Properties())
        {
            Console.WriteLine($"{property.Name}: {property.Value}");
        }
    }
}