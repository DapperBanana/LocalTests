// Note: This is C# code using OpenCV for image segmentation.
// Make sure you have Emgu CV installed and configured for C# development.

using Emgu.CV;
using Emgu.CV.CvEnum;
using Emgu.CV.Structure;
using Emgu.CV.Util;

public class ImageSegmentation
{
    public static void Main()
    {
        // Load the image
        Mat src = CvInvoke.Imread("path_to_image.jpg", ImreadModes.Color);
        if (src.IsEmpty)
        {
            Console.WriteLine("Image not found.");
            return;
        }

        // Convert image to grayscale
        Mat gray = new Mat();
        CvInvoke.CvtColor(src, gray, ColorConversion.Bgr2Gray);

        // Apply Gaussian blur to reduce noise
        CvInvoke.GaussianBlur(gray, gray, new Size(5, 5), 1);

        // Apply Otsu's thresholding
        Mat binary = new Mat();
        CvInvoke.Threshold(gray, binary, 0, 255, ThresholdType.Binary | ThresholdType.Otsu);

        // Find contours from binary image
        using (VectorOfVectorOfPoint contours = new VectorOfVectorOfPoint())
        {
            CvInvoke.FindContours(binary, contours, null, RetrType.External, ChainApproxMethod.ChainApproxSimple);

            // Draw contours on the original image
            for (int i = 0; i < contours.Size; i++)
            {
                CvInvoke.DrawContours(src, contours, i, new MCvScalar(0, 255, 0), 2);
            }
        }

        // Save or display the result
        CvInvoke.Imwrite("segmented_output.jpg", src);
        // Or display using CvInvoke.Imshow("Segmentation", src);
        // CvInvoke.WaitKey(0);
    }
}