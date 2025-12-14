using System;
using System.Collections.Generic;
using System.Linq;

public class MedianCalculator
{
    public static double CalculateMedian(List<double> numbers)
    {
        if (numbers == null || numbers.Count == 0)
            throw new ArgumentException("The list of numbers cannot be null or empty.");

        var sortedNumbers = numbers.OrderBy(n => n).ToList();
        int count = sortedNumbers.Count;
        int middleIndex = count / 2;

        if (count % 2 == 0)
        {
            // Even number of elements - average the two middle values
            return (sortedNumbers[middleIndex - 1] + sortedNumbers[middleIndex]) / 2.0;
        }
        else
        {
            // Odd number of elements - return the middle value
            return sortedNumbers[middleIndex];
        }
    }

    static void Main()
    {
        List<double> sampleNumbers = new List<double> { 1, 3, 3, 6, 7, 8, 9 };
        Console.WriteLine("Median: " + CalculateMedian(sampleNumbers));
    }
}