
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Iterate through each 'person' element in the XML file
for person in root.findall('person'):
    # Extract the name and age of each person
    name = person.find('name').text
    age = person.find('age').text
    
    # Print out the name and age of each person
    print(f"Name: {name}, Age: {age}")
