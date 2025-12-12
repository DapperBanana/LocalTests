using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Example sets
        HashSet<int> set1 = new HashSet<int> {1, 2, 3, 4};
        HashSet<int> set2 = new HashSet<int> {3, 4, 5, 6};

        // Compute the union
        HashSet<int> unionSet = new HashSet<int>(set1);
        unionSet.UnionWith(set2);

        // Print the result
        Console.WriteLine("Union of the two sets:");
        foreach (var item in unionSet)
        {
            Console.WriteLine(item);
        }
    }
}