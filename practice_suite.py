using System;

class Program
{
    static void Main()
    {
        // Input: length of a side of the regular decagon
        Console.Write("Enter the length of a side: ");
        double sideLength = Convert.ToDouble(Console.ReadLine());

        // Number of sides for a decagon
        int numberOfSides = 10;

        // Calculate the area using the formula:
        // Area = (1/2) * perimeter * apothem
        // For a regular polygon: apothem = side / (2 * tan(pi / n))
        double apothem = sideLength / (2 * Math.Tan(Math.PI / numberOfSides));
        double perimeter = numberOfSides * sideLength;
        double area = (perimeter * apothem) / 2;

        Console.WriteLine($"The area of the regular decagon is: {area}");
    }
}