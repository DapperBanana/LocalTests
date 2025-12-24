using System;

class Program
{
    // Method to calculate the area of a triangle given the lengths of its three sides
    static double CalculateTriangleArea(double a, double b, double c)
    {
        // Use Heron's formula
        double semiPerimeter = (a + b + c) / 2;
        return Math.Sqrt(semiPerimeter * (semiPerimeter - a) * (semiPerimeter - b) * (semiPerimeter - c));
    }

    static void Main()
    {
        // Example sides
        double side1 = 3;
        double side2 = 4;
        double side3 = 5;

        double area = CalculateTriangleArea(side1, side2, side3);
        Console.WriteLine($"The area of the triangle is {area}");
    }
}