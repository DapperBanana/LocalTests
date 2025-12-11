using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a number:");
        int number = int.Parse(Console.ReadLine());
        int nextPrime = FindNextPrime(number + 1);
        Console.WriteLine($"The smallest prime number greater than {number} is {nextPrime}.");
    }

    static bool IsPrime(int num)
    {
        if (num <= 1) return false;
        if (num == 2) return true;
        if (num % 2 == 0) return false;

        int sqrt = (int)Math.Sqrt(num);
        for (int i = 3; i <= sqrt; i += 2)
        {
            if (num % i == 0)
                return false;
        }
        return true;
    }

    static int FindNextPrime(int start)
    {
        int candidate = start;
        while (true)
        {
            if (IsPrime(candidate))
                return candidate;
            candidate++;
        }
    }
}