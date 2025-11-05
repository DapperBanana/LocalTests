
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Extract specific information
for person in root:
    name = person.find('name').text
    age = person.find('age').text
    print(f"Name: {name}, Age: {age}")
