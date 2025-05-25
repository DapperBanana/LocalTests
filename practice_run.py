
from xml.dom import minidom

def is_valid_xml_with_dtd(xml_string):
    try:
        dom = minidom.parseString(xml_string)
        dtd = dom.doctype
        if dtd:
            return True
        else:
            return False
    except Exception as e:
        return False

# Test the function
xml_string1 = """<?xml version="1.0"?>
<!DOCTYPE note SYSTEM "note.dtd">
<note>
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
</note>"""

xml_string2 = """<?xml version="1.0"?>
<note>
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
</note>"""

print(is_valid_xml_with_dtd(xml_string1))  # Output: True
print(is_valid_xml_with_dtd(xml_string2))  # Output: False
