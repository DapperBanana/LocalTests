
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Extract specific information
for item in root.findall('item'):
    name = item.find('name').text
    price = item.find('price').text
    description = item.find('description').text
    
    print('Name:', name)
    print('Price:', price)
    print('Description:', description)
    print('-----------------------------')
