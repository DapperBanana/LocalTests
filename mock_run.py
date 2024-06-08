
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Extract specific information from the XML file
for child in root:
    if child.tag == 'person':
        name = child.find('name').text
        age = child.find('age').text
        email = child.find('email').text
        print(f"Name: {name}, Age: {age}, Email: {email}")
