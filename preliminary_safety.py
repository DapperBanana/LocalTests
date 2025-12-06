using System;
using System.Xml;

class Program
{
    static void Main()
    {
        string filePath = "yourfile.xml"; // Replace with your XML file path

        XmlDocument xmlDoc = new XmlDocument();

        try
        {
            xmlDoc.Load(filePath);

            // Example: Extract all elements with a specific tag, e.g., "Item"
            XmlNodeList items = xmlDoc.GetElementsByTagName("Item");

            foreach (XmlNode item in items)
            {
                // Example: Extract "Name" and "Value" child elements
                string name = item["Name"]?.InnerText;
                string value = item["Value"]?.InnerText;

                Console.WriteLine($"Name: {name}, Value: {value}");
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error reading XML file: {e.Message}");
        }
    }
}