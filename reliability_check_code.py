// Python code implementation to sort a list of integers in ascending order
// Note: Since you asked for C# code, here is the equivalent C# implementation.

using System;
using System.Collections.Generic;

public class Program
{
    public static void Main()
    {
        List<int> numbers = new List<int> { 5, 2, 9, 1, 5, 6 };
        numbers.Sort();
        Console.WriteLine(string.Join(", ", numbers));
    }
}