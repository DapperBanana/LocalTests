
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('books.xml')
root = tree.getroot()

# Iterate through each book element
for book in root.findall('.//book'):
    title = book.find('title').text
    author = book.find('author').text
    print('Title: ', title)
    print('Author: ', author)
    print('------------')
