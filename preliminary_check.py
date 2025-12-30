using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter the start of the range: ");
        int start = int.Parse(Console.ReadLine());
        Console.Write("Enter the end of the range: ");
        int end = int.Parse(Console.ReadLine());

        int sum = 0;
        for (int number = start; number <= end; number++)
        {
            if (IsPrime(number))
            {
                sum += number;
            }
        }

        Console.WriteLine($"Sum of all prime numbers in the range [{start}, {end}] is: {sum}");
    }

    static bool IsPrime(int n)
    {
        if (n < 2)
            return false;
        if (n == 2)
            return true;
        if (n % 2 == 0)
            return false;
        int sqrtN = (int)Math.Sqrt(n);
        for (int i = 3; i <= sqrtN; i += 2)
        {
            if (n % i == 0)
                return false;
        }
        return true;
    }
}