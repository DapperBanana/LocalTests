
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('books.xml')
root = tree.getroot()

# Create empty lists to store book titles and authors
titles = []
authors = []

# Loop through each <book> element in the XML file
for book in root.findall('book'):
    # Get the title and author of each book
    title = book.find('title').text
    author = book.find('author').text
    
    # Append the title and author to their respective lists
    titles.append(title)
    authors.append(author)

# Print the extracted information
for i in range(len(titles)):
    print(f"Book {i + 1}:")
    print(f"Title: {titles[i]}")
    print(f"Author: {authors[i]}")
    print()

