
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Define the information to extract
info_to_extract = {
    'name': 'Name',
    'age': 'Age',
    'city': 'City'
}

# Iterate over the XML file and extract the specified information
for person in root.findall('Person'):
    info = {}
    for key, value in info_to_extract.items():
        info[key] = person.find(value).text
    print(info)
