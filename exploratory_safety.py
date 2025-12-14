using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;

class ImageMetadataExtractor
{
    static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("Please provide the path to the image file.");
            return;
        }

        string imagePath = args[0];

        if (!File.Exists(imagePath))
        {
            Console.WriteLine("File does not exist: " + imagePath);
            return;
        }

        try
        {
            using (Image image = Image.FromFile(imagePath))
            {
                // Extract basic properties
                Console.WriteLine("Image Properties:");
                Console.WriteLine($"- Width: {image.Width} pixels");
                Console.WriteLine($"- Height: {image.Height} pixels");
                Console.WriteLine($"- Horizontal Resolution: {image.HorizontalResolution} dpi");
                Console.WriteLine($"- Vertical Resolution: {image.VerticalResolution} dpi");
                Console.WriteLine($"- Raw Format: {image.RawFormat}");

                // Extract PropertyItems (metadata)
                PropertyItem[] propertyItems = image.PropertyItems;

                Console.WriteLine("\nMetadata (PropertyItems):");
                foreach (var prop in propertyItems)
                {
                    string propIdHex = $"0x{prop.Id.ToString("X")}";
                    string propType = prop.Type.ToString();
                    string valueHex = BitConverter.ToString(prop.Value);

                    Console.WriteLine($"Property ID: {propIdHex}");
                    Console.WriteLine($"Type: {propType}");
                    Console.WriteLine($"Value (hex): {valueHex}");

                    // Optionally, decode common property IDs
                    switch (prop.Id)
                    {
                        case 0x010F:
                            Console.WriteLine($"Make: {DecodeStringProperty(prop)}");
                            break;
                        case 0x0110:
                            Console.WriteLine($"Model: {DecodeStringProperty(prop)}");
                            break;
                        case 0x9003:
                            Console.WriteLine($"DateTimeOriginal: {DecodeStringProperty(prop)}");
                            break;
                        case 0x010E:
                            Console.WriteLine($"Image Description: {DecodeStringProperty(prop)}");
                            break;
                        // Add more cases for known metadata tags if needed
                    }

                    Console.WriteLine();
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error reading image: " + ex.Message);
        }
    }

    // Helper method to decode string property
    static string DecodeStringProperty(PropertyItem prop)
    {
        try
        {
            // Remove null terminator if present
            string value = System.Text.Encoding.ASCII.GetString(prop.Value);
            return value.Trim('\0');
        }
        catch
        {
            return "Unable to decode";
        }
    }
}