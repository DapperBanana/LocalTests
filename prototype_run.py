
from xml.etree import ElementTree as ET

def is_valid_xml_with_dtd(xml_str):
    try:
        root = ET.fromstring(xml_str)
        if root.tag.startswith('<?xml') and len(root) == 0:
            return False
    except ET.ParseError:
        return False
    
    return True

# Test the function with a sample XML string
sample_xml = '''<?xml version="1.0"?>
<!DOCTYPE note SYSTEM "note.dtd">
<note>
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
</note>'''

if is_valid_xml_with_dtd(sample_xml):
    print("The given string is a valid XML document with a DTD.")
else:
    print("The given string is not a valid XML document with a DTD.")
