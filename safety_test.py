using System;

class WeatherForecastingSystem
{
    static void Main()
    {
        Console.WriteLine("Welcome to the Basic Text-Based Weather Forecasting System!");

        // Ask the user for the city name
        Console.Write("Enter the city name: ");
        string city = Console.ReadLine();

        // Ask for the current temperature
        Console.Write("Enter the current temperature in Celsius: ");
        if (!double.TryParse(Console.ReadLine(), out double temperature))
        {
            Console.WriteLine("Invalid temperature input. Please enter a numeric value.");
            return;
        }

        // Ask for weather condition
        Console.Write("Enter the weather condition (sunny, cloudy, rainy, snowy): ");
        string condition = Console.ReadLine().ToLower();

        // Provide a simple forecast based on inputs
        string forecast = GenerateForecast(temperature, condition);

        // Display forecast
        Console.WriteLine($"\nWeather forecast for {city}:");
        Console.WriteLine(forecast);
    }

    static string GenerateForecast(double temperature, string condition)
    {
        if (condition == "sunny")
        {
            if (temperature > 25)
                return "It's hot and sunny. Perfect for outdoor activities!";
            else
                return "It's mildly sunny. A comfortable day.";
        }
        else if (condition == "cloudy")
        {
            if (temperature > 20)
                return "It's a warm, cloudy day.";
            else
                return "It's a bit chilly with cloudy skies.";
        }
        else if (condition == "rainy")
        {
            if (temperature > 15)
                return "It's warm and rainy. Don't forget your umbrella!";
            else
                return "It's cold and rainy. Stay warm!";
        }
        else if (condition == "snowy")
        {
            if (temperature < 0)
                return "It's snowy and freezing. Stay indoors if possible.";
            else
                return "It's snowy but not too cold.";
        }
        else
        {
            return "Weather condition unknown. Please check the inputs.";
        }
    }
}