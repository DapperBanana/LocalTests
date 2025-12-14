using System;

class Tetrahedron
{
    public static double CalculateSurfaceArea(double edgeLength)
    {
        // Surface area of a regular tetrahedron: A = √3 * a^2
        return Math.Sqrt(3) * Math.Pow(edgeLength, 2);
    }

    static void Main()
    {
        Console.Write("Enter the length of an edge of the tetrahedron: ");
        if (double.TryParse(Console.ReadLine(), out double edgeLength))
        {
            double area = CalculateSurfaceArea(edgeLength);
            Console.WriteLine($"The surface area of the tetrahedron is: {area}");
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a numeric value.");
        }
    }
}