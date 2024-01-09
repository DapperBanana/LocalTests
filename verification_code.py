
import xml.etree.ElementTree as ET

# Path to the XML file
xml_file = 'example.xml'

# Parse the XML file
tree = ET.parse(xml_file)
root = tree.getroot()

# Extract specific information
for item in root.findall('.//item'):
    item_name = item.find('name').text
    item_price = item.find('price').text
    item_description = item.find('description').text

    print(f'Name: {item_name}')
    print(f'Price: {item_price}')
    print(f'Description: {item_description}')
    print('---')
