using System;

class Program
{
    static void Main()
    {
        // Radius of the circumscribed circle
        double radius = 1.0;

        // Number of sides for a hendecagon
        int n = 11;

        // Calculate the side length
        double sideLength = 2 * radius * Math.Sin(Math.PI / n);

        // Calculate the area of the regular hendecagon
        double area = (n * Math.Pow(sideLength, 2)) / (4 * Math.Tan(Math.PI / n));

        Console.WriteLine($"The area of a regular hendecagon with radius {radius} is: {area}");
    }
}