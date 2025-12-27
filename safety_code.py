using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;

public class ImageMetadataExtractor
{
    public static void Main(string[] args)
    {
        string imagePath = "path_to_your_image.jpg"; // Replace with your image path

        if (!File.Exists(imagePath))
        {
            Console.WriteLine("Image file does not exist.");
            return;
        }

        try
        {
            using (Image img = Image.FromFile(imagePath))
            {
                Console.WriteLine($"Width: {img.Width}px");
                Console.WriteLine($"Height: {img.Height}px");
                Console.WriteLine($"Horizontal Resolution: {img.HorizontalResolution} dpi");
                Console.WriteLine($"Vertical Resolution: {img.VerticalResolution} dpi");
                Console.WriteLine($"Pixel Format: {img.PixelFormat}");

                // Extracting metadata properties
                foreach (PropertyItem propItem in img.PropertyItems)
                {
                    string value = "";

                    switch (propItem.Id)
                    {
                        case 0x010F: // Make
                            value = System.Text.Encoding.ASCII.GetString(propItem.Value).Trim('\0');
                            Console.WriteLine($"Camera Make: {value}");
                            break;
                        case 0x0110: // Model
                            value = System.Text.Encoding.ASCII.GetString(propItem.Value).Trim('\0');
                            Console.WriteLine($"Camera Model: {value}");
                            break;
                        case 0x0132: // DateTime
                            value = System.Text.Encoding.ASCII.GetString(propItem.Value).Trim('\0');
                            Console.WriteLine($"Date Taken: {value}");
                            break;
                        case 0x9003: // DateTimeOriginal
                            value = System.Text.Encoding.ASCII.GetString(propItem.Value).Trim('\0');
                            Console.WriteLine($"Original Date/Time: {value}");
                            break;
                        case 0x010E: // Image Description
                            value = System.Text.Encoding.ASCII.GetString(propItem.Value).Trim('\0');
                            Console.WriteLine($"Image Description: {value}");
                            break;
                        case 0x8827: // ISOSpeedRatings
                            value = BitConverter.ToString(propItem.Value);
                            Console.WriteLine($"ISO Speed Ratings: {BitConverter.ToString(propItem.Value)}");
                            break;
                        default:
                            // For other properties, display Id and raw value
                            value = BitConverter.ToString(propItem.Value);
                            Console.WriteLine($"Property ID 0x{propItem.Id:X}: {value}");
                            break;
                    }
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error reading image metadata: {ex.Message}");
        }
    }
}