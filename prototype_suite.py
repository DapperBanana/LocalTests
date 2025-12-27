using System;

class Program
{
    static void Main()
    {
        // Number of sides for a regular dodecagon
        int n = 12;
        // Length of one side
        Console.Write("Enter the length of a side: ");
        double sideLength = Convert.ToDouble(Console.ReadLine());

        // Calculate the area
        double area = (n * Math.Pow(sideLength, 2)) / (4 * Math.Tan(Math.PI / n));
        Console.WriteLine($"The area of the regular dodecagon is: {area}");
    }
}