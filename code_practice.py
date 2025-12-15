using System;

class Program
{
    static void Main()
    {
        // Input coordinates for the first point
        Console.Write("Enter x1: ");
        double x1 = Convert.ToDouble(Console.ReadLine());
        Console.Write("Enter y1: ");
        double y1 = Convert.ToDouble(Console.ReadLine());
        Console.Write("Enter z1: ");
        double z1 = Convert.ToDouble(Console.ReadLine());

        // Input coordinates for the second point
        Console.Write("Enter x2: ");
        double x2 = Convert.ToDouble(Console.ReadLine());
        Console.Write("Enter y2: ");
        double y2 = Convert.ToDouble(Console.ReadLine());
        Console.Write("Enter z2: ");
        double z2 = Convert.ToDouble(Console.ReadLine());

        // Calculate the distance
        double distance = Math.Sqrt(Math.Pow(x2 - x1, 2) +
                                    Math.Pow(y2 - y1, 2) +
                                    Math.Pow(z2 - z1, 2));

        // Output the result
        Console.WriteLine($"Distance between points: {distance}");
    }
}