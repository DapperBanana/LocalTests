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
        for (int number = start; number <= end; number++)
        {
            if (IsPrime(number))
            {
                count++;
            }
        }

        Console.WriteLine($"Number of prime numbers between {start} and {end}: {count}");
    }

    static bool IsPrime(int num)
    {
        if (num <= 1)
            return false;
        if (num == 2)
            return true;
        if (num % 2 == 0)
            return false;

        int sqrt = (int)Math.Sqrt(num);
        for (int i = 3; i <= sqrt; i += 2)
        {
            if (num % i == 0)
                return false;
        }
        return true;
    }
}