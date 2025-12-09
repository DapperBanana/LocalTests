// Note: The request was for Python code, but as specified, here's the C# version:

using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        // Sample dictionary
        Dictionary<string, int> dict = new Dictionary<string, int>()
        {
            {"a", 10},
            {"b", 5},
            {"c", 20},
            {"d", 15}
        };

        // Find the key-value pair with the maximum value
        var maxPair = dict.Aggregate((l, r) => l.Value > r.Value ? l : r);
        // Find the key-value pair with the minimum value
        var minPair = dict.Aggregate((l, r) => l.Value < r.Value ? l : r);

        Console.WriteLine($"Maximum value: {maxPair.Key} = {maxPair.Value}");
        Console.WriteLine($"Minimum value: {minPair.Key} = {minPair.Value}");
    }
}