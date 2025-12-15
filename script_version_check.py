using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter the edge length of the regular tetrahedron:");
        double edgeLength = Convert.ToDouble(Console.ReadLine());

        // Calculate the area of one face (equilateral triangle)
        double faceArea = Math.Sqrt(3) / 4 * Math.Pow(edgeLength, 2);
        // Total surface area of the tetrahedron (4 faces)
        double totalArea = 4 * faceArea;

        Console.WriteLine($"The surface area of the regular tetrahedron is: {totalArea}");
    }
}