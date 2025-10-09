
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Loop through each book element in the XML file
for book in root.findall('book'):
    # Extract the title and author information
    title = book.find('title').text
    author = book.find('author').text

    # Display the extracted information
    print(f'Title: {title}')
    print(f'Author: {author}')
    print('----------------------')
