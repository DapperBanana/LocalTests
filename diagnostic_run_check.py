
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Extract specific information
for child in root:
    if child.tag == 'person':
        name = child.find('name').text
        age = child.find('age').text
        print(f'Name: {name}, Age: {age}')
