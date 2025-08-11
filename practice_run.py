
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Extract specific information
for student in root.findall('student'):
    name = student.find('name').text
    grade = student.find('grade').text
    print(f"Name: {name}, Grade: {grade}")
