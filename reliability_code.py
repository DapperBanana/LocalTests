// Note: C# does not have a built-in way to create bar charts directly.
// You can use a graphics library like System.Drawing to draw a chart to a bitmap.
// Below is an example of how you might generate a simple bar chart using System.Drawing.

using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;

class Program
{
    static void Main()
    {
        // Sample data: dictionary of labels and values
        var data = new Dictionary<string, int>
        {
            { "A", 10 },
            { "B", 25 },
            { "C", 15 },
            { "D", 30 }
        };

        int width = 400;
        int height = 300;
        int margin = 40;

        using (var bitmap = new Bitmap(width, height))
        using (var graphics = Graphics.FromImage(bitmap))
        {
            graphics.Clear(Color.White);

            // Draw axes
            Pen axisPen = Pens.Black;
            // X-axis
            graphics.DrawLine(axisPen, margin, height - margin, width - margin, height - margin);
            // Y-axis
            graphics.DrawLine(axisPen, margin, margin, margin, height - margin);

            // Calculate max value for scaling
            int maxVal = 0;
            foreach (var val in data.Values)
                if (val > maxVal) maxVal = val;

            int numBars = data.Count;
            int barWidth = (width - 2 * margin) / numBars - 10;

            int index = 0;
            foreach (var kvp in data)
            {
                string label = kvp.Key;
                int value = kvp.Value;

                // Calculate bar height based on value
                int barHeight = (int)((double)value / maxVal * (height - 2 * margin));

                // Calculate position
                int x = margin + index * (barWidth + 10) + 5;
                int y = height - margin - barHeight;

                // Draw bar
                graphics.FillRectangle(Brushes.Blue, x, y, barWidth, barHeight);

                // Draw label
                var labelSize = graphics.MeasureString(label, SystemFonts.DefaultFont);
                graphics.DrawString(label, SystemFonts.DefaultFont, Brushes.Black, x + (barWidth - labelSize.Width) / 2, height - margin + 5);

                index++;
            }

            // Save the image
            bitmap.Save("barchart.png", ImageFormat.Png);
        }

        Console.WriteLine("Bar chart saved as 'barchart.png'");
    }
}