using System;
using System.Collections.Generic;

class PrimeFactors
{
    static void Main(string[] args)
    {
        Console.WriteLine("Enter a number to find its prime factors:");
        if (long.TryParse(Console.ReadLine(), out long number))
        {
            var factors = GetPrimeFactors(number);
            Console.WriteLine($"Prime factors of {number}: {string.Join(", ", factors)}");
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a valid number.");
        }
    }

    static List<long> GetPrimeFactors(long n)
    {
        var factors = new List<long>();

        // Handle negative numbers
        if (n < 0)
        {
            factors.Add(-1);
            n = -n;
        }

        // Divide out factors of 2
        while (n % 2 == 0)
        {
            factors.Add(2);
            n /= 2;
        }

        // Divide out odd factors
        long divisor = 3;
        while (divisor * divisor <= n)
        {
            while (n % divisor == 0)
            {
                factors.Add(divisor);
                n /= divisor;
            }
            divisor += 2;
        }

        // If remaining n is greater than 1, it is a prime factor
        if (n > 1)
        {
            factors.Add(n);
        }

        return factors;
    }
}