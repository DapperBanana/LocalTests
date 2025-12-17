// Note: This is a simple implementation of linear regression in C#
using System;

class LinearRegression
{
    private double[] x;
    private double[] y;
    private double slope;
    private double intercept;

    public LinearRegression(double[] x, double[] y)
    {
        this.x = x;
        this.y = y;
        CalculateRegression();
    }

    private void CalculateRegression()
    {
        int n = x.Length;
        double sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;

        for (int i = 0; i < n; i++)
        {
            sumX += x[i];
            sumY += y[i];
            sumXY += x[i] * y[i];
            sumX2 += x[i] * x[i];
        }

        double denominator = (n * sumX2 - sumX * sumX);
        if (denominator == 0)
        {
            throw new InvalidOperationException("Division by zero in regression calculation.");
        }

        slope = (n * sumXY - sumX * sumY) / denominator;
        intercept = (sumY - slope * sumX) / n;
    }

    public double Predict(double xValue)
    {
        return slope * xValue + intercept;
    }

    public void PrintParameters()
    {
        Console.WriteLine($"Slope (m): {slope}");
        Console.WriteLine($"Intercept (b): {intercept}");
    }
}

class Program
{
    static void Main()
    {
        // Sample data
        double[] xData = { 1, 2, 3, 4, 5 };
        double[] yData = { 2, 4, 5, 4, 5 };

        LinearRegression model = new LinearRegression(xData, yData);
        model.PrintParameters();

        double prediction = model.Predict(6);
        Console.WriteLine($"Prediction for x=6: {prediction}");
    }
}