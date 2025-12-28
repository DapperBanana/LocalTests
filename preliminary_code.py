// Basic Linear Regression Implementation in C#

using System;

class LinearRegression
{
    public double Slope { get; private set; }
    public double Intercept { get; private set; }

    // Fit the model to the data
    public void Fit(double[] x, double[] y)
    {
        if (x.Length != y.Length)
            throw new ArgumentException("Input arrays must have the same length.");

        int n = x.Length;
        double sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;

        for (int i = 0; i < n; i++)
        {
            sumX += x[i];
            sumY += y[i];
            sumXY += x[i] * y[i];
            sumX2 += x[i] * x[i];
        }

        double denominator = n * sumX2 - sumX * sumX;

        if (denominator == 0)
            throw new InvalidOperationException("Denominator is zero. Cannot compute linear regression.");

        Slope = (n * sumXY - sumX * sumY) / denominator;
        Intercept = (sumY - Slope * sumX) / n;
    }

    // Predict the y value for a given x
    public double Predict(double x)
    {
        return Slope * x + Intercept;
    }
}

class Program
{
    static void Main()
    {
        // Example data
        double[] xData = { 1, 2, 3, 4, 5 };
        double[] yData = { 2, 4, 5, 4, 5 };

        var model = new LinearRegression();
        model.Fit(xData, yData);

        Console.WriteLine($"Slope: {model.Slope}");
        Console.WriteLine($"Intercept: {model.Intercept}");

        double newX = 6;
        double prediction = model.Predict(newX);
        Console.WriteLine($"Prediction for x = {newX}: {prediction}");
    }
}