using System;

class Program
{
    // Function to compute the Greatest Common Divisor using Euclidean Algorithm
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

    // Function to convert decimal to fraction
    public static string DecimalToFraction(double decimalNumber, double tolerance = 1.0E-6)
    {
        if (decimalNumber == 0)
            return "0";

        // Handle negative numbers
        bool isNegative = false;
        if (decimalNumber < 0)
        {
            isNegative = true;
            decimalNumber = Math.Abs(decimalNumber);
        }

        long numerator = 1;
        long denominator = 1;

        // Continue until the approximation is within the tolerance
        double fraction = (double)numerator / denominator;
        while (Math.Abs(fraction - decimalNumber) > tolerance)
        {
            if (fraction < decimalNumber)
            {
                numerator++;
            }
            else
            {
                denominator++;
                numerator = (long)Math.Round(decimalNumber * denominator);
            }
            // Simplify the fraction at each step
            long gcd = GCD(numerator, denominator);
            numerator /= gcd;
            denominator /= gcd;
            fraction = (double)numerator / denominator;
        }

        if (isNegative)
            numerator = -numerator;

        return $"{numerator}/{denominator}";
    }

    static void Main()
    {
        double decimalNumber = 0.75; // Example input
        string fraction = DecimalToFraction(decimalNumber);
        Console.WriteLine($"{decimalNumber} as a fraction is {fraction}");
    }
}