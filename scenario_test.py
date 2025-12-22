using System;

class Program
{
    static void Main()
    {
        // Input: length of one side of the regular hexadecagon
        Console.Write("Enter the length of a side: ");
        double sideLength = Convert.ToDouble(Console.ReadLine());

        // Calculate the area of a regular hexadecagon
        double area = (8 * Math.Pow(sideLength, 2)) / Math.Tan(Math.PI / 16);

        Console.WriteLine("The area of the regular hexadecagon is: " + area);
    }
}