
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('file.xml')
root = tree.getroot()

# Extract specific information
for child in root:
    if child.tag == 'element1':
        print('Element 1:', child.text)
    elif child.tag == 'element2':
        attribute_value = child.get('attribute_name')
        print('Element 2 Attribute:', attribute_value)
    elif child.tag == 'element3':
        for sub_child in child:
            print('Element 3 Sub-element:', sub_child.text)
    else:
        print('Unknown element:', child.tag)
