
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Extract specific information from the XML file
for item in root.findall('item'):
    name = item.find('name').text
    price = item.find('price').text
    description = item.find('description').text

    print(f"Name: {name}")
    print(f"Price: {price}")
    print(f"Description: {description}")
    print()
