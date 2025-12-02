// C# program to calculate the surface area of a regular pentagonal prism
using System;

class PentagonalPrism
{
    static void Main()
    {
        // Input: length of the side of the pentagon and the height of the prism
        Console.WriteLine("Enter the length of the side of the pentagon:");
        double sideLength = Convert.ToDouble(Console.ReadLine());

        Console.WriteLine("Enter the height of the prism:");
        double height = Convert.ToDouble(Console.ReadLine());

        // Calculate the area of the base pentagon
        double apothem = sideLength / (2 * Math.Tan(Math.PI / 5));
        double baseArea = (5 * sideLength * apothem) / 2;

        // Calculate the lateral surface area (perimeter * height)
        double perimeter = 5 * sideLength;
        double lateralSurfaceArea = perimeter * height;

        // Calculate the total surface area
        double totalSurfaceArea = 2 * baseArea + lateralSurfaceArea;

        Console.WriteLine($"The surface area of the pentagonal prism is: {totalSurfaceArea}");
    }
}