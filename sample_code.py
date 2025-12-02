using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter the length of one side of the regular octagon: ");
        double sideLength = double.Parse(Console.ReadLine());

        double area = CalculateOctagonArea(sideLength);
        Console.WriteLine($"The area of the regular octagon is: {area}");
    }

    static double CalculateOctagonArea(double side)
    {
        // Formula for the area of a regular octagon:
        // (2 * (1 + √2)) * side^2
        return 2 * (1 + Math.Sqrt(2)) * Math.Pow(side, 2);
    }
}