using System;

class PrimeCounter
{
    static void Main()
    {
        Console.WriteLine("Enter the start of the range:");
        int start = int.Parse(Console.ReadLine());
        Console.WriteLine("Enter the end of the range:");
        int end = int.Parse(Console.ReadLine());

        int primeCount = CountPrimesInRange(start, end);
        Console.WriteLine($"Number of prime numbers between {start} and {end}: {primeCount}");
    }

    static int CountPrimesInRange(int start, int end)
    {
        int count = 0;
        for (int number = start; number <= end; number++)
        {
            if (IsPrime(number))
            {
                count++;
            }
        }
        return count;
    }

    static bool IsPrime(int number)
    {
        if (number <= 1) return false;
        if (number == 2) return true;
        if (number % 2 == 0) return false;

        int sqrt = (int)Math.Sqrt(number);
        for (int i = 3; i <= sqrt; i += 2)
        {
            if (number % i == 0)
                return false;
        }
        return true;
    }
}