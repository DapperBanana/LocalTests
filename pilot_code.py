using System;
using System.Xml;

class Program
{
    static void Main()
    {
        string filename = "yourfile.xml"; // replace with your XML file path
        XmlDocument doc = new XmlDocument();

        try
        {
            doc.Load(filename);

            // Example: Extract all elements with specific tag, e.g., "Item"
            XmlNodeList items = doc.GetElementsByTagName("Item");
            foreach (XmlNode item in items)
            {
                // Extract specific information, e.g., attribute "id" and inner text
                string id = item.Attributes["id"]?.InnerText;
                string value = item.InnerText;

                Console.WriteLine($"ID: {id}, Value: {value}");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error parsing XML: {ex.Message}");
        }
    }
}