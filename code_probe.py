
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Find and extract specific information
for item in root.findall('.//item'):
    name = item.find('name').text
    price = item.find('price').text
    currency = item.find('currency').text
    print(f'Item: {name}, Price: {price} {currency}')
