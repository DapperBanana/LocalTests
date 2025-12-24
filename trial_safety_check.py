// Note: The following code requires the Emgu CV library (a .NET wrapper for OpenCV).
// Make sure to install Emgu CV via NuGet package manager before running this code.

using System;
using Emgu.CV;
using Emgu.CV.Structure;

class ImageProcessing
{
    static void Main(string[] args)
    {
        // Load the image from disk
        string imagePath = "path_to_your_image.jpg";
        Mat image = CvInvoke.Imread(imagePath, Emgu.CV.CvEnum.ImreadModes.Color);

        if (image.IsEmpty)
        {
            Console.WriteLine("Failed to load image.");
            return;
        }

        // Convert to grayscale
        Mat grayImage = new Mat();
        CvInvoke.CvtColor(image, grayImage, Emgu.CV.CvEnum.ColorConversion.Bgr2Gray);

        // Save the grayscale image
        string outputPath = "grayscale_image.jpg";
        CvInvoke.Imwrite(outputPath, grayImage);

        Console.WriteLine($"Grayscale image saved to {outputPath}");
    }
}