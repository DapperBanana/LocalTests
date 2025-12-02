using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a number:");
        int number = int.Parse(Console.ReadLine());
        int result = FindNextPrime(number);
        Console.WriteLine($"The smallest prime greater than {number} is {result}.");
    }

    static int FindNextPrime(int num)
    {
        int candidate = num + 1;
        while (!IsPrime(candidate))
        {
            candidate++;
        }
        return candidate;
    }

    static bool IsPrime(int n)
    {
        if (n <= 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;

        int sqrtN = (int)Math.Sqrt(n);
        for (int i = 3; i <= sqrtN; i += 2)
        {
            if (n % i == 0)
                return false;
        }
        return true;
    }
}