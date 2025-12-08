using System;
using System.Xml;

public class Program
{
    public static void Main()
    {
        string xmlInput = "<root><child>Test</child></root>"; // Replace with your XML string
        bool isValid = IsValidXml(xmlInput);
        Console.WriteLine($"Is the input a valid XML? {isValid}");
    }

    public static bool IsValidXml(string xmlString)
    {
        try
        {
            var xmlDoc = new XmlDocument();
            xmlDoc.LoadXml(xmlString);
            return true; // Successfully loaded, so it's valid XML
        }
        catch (XmlException)
        {
            return false; // Invalid XML
        }
    }
}