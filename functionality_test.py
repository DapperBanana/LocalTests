
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Loop through each 'person' element in the XML
for person in root.findall('person'):
    name = person.find('name').text
    age = person.find('age').text
    print(f"Name: {name}, Age: {age}")
