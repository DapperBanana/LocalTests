// Note: Here's a C# implementation for removing duplicates from a list while preserving order.

using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<int> originalList = new List<int> { 1, 2, 2, 3, 4, 4, 5 };
        List<int> deduplicatedList = RemoveDuplicatesPreserveOrder(originalList);
        Console.WriteLine(string.Join(", ", deduplicatedList));
    }

    static List<T> RemoveDuplicatesPreserveOrder<T>(List<T> list)
    {
        HashSet<T> seen = new HashSet<T>();
        List<T> result = new List<T>();
        foreach (var item in list)
        {
            if (seen.Add(item))
            {
                result.Add(item);
            }
        }
        return result;
    }
}