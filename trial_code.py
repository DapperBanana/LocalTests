using System;

class Program
{
    // Function to compute the Greatest Common Divisor (GCD) using Euclidean Algorithm
    static long GCD(long a, long b)
    {
        while (b != 0)
        {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    // Function to compute the Least Common Multiple (LCM)
    static long LCM(long a, long b)
    {
        return Math.Abs(a * b) / GCD(a, b);
    }

    static void Main()
    {
        Console.WriteLine("Enter the first number:");
        long num1 = long.Parse(Console.ReadLine());

        Console.WriteLine("Enter the second number:");
        long num2 = long.Parse(Console.ReadLine());

        long lcm = LCM(num1, num2);
        Console.WriteLine($"LCM of {num1} and {num2} is {lcm}");
    }
}