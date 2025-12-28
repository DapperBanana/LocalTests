// C# code to generate a simple line chart from a dictionary of data
using System;
using System.Collections.Generic;
using OxyPlot;
using OxyPlot.Series;
using OxyPlot.WindowsForms;

class Program
{
    static void Main()
    {
        // Example data: dictionary with x and y values
        var data = new Dictionary<double, double>
        {
            {1, 2},
            {2, 4},
            {3, 1},
            {4, 3},
            {5, 5}
        };

        // Create the plot model
        var plotModel = new PlotModel { Title = "Simple Line Chart" };
        var lineSeries = new LineSeries { Title = "Data" };

        // Add data points to the series
        foreach (var point in data)
        {
            lineSeries.Points.Add(new DataPoint(point.Key, point.Value));
        }

        plotModel.Series.Add(lineSeries);

        // Create a Windows Forms Plot View to display the chart
        var plotView = new PlotView
        {
            Model = plotModel,
            Dock = System.Windows.Forms.DockStyle.Fill
        };

        // Create and show a Windows Form
        var form = new System.Windows.Forms.Form
        {
            Text = "Line Chart",
            Width = 800,
            Height = 600
        };
        form.Controls.Add(plotView);

        System.Windows.Forms.Application.EnableVisualStyles();
        System.Windows.Forms.Application.Run(form);
    }
}