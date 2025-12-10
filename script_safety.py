using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter the base area of the pyramid: ");
        double baseArea = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter the height of the pyramid: ");
        double height = Convert.ToDouble(Console.ReadLine());

        double volume = (1.0 / 3.0) * baseArea * height;

        Console.WriteLine($"The volume of the pyramid is: {volume}");
    }
}