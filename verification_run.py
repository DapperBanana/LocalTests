using System;

class Program
{
    static void Main()
    {
        // Input radius and angle in degrees
        Console.WriteLine("Enter the radius of the sector:");
        double radius = double.Parse(Console.ReadLine());

        Console.WriteLine("Enter the angle of the sector in degrees:");
        double angleDegrees = double.Parse(Console.ReadLine());

        // Convert angle from degrees to radians
        double angleRadians = (Math.PI / 180) * angleDegrees;

        // Calculate the area of the sector
        double area = 0.5 * radius * radius * angleRadians;

        Console.WriteLine($"The area of the sector is: {area}");
    }
}