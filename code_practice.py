
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Get all the items in the XML file
items = root.findall('.//item')

# Iterate through each item and extract specific information
for item in items:
    name = item.find('name').text
    price = item.find('price').text
    quantity = item.find('quantity').text
    
    print(f"Item: {name} | Price: {price} | Quantity: {quantity}")
