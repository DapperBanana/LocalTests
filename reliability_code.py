using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter the limit: ");
        int limit = int.Parse(Console.ReadLine());

        long sum = 0;
        for (int num = 2; num <= limit; num++)
        {
            if (IsPrime(num))
            {
                sum += num;
            }
        }

        Console.WriteLine($"Sum of all prime numbers up to {limit} is: {sum}");
    }

    static bool IsPrime(int number)
    {
        if (number <= 1)
            return false;
        if (number == 2)
            return true;
        if (number % 2 == 0)
            return false;

        int sqrt = (int)Math.Sqrt(number);
        for (int i = 3; i <= sqrt; i += 2)
        {
            if (number % i == 0)
                return false;
        }
        return true;
    }
}