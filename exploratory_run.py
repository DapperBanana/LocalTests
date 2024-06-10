
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Extract specific information
for person in root.findall('person'):
    name = person.find('name').text
    age = person.find('age').text
    occupation = person.find('occupation').text
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Occupation: {occupation}")
    print()
