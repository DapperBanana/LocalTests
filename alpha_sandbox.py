using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter the length of a side of the regular hexadecagon: ");
        double sideLength = double.Parse(Console.ReadLine());

        // Formula for the area of a regular hexadecagon:
        // Area = 4 * (1 + sqrt(2)) * side^2
        double area = 4 * (1 + Math.Sqrt(2)) * Math.Pow(sideLength, 2);

        Console.WriteLine($"The area of the regular hexadecagon is: {area}");
    }
}