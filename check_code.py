using System;

class Program
{
    static void Main()
    {
        // Length of a side of the nonagon
        double sideLength = 1.0;

        // Calculate the area
        double area = CalculateRegularNonagonArea(sideLength);
        Console.WriteLine($"The area of the regular nonagon is: {area}");
    }

    static double CalculateRegularNonagonArea(double side)
    {
        // Formula: (9/4) * side^2 * cot(π/9)
        double angle = Math.PI / 9; // 20 degrees in radians
        double cotangent = 1 / Math.Tan(angle);
        double area = (9.0 / 4.0) * Math.Pow(side, 2) * cotangent;
        return area;
    }
}