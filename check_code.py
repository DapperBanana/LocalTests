
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Extract specific information
for child in root:
    if child.tag == 'book':
        title = child.find('title').text
        author = child.find('author').text
        price = child.find('price').text
        print(f'Title: {title}, Author: {author}, Price: {price}')
