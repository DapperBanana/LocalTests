// C# program to calculate the area of a parallelogram
using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter the base length of the parallelogram: ");
        double baseLength = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter the height of the parallelogram: ");
        double height = Convert.ToDouble(Console.ReadLine());

        double area = baseLength * height;
        Console.WriteLine("The area of the parallelogram is: " + area);
    }
}