
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Iterate through each 'person' element in the XML file
for person in root.findall('person'):
    name = person.find('name').text
    age = person.find('age').text

    print(f"Name: {name}, Age: {age}")
