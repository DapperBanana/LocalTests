
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Extract specific information from the XML file
for item in root.findall('.//item'):
    name = item.find('name').text
    price = item.find('price').text

    print(f'Item: {name} - Price: {price}')
