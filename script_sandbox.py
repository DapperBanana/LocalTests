using System;
using System.Drawing;
using System.Drawing.Imaging;
using QRCoder;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter the text to encode into QR code:");
        string input = Console.ReadLine();

        using (QRCodeGenerator qrGenerator = new QRCodeGenerator())
        {
            QRCodeData qrCodeData = qrGenerator.CreateQrCode(input, QRCodeGenerator.ECCLevel.Q);
            using (QRCode qrCode = new QRCode(qrCodeData))
            {
                using (Bitmap qrCodeImage = qrCode.GetGraphic(20))
                {
                    string filePath = "qrcode.png";
                    qrCodeImage.Save(filePath, ImageFormat.Png);
                    Console.WriteLine($"QR code saved to {filePath}");
                }
            }
        }
    }
}