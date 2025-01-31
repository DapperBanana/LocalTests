
import xml.etree.ElementTree as ET

def is_valid_xml_with_dtd(xml_str):
    try:
        root = ET.fromstring(xml_str)
        if root.docinfo.internalDTD:
            return True
        else:
            return False
    except ET.ParseError:
        return False

# Test the function with an example XML document
xml_document = """
<!DOCTYPE note SYSTEM "note.dtd">
<note>
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
</note>
"""

if is_valid_xml_with_dtd(xml_document):
    print("The given XML document is valid with a DTD.")
else:
    print("The given XML document is not valid with a DTD.")
