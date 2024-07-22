
from xml.dom import minidom

def is_valid_xml_with_dtd(xml_string):
    try:
        document = minidom.parseString(xml_string)
        if document.doctype:
            return True
        else:
            return False
    except Exception as e:
        return False

# Test the function
xml_string = '''<?xml version="1.0"?>
<!DOCTYPE note SYSTEM "note.dtd">
<note>
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
</note>'''

if is_valid_xml_with_dtd(xml_string):
    print("The given string is a valid XML document with a DTD.")
else:
    print("The given string is not a valid XML document with a DTD.")
