using System;

class Program
{
    static void Main()
    {
        // Radius of the circumcircle of the decagon
        double sideLength = 5; // Example side length; change as needed
        double area = CalculateDecagonArea(sideLength);
        Console.WriteLine($"The area of the regular decagon is: {area}");
    }

    static double CalculateDecagonArea(double sideLength)
    {
        // Formula: (5/2) * sideLength^2 * cot(pi/10)
        double angle = Math.PI / 10; // 18 degrees in radians
        double area = (5.0 / 2.0) * Math.Pow(sideLength, 2) * (1.0 / Math.Tan(angle));
        return area;
    }
}