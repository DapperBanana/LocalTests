
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Extract specific information
for child in root:
    if child.tag == 'book':
        title = child.find('title').text
        author = child.find('author').text
        genre = child.find('genre').text
        price = child.find('price').text
        print(f'Title: {title}, Author: {author}, Genre: {genre}, Price: {price}')
