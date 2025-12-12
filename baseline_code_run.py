using System;
using System.Drawing;
using System.Drawing.Imaging;

class Program
{
    static void Main(string[] args)
    {
        string imagePath = "path_to_your_image.jpg";

        try
        {
            using (Image image = Image.FromFile(imagePath))
            {
                // Get Basic Metadata
                Console.WriteLine($"Width: {image.Width}");
                Console.WriteLine($"Height: {image.Height}");
                Console.WriteLine($"Pixel Format: {image.PixelFormat}");

                // Get Property Items (Exif Metadata)
                PropertyItem[] props = image.PropertyItems;

                foreach (var prop in props)
                {
                    string name = GetPropertyName(prop.Id);
                    string value = GetPropertyValue(prop);
                    Console.WriteLine($"{name} (ID: 0x{prop.Id:X}): {value}");
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }

    static string GetPropertyName(int propertyId)
    {
        // Common Exif tags
        switch (propertyId)
        {
            case 0x010F: return "Make";
            case 0x0110: return "Model";
            case 0x0132: return "DateTime";
            case 0x9003: return "DateTimeOriginal";
            case 0x829A: return " ExposureTime";
            case 0x8827: return "ISOSpeedRatings";
            case 0x9209: return "Flash";
            case 0x9204: return "ExposureBiasValue";
            case 0x9201: return "ShutterSpeedValue";
            case 0x9202: return "ApertureValue";
            case 0x9207: return "MeteringMode";
            case 0x9208: return "LightSource";
            default: return $"Unknown (0x{propertyId:X})";
        }
    }

    static string GetPropertyValue(PropertyItem prop)
    {
        try
        {
            // Attempt to decode the value appropriately based on type
            switch (prop.Type)
            {
                case 1: // byte
                case 7: // undefined
                    return BitConverter.ToString(prop.Value);
                case 2: // ASCII
                    string asciiStr = System.Text.Encoding.ASCII.GetString(prop.Value);
                    return asciiStr.Trim('\0');
                case 3: // short
                    return BitConverter.ToUInt16(prop.Value, 0).ToString();
                case 4: // long
                    return BitConverter.ToUInt32(prop.Value, 0).ToString();
                case 5: // rational
                    uint numerator = BitConverter.ToUInt32(prop.Value, 0);
                    uint denominator = BitConverter.ToUInt32(prop.Value, 4);
                    return $"{numerator}/{denominator}";
                case 9: // slong
                    return BitConverter.ToInt32(prop.Value, 0).ToString();
                case 10: // srational
                    int snumerator = BitConverter.ToInt32(prop.Value, 0);
                    int sdenominator = BitConverter.ToInt32(prop.Value, 4);
                    return $"{snumerator}/{sdenominator}";
                default:
                    return BitConverter.ToString(prop.Value);
            }
        }
        catch
        {
            return "Unable to decode";
        }
    }
}