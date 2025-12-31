using System;

class Program
{
    static void Main()
    {
        // Example points
        double x1 = 1, y1 = 2, z1 = 3;
        double x2 = 4, y2 = 5, z2 = 6;

        double distance = CalculateDistance3D(x1, y1, z1, x2, y2, z2);
        Console.WriteLine($"Distance between points: {distance}");
    }

    static double CalculateDistance3D(double x1, double y1, double z1, double x2, double y2, double z2)
    {
        double dx = x2 - x1;
        double dy = y2 - y1;
        double dz = z2 - z1;
        return Math.Sqrt(dx * dx + dy * dy + dz * dz);
    }
}