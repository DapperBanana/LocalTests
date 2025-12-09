using System;

class PrimeCounter
{
    static void Main()
    {
        Console.WriteLine("Enter the start of the range:");
        int start = int.Parse(Console.ReadLine());
        Console.WriteLine("Enter the end of the range:");
        int end = int.Parse(Console.ReadLine());

        int count = 0;
        for (int num = start; num <= end; num++)
        {
            if (IsPrime(num))
            {
                count++;
            }
        }

        Console.WriteLine($"Number of prime numbers between {start} and {end}: {count}");
    }

    static bool IsPrime(int n)
    {
        if (n <= 1)
            return false;
        if (n <= 3)
            return true;
        if (n % 2 == 0 || n % 3 == 0)
            return false;

        for (int i = 5; i * i <= n; i += 6)
        {
            if (n % i == 0 || n % (i + 2) == 0)
                return false;
        }
        return true;
    }
}