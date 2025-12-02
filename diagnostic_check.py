using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a number:");
        if (int.TryParse(Console.ReadLine(), out int number))
        {
            Console.WriteLine($"Is the number {number} prime? {IsPrime(number)}");
        }
        else
        {
            Console.WriteLine("Invalid input.");
        }
    }

    static bool IsPrime(int num)
    {
        if (num <= 1) return false;
        if (num == 2) return true;
        if (num % 2 == 0) return false;
        int sqrt = (int)Math.Sqrt(num);
        for (int i = 3; i <= sqrt; i += 2)
        {
            if (num % i == 0) return false;
        }
        return true;
    }
}