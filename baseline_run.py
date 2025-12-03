using System;
using System.Collections.Generic;

class Program
{
    // Function to compute GCD of two numbers
    static int GCD(int a, int b)
    {
        while (b != 0)
        {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return Math.Abs(a);
    }

    // Function to compute LCM of two numbers
    static int LCM(int a, int b)
    {
        return Math.Abs(a * b) / GCD(a, b);
    }

    // Function to compute LCM of a list of numbers
    static int LCMOfList(List<int> numbers)
    {
        if (numbers == null || numbers.Count == 0)
            return 0;
        int result = numbers[0];
        for (int i = 1; i < numbers.Count; i++)
        {
            result = LCM(result, numbers[i]);
        }
        return result;
    }

    static void Main()
    {
        // Example usage
        List<int> numbers = new List<int> { 4, 6, 8 };
        Console.WriteLine("LCM of list: " + LCMOfList(numbers));
    }
}