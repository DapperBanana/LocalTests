
import xml.etree.ElementTree as ET

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    users = []
    
    for user in root.findall('user'):
        name = user.find('name').text
        users.append(name)
    
    return users

file_path = 'data.xml'
users = parse_xml(file_path)

for user in users:
    print(user)
