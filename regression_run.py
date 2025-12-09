using System;
using System.Numerics;

class CarmichaelChecker
{
    // Check if a number is prime
    static bool IsPrime(BigInteger n)
    {
        if (n < 2) return false;
        if (n == 2 || n == 3) return true;
        if (n % 2 == 0) return false;

        BigInteger sqrtN = BigInteger.Sqrt(n);
        for (BigInteger i = 3; i <= sqrtN; i += 2)
        {
            if (n % i == 0)
                return false;
        }
        return true;
    }

    // Fast modular exponentiation
    static BigInteger ModPow(BigInteger baseNum, BigInteger exponent, BigInteger modulus)
    {
        return BigInteger.ModPow(baseNum, exponent, modulus);
    }

    // Check if n is a Carmichael number
    public static bool IsCarmichael(BigInteger n)
    {
        // Carmichael numbers are composite and satisfy Korselt's criterion:
        // 1. n is square-free
        // 2. For every prime p dividing n, (p - 1) divides (n - 1)

        if (n < 2 || IsPrime(n))
            return false;

        // Find the prime factors of n
        var primeFactors = new System.Collections.Generic.List<BigInteger>();
        BigInteger temp = n;

        for (BigInteger i = 2; i * i <= temp; i++)
        {
            if (temp % i == 0)
            {
                if (IsPrime(i))
                {
                    primeFactors.Add(i);
                    while (temp % i == 0)
                        temp /= i;
                }
            }
        }
        if (temp > 1)
        {
            if (IsPrime(temp))
                primeFactors.Add(temp);
        }

        // Check if n is square-free
        var uniqueFactors = new System.Collections.Generic.HashSet<BigInteger>(primeFactors);
        if (uniqueFactors.Count != primeFactors.Count)
            return false; // Not square-free

        // Check Korselt's criterion for each prime factor
        foreach (var p in uniqueFactors)
        {
            if ((n - 1) % (p - 1) != 0)
                return false;
        }

        // Ensure n is composite (already checked)

        return true;
    }

    static void Main()
    {
        Console.WriteLine("Enter a number to check if it is a Carmichael number:");
        string input = Console.ReadLine();
        if (BigInteger.TryParse(input, out BigInteger number))
        {
            if (IsCarmichael(number))
                Console.WriteLine($"{number} is a Carmichael number.");
            else
                Console.WriteLine($"{number} is NOT a Carmichael number.");
        }
        else
        {
            Console.WriteLine("Invalid input.");
        }
    }
}