using System;

class Program
{
    static void Main()
    {
        // Example: input the side length of the dodecagon
        Console.WriteLine("Enter the length of a side of the dodecagon:");
        double sideLength = double.Parse(Console.ReadLine());

        double area = CalculateDodecagonArea(sideLength);
        Console.WriteLine($"The area of the regular dodecagon is: {area}");
    }

    static double CalculateDodecagonArea(double side)
    {
        // The formula for the area of a regular dodecagon:
        // Area = 3 * (2 + √3) * s^2
        double area = 3 * (2 + Math.Sqrt(3)) * Math.Pow(side, 2);
        return area;
    }
}