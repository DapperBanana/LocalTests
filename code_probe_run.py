using System;

class Program
{
    static void Main()
    {
        // Side length of the regular dodecagon
        double sideLength = 1.0; // You can change this value

        // Calculate the area
        double area = CalculateDodecagonArea(sideLength);

        Console.WriteLine($"The area of a regular dodecagon with side length {sideLength} is {area}");
    }

    static double CalculateDodecagonArea(double side)
    {
        // Formula: (3 * s^2 * (2 + √3))
        return (3 * Math.Pow(side, 2) * (2 + Math.Sqrt(3)));
    }
}