using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a number to check if it is a Lucas-Carmichael number:");
        if (long.TryParse(Console.ReadLine(), out long n))
        {
            if (IsLucasCarmichael(n))
                Console.WriteLine($"{n} is a Lucas-Carmichael number.");
            else
                Console.WriteLine($"{n} is not a Lucas-Carmichael number.");
        }
        else
        {
            Console.WriteLine("Invalid input.");
        }
    }

    static bool IsLucasCarmichael(long n)
    {
        if (n < 2)
            return false;

        // Get prime factors and their powers
        var factors = PrimeFactors(n);
        foreach (var factor in factors)
        {
            long p = factor.Key;
            int exp = factor.Value;

            // Check if p is prime
            if (!IsPrime(p))
                return false;

            // Compute U_p and check if U_p divides n
            long U_p = LucasCarmichaelU(p);
            if (U_p == 0 || n % U_p != 0)
                return false;
        }
        return true;
    }

    static Dictionary<long, int> PrimeFactors(long n)
    {
        var factors = new Dictionary<long, int>();
        long num = n;

        for (long i = 2; i * i <= num; i++)
        {
            while (num % i == 0)
            {
                if (factors.ContainsKey(i))
                    factors[i]++;
                else
                    factors[i] = 1;
                num /= i;
            }
        }
        if (num > 1)
        {
            if (factors.ContainsKey(num))
                factors[num]++;
            else
                factors[num] = 1;
        }
        return factors;
    }

    static bool IsPrime(long n)
    {
        if (n <= 1) return false;
        if (n == 2 || n == 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (long i = 5; i * i <= n; i += 6)
        {
            if (n % i == 0 || n % (i + 2) == 0)
                return false;
        }
        return true;
    }

    static long LucasCarmichaelU(long p)
    {
        // U_p = p + 1 if p is odd prime
        // for p=2, U_2=3
        if (p == 2)
            return 3;
        if (IsPrime(p))
            return p + 1;
        return 0;
    }
}