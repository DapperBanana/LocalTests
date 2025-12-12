using System;
using System.Collections.Generic;

namespace SimpleBarChart
{
    class Program
    {
        static void Main(string[] args)
        {
            // Sample data: category and value
            var data = new Dictionary<string, int>
            {
                {"A", 5},
                {"B", 8},
                {"C", 3},
                {"D", 10}
            };

            // Find the maximum value for scaling
            int maxValue = 0;
            foreach (var value in data.Values)
            {
                if (value > maxValue)
                    maxValue = value;
            }

            // Define the maximum bar length
            int maxBarLength = 50;

            // Generate the bar chart
            foreach (var kvp in data)
            {
                string category = kvp.Key;
                int value = kvp.Value;

                // Calculate the number of characters for the bar
                int barLength = (int)((double)value / maxValue * maxBarLength);

                // Generate the bar string
                string bar = new string('#', barLength);

                // Output the category, bar, and value
                Console.WriteLine($"{category}: {bar} ({value})");
            }
        }
    }
}