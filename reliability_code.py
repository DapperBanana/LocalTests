// Function to calculate the area of the lateral surface of a frustum of a cone
public class FrustumCalculator
{
    // Method to calculate the lateral area
    public static double CalculateLateralArea(double r1, double r2, double h)
    {
        double slantHeight = Math.Sqrt(Math.Pow(r2 - r1, 2) + Math.Pow(h, 2));
        return Math.PI * (r1 + r2) * slantHeight;
    }
}

// Example usage
/*
double radius1 = 3.0; // Bottom radius
double radius2 = 2.0; // Top radius
double height = 5.0;  // Vertical height

double area = FrustumCalculator.CalculateLateralArea(radius1, radius2, height);
Console.WriteLine($"Lateral surface area of the frustum: {area}");
*/