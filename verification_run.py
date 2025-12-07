using System;

class IcosahedronAreaCalculator
{
    static void Main()
    {
        // Length of one edge of the icosahedron
        Console.WriteLine("Enter the length of an edge: ");
        double edgeLength = Convert.ToDouble(Console.ReadLine());

        // Calculate the surface area of a regular icosahedron
        // Formula: 5 * sqrt(3) * a^2
        double surfaceArea = 5 * Math.Sqrt(3) * Math.Pow(edgeLength, 2);

        Console.WriteLine($"The surface area of the icosahedron is: {surfaceArea}");
    }
}