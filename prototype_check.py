using System;

class Program
{
    // Method to calculate the GCD (Greatest Common Divisor) using Euclidean algorithm
    static int GCD(int a, int b)
    {
        while (b != 0)
        {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    // Method to calculate LCM using GCD
    static int LCM(int a, int b)
    {
        return Math.Abs(a * b) / GCD(a, b);
    }

    static void Main()
    {
        Console.WriteLine("Enter the first number:");
        int num1 = int.Parse(Console.ReadLine());

        Console.WriteLine("Enter the second number:");
        int num2 = int.Parse(Console.ReadLine());

        int result = LCM(num1, num2);
        Console.WriteLine($"LCM of {num1} and {num2} is {result}");
    }
}