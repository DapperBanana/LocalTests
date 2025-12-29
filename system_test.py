using System;

class Program
{
    static void Main()
    {
        // Input: length of one side of the heptagon
        Console.Write("Enter the side length of the heptagon: ");
        double sideLength = Convert.ToDouble(Console.ReadLine());

        // Number of sides for a regular heptagon
        int n = 7;

        // Calculate the area
        double area = (n * Math.Pow(sideLength, 2)) /
                      (4 * Math.Tan(Math.PI / n));

        Console.WriteLine($"The area of the regular heptagon is: {area}");
    }
}