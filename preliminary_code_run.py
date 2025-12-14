using System;

class TemperatureConverter
{
    static void Main()
    {
        Console.Write("Enter temperature in Celsius: ");
        string input = Console.ReadLine();
        if (double.TryParse(input, out double celsius))
        {
            double fahrenheit = (celsius * 9 / 5) + 32;
            Console.WriteLine($"{celsius}°C is equivalent to {fahrenheit}°F");
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a numerical value.");
        }
    }
}