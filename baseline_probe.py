// Sample C# program to find the union of two sets
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Define two sets
        HashSet<int> set1 = new HashSet<int> { 1, 2, 3, 4 };
        HashSet<int> set2 = new HashSet<int> { 3, 4, 5, 6 };

        // Find the union of the sets
        HashSet<int> unionSet = new HashSet<int>(set1);
        unionSet.UnionWith(set2);

        // Display the result
        Console.WriteLine("Union of the sets:");
        foreach (int item in unionSet)
        {
            Console.WriteLine(item);
        }
    }
}