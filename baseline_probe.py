using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter the radius of the circle:");
        string input = Console.ReadLine();
        if (double.TryParse(input, out double radius))
        {
            double area = Math.PI * radius * radius;
            Console.WriteLine($"The area of the circle is: {area}");
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a numeric value for the radius.");
        }
    }
}