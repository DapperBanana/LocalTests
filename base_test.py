using System;

class Program
{
    // Method to calculate GCD (Greatest Common Divisor) using Euclidean Algorithm
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

    // Method to calculate LCM (Least Common Multiple)
    static int LCM(int a, int b)
    {
        return Math.Abs(a * b) / GCD(a, b);
    }

    static void Main()
    {
        Console.Write("Enter the first number: ");
        int num1 = int.Parse(Console.ReadLine());

        Console.Write("Enter the second number: ");
        int num2 = int.Parse(Console.ReadLine());

        int lcm = LCM(num1, num2);
        Console.WriteLine($"The Least Common Multiple of {num1} and {num2} is {lcm}");
    }
}